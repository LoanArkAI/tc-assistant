"""READ-ONLY access to iMessage chat.db.

Primary path: sqlite URI mode=ro with busy_timeout retries.
Fallback (locked / WAL-recovery failure): APFS clone (`cp -c`) of
chat.db{,-wal,-shm} into a temp dir, open the CLONE read-write so SQLite can
recover the WAL, then PRAGMA quick_check — on any failure the run is skipped
rather than emitting partial data as complete (Fable review H7).
"""

from __future__ import annotations

import re
import sqlite3
import subprocess
import tempfile
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path

from . import contacts as contacts_mod

APPLE_EPOCH_UNIX = 978307200  # 2001-01-01 UTC as unix time
CHAT_STYLE_ONE_TO_ONE = 45  # chat.style: 45 = 1:1, 43 = group


class ChatDbUnavailableError(RuntimeError):
    """Raised when chat.db cannot be read consistently; the run is skipped."""


def apple_timestamp_to_unix(value: float | int | None) -> float | None:
    """message.date is nanoseconds since 2001 on modern macOS but SECONDS on
    pre-High Sierra rows; the regimes are ~9 orders of magnitude apart
    (Fable review M1)."""
    if value is None:
        return None
    value = float(value)
    if value > 1e12:
        value = value / 1e9
    return value + APPLE_EPOCH_UNIX


def open_chat_db(path: Path) -> sqlite3.Connection:
    if not path.exists():
        # Most likely cause when run under launchd: Full Disk Access not
        # granted to the pinned interpreter (Fable H2 / Pass B clone-empty-db).
        raise ChatDbUnavailableError(
            f"{path} not found or not visible — check Full Disk Access for the "
            f"interpreter in the launchd plist"
        )
    try:
        conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True, timeout=10)
        conn.execute("PRAGMA busy_timeout = 10000")
        conn.execute("SELECT count(*) FROM sqlite_master")  # force open/WAL read
        return conn
    except sqlite3.Error:
        return _open_cloned_copy(path)


def _open_cloned_copy(path: Path) -> sqlite3.Connection:
    import atexit
    import shutil

    tmpdir = Path(tempfile.mkdtemp(prefix="ea-chatdb-"))
    # The clone is the FULL message history; never leave it behind
    # (Pass B clone-leak).
    atexit.register(shutil.rmtree, tmpdir, ignore_errors=True)
    try:
        for suffix in ("", "-wal", "-shm"):
            src = Path(str(path) + suffix)
            if src.exists():
                # cp -c = APFS clonefile: near-instant, minimizes torn-copy window
                subprocess.run(["cp", "-c", str(src), str(tmpdir / src.name)], check=True)
    except subprocess.CalledProcessError as exc:
        raise ChatDbUnavailableError(
            f"could not clone chat.db (permissions? Full Disk Access?): rc={exc.returncode}"
        ) from None
    copy = tmpdir / path.name
    if not copy.exists():
        # sqlite3.connect would CREATE an empty db here that passes
        # quick_check — refuse instead (Pass B clone-empty-db).
        raise ChatDbUnavailableError(f"clone of {path.name} did not materialize")
    try:
        conn = sqlite3.connect(copy)  # read-write ON THE COPY so WAL recovery can run
        result = conn.execute("PRAGMA quick_check").fetchone()
        if result is None or result[0] != "ok":
            conn.close()
            raise ChatDbUnavailableError(f"cloned chat.db failed quick_check: {result}")
        return conn
    except sqlite3.Error as exc:
        raise ChatDbUnavailableError(
            f"cloned chat.db unreadable: {exc.__class__.__name__}"
        ) from exc


_TYPEDSTREAM_PREFIX = re.compile(rb"\x01[\x94\x95]\x84\x01\x2b")
_CONTROL_CHARS = re.compile(r"[\x00-\x08\x0b-\x1f\x7f]")


def decode_attributed_body(blob: bytes | None) -> str | None:
    """Minimal typedstream NSString extraction for rows whose text lives only
    in attributedBody. The expected prefix is validated explicitly so an
    unfamiliar encoding returns None (a COUNTED failure) instead of silently
    decoding garbage at a wrong offset (Fable review M3 + Pass B
    decode-garbage)."""
    if not blob:
        return None
    try:
        idx = blob.find(b"NSString")
        if idx == -1:
            return None
        start = idx + len(b"NSString")
        if not _TYPEDSTREAM_PREFIX.match(blob, start):
            return None  # unknown layout: refuse, don't guess
        start += 5
        marker = blob[start]
        if marker == 0x81:
            length = int.from_bytes(blob[start + 1 : start + 3], "little")
            text_start = start + 3
        elif marker == 0x82:
            length = int.from_bytes(blob[start + 1 : start + 5], "little")
            text_start = start + 5
        elif marker < 0x80:
            length = marker
            text_start = start + 1
        else:
            return None  # other 0x8x markers: layout we don't understand
        if length <= 0 or text_start + length > len(blob):
            return None  # length runs past the blob: corrupt, refuse
        text = blob[text_start : text_start + length].decode("utf-8", errors="strict")
        if _CONTROL_CHARS.search(text):
            return None  # control chars = we decoded the wrong bytes
        return text or None
    except (IndexError, UnicodeDecodeError, ValueError):
        return None


def sanitize_excerpt(body: str | None, limit: int) -> str:
    """Excerpts are interpolated into a markdown digest later delivered via
    an LLM-read file: collapse ALL whitespace (no newline = no
    injected headings/@channel lines) and drop control chars (Pass B
    md-inject)."""
    if not body or limit <= 0:
        return ""
    flat = " ".join(_CONTROL_CHARS.sub("", body).split())
    return flat[:limit]


@dataclass
class MessageScan:
    threads: list[dict] = field(default_factory=list)
    message_count: int = 0
    decode_failures: int = 0
    direction_anomalies: int = 0  # is_from_me=1 but handle_id != 0 etc., logged not used


def scan_messages(
    conn: sqlite3.Connection,
    since_unix: float,
    categories: dict[str, str],
    work_body_chars: int,
    personal_body_chars: int,
    names: dict[str, str] | None = None,
    recent_chars: int = 300,
    recent_cap: int = 15,
) -> MessageScan:
    """Per-1:1-thread summary for the digest. Group chats are excluded in
    Phase 0 (Fable review H5); direction comes from is_from_me alone (H6);
    personal-category bodies are minimized at the source (B4)."""
    scan = MessageScan()
    rows = conn.execute(
        """
        SELECT m.guid, m.date, m.is_from_me, m.handle_id,
               m.text, m.attributedBody,
               h.id AS handle, c.chat_identifier
        FROM message m
        JOIN chat_message_join cmj ON cmj.message_id = m.ROWID
        JOIN chat c ON c.ROWID = cmj.chat_id
        LEFT JOIN handle h ON h.ROWID = m.handle_id
        WHERE c.style = ?
          AND m.date > ?
          AND IFNULL(m.associated_message_type, 0) = 0
          AND IFNULL(m.item_type, 0) = 0
        ORDER BY m.date ASC
        """,
        (CHAT_STYLE_ONE_TO_ONE, _unix_to_apple_ns(since_unix)),
    )
    # associated_message_type != 0 = tapbacks/edits/unsends; item_type != 0 =
    # group-rename etc. Counting those as messages marks threads falsely
    # answered (the agent ❤️s a question) or falsely unanswered (a client ❤️s
    # the reply) — Pass B [tapbacks].

    seen_guids: set[str] = set()
    threads: dict[str, dict] = {}
    for guid, date_raw, is_from_me, handle_id, text, attributed, handle, chat_identifier in rows:
        if guid in seen_guids:  # merged SMS/iMessage threads can join twice
            continue
        seen_guids.add(guid)
        scan.message_count += 1

        body = text
        if body is None:
            body = decode_attributed_body(attributed)
            if body is None and attributed:
                scan.decode_failures += 1
        if bool(is_from_me) and handle_id not in (0, None):
            scan.direction_anomalies += 1  # counted only; is_from_me stays authoritative

        contact = contacts_mod.normalize_contact(handle or chat_identifier)
        if contact is None:
            continue
        category = categories.get(contact)
        # Uncategorized contacts get the PERSONAL treatment (bodies stay
        # home): a new friend texting the agent must not leak into the output just
        # because the CSV hasn't caught up — Pass B [uncategorized-privacy].
        personal = contacts_mod.is_personal(category) or category is None
        limit = personal_body_chars if personal else work_body_chars
        excerpt = sanitize_excerpt(body, limit)

        ts = apple_timestamp_to_unix(date_raw)
        thread = threads.setdefault(
            contact,
            {
                "contact": contact,
                "name": (names or {}).get(contact),  # tap v2: Contacts display name, or None
                "category": category or "Uncategorized",
                "personal": personal,
                "last_inbound_ts": None,
                "last_outbound_ts": None,
                "last_inbound_excerpt": "",
                "recent": [],  # tap v2: conversation window, WORK threads only
                "inbound_count": 0,
                "outbound_count": 0,
            },
        )
        if is_from_me:
            thread["outbound_count"] += 1
            if ts and (thread["last_outbound_ts"] or 0) < ts:
                thread["last_outbound_ts"] = ts
        else:
            thread["inbound_count"] += 1
            if ts and (thread["last_inbound_ts"] or 0) < ts:
                thread["last_inbound_ts"] = ts
                thread["last_inbound_excerpt"] = excerpt
        # tap v2 conversation window — bodies for WORK threads only (B4: never
        # collect for personal, same guard as the excerpt).
        if not personal:
            thread["recent"].append(
                {
                    "ts": ts,
                    "from_me": bool(is_from_me),
                    "text": sanitize_excerpt(body, recent_chars),
                }
            )

    for thread in threads.values():
        thread["recent"] = thread["recent"][-recent_cap:]  # keep the last N, chronological
    scan.threads = sorted(threads.values(), key=lambda t: t["last_inbound_ts"] or 0, reverse=True)
    return scan


def _unix_to_apple_ns(unix_ts: float) -> int:
    return int((unix_ts - APPLE_EPOCH_UNIX) * 1e9)


def iso(ts: float | None) -> str | None:
    if ts is None:
        return None
    return datetime.fromtimestamp(ts, tz=UTC).astimezone().isoformat(timespec="seconds")
