"""iMessage tap for the TC assistant — read-only, local, never sends.

Every run: read the last N days of 1:1 iMessage/SMS threads from chat.db
(READ-ONLY), keep only threads with WORK contacts (the work-contacts CSV), and
write a small JSON snapshot the plugin's skills read as "texts" evidence.

    python3 -m tc_tap.tap --dry-run     # print the snapshot, write nothing

Privacy model (inherited from the EA tap, tightened):
- A contact is WORK only if the work-contacts CSV lists it with a non-personal
  category. Anyone not in the CSV — every friend, family member, unknown number —
  is personal, and personal threads are DROPPED ENTIRELY: no body, no name, no
  number, no timestamps. Only a count of skipped threads is written.
- Group chats are never read.
- Nothing leaves the Mac except the output file you point it at (normally a
  folder in Google Drive that syncs). No network calls, no send path exists.

Config (environment, or flags; flags win):
  TC_TAP_OUTPUT         where to write the snapshot (JSON)
  TC_TAP_CONTACTS_CSV   the work-contacts CSV (Category,Name,Contact)
  TC_TAP_LOOKBACK_DAYS  default 14
  TC_TAP_RECENT_CAP     messages kept per thread, default 15
  TC_TAP_RECENT_CHARS   chars kept per message, default 300
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import tempfile
import time
from datetime import UTC, datetime
from pathlib import Path

from tc_tap import chatdb
from tc_tap import contacts as contacts_mod

log = logging.getLogger("tc.tap")

SCHEMA_VERSION = 1
SUPPORT_DIR = "~/Library/Application Support/TC Assistant"
DEFAULT_OUTPUT = f"{SUPPORT_DIR}/imessage-threads.json"
DEFAULT_CONTACTS_CSV = f"{SUPPORT_DIR}/work-contacts.csv"
DEFAULT_CHAT_DB = "~/Library/Messages/chat.db"


def _iso(ts: float | None) -> str | None:
    if ts is None:
        return None
    return datetime.fromtimestamp(ts, tz=UTC).isoformat(timespec="seconds")


def build_snapshot(
    scan: chatdb.MessageScan,
    *,
    generated_at: str,
    lookback_days: int,
    contacts_csv_found: bool,
) -> dict:
    """Whitelist-only serialization. Personal threads never appear — not even
    as metadata — and each work thread carries a fixed key set, so a stray
    field upstream can't ride along."""
    work = [t for t in scan.threads if not t["personal"]]
    threads = []
    for t in work:
        last_in, last_out = t["last_inbound_ts"], t["last_outbound_ts"]
        threads.append(
            {
                "contact": t["contact"],
                "name": t.get("name"),
                "category": t["category"],
                "last_inbound_at": _iso(last_in),
                "last_outbound_at": _iso(last_out),
                # their last text is newer than anything sent back
                "awaiting_reply": bool(last_in and (last_out or 0) < last_in),
                "inbound_count": t["inbound_count"],
                "outbound_count": t["outbound_count"],
                "recent": [
                    {"at": _iso(m["ts"]), "from_me": bool(m["from_me"]), "text": m.get("text", "")}
                    for m in t.get("recent", [])
                ],
            }
        )
    return {
        "schema_version": SCHEMA_VERSION,
        "source": "imessage",
        "generated_at": generated_at,
        "lookback_days": lookback_days,
        "work_contacts_csv_found": contacts_csv_found,
        "threads": threads,
        "personal_threads_skipped": len(scan.threads) - len(work),
        "decode_failures": scan.decode_failures,
    }


def write_atomic(path: Path, data: dict) -> None:
    """Write via a temp file + rename so a reader (or Drive sync) never sees a
    half-written snapshot."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".imessage-", suffix=".json", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
            f.write("\n")
        os.chmod(tmp, 0o600)
        os.replace(tmp, path)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise


def run(args: argparse.Namespace) -> int:
    csv_path = Path(args.contacts_csv).expanduser()
    categories: dict[str, str] = {}
    if csv_path.exists():
        categories = contacts_mod.load_categories(csv_path)
    else:
        # Fail-safe: with no CSV every thread is personal, so nothing but a
        # count is written. Say so loudly — an empty snapshot is not "no texts".
        log.warning("work-contacts CSV not found at %s; every thread treated as personal", csv_path)

    try:
        names = contacts_mod.name_map()
    except Exception as exc:  # Contacts unreadable shouldn't kill the run
        log.warning("could not read Contacts for names (%s); continuing", exc.__class__.__name__)
        names = {}

    since = time.time() - args.lookback_days * 86400
    conn = chatdb.open_chat_db(Path(args.chat_db).expanduser())
    try:
        scan = chatdb.scan_messages(
            conn,
            since,
            categories,
            work_body_chars=args.recent_chars,
            personal_body_chars=0,
            names=names,
            recent_chars=args.recent_chars,
            recent_cap=args.recent_cap,
        )
    finally:
        conn.close()

    snapshot = build_snapshot(
        scan,
        generated_at=datetime.now(tz=UTC).isoformat(timespec="seconds"),
        lookback_days=args.lookback_days,
        contacts_csv_found=csv_path.exists(),
    )
    if args.dry_run:
        print(json.dumps(snapshot, indent=1, ensure_ascii=False))
        print(
            f"DRY RUN — would write {len(snapshot['threads'])} work threads "
            f"({snapshot['personal_threads_skipped']} personal skipped) to {args.output}",
            file=sys.stderr,
        )
        return 0
    out = Path(args.output).expanduser()
    write_atomic(out, snapshot)
    log.info(
        "wrote %d work threads (%d personal skipped) -> %s",
        len(snapshot["threads"]),
        snapshot["personal_threads_skipped"],
        out,
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    env = os.environ.get
    p = argparse.ArgumentParser(description="TC assistant iMessage tap (read-only, local)")
    p.add_argument("--dry-run", action="store_true", help="print the snapshot; write nothing")
    p.add_argument("--output", default=env("TC_TAP_OUTPUT", DEFAULT_OUTPUT))
    p.add_argument("--contacts-csv", default=env("TC_TAP_CONTACTS_CSV", DEFAULT_CONTACTS_CSV))
    p.add_argument("--chat-db", default=env("TC_TAP_CHAT_DB", DEFAULT_CHAT_DB))
    p.add_argument("--lookback-days", type=int, default=int(env("TC_TAP_LOOKBACK_DAYS", "14")))
    p.add_argument("--recent-cap", type=int, default=int(env("TC_TAP_RECENT_CAP", "15")))
    p.add_argument("--recent-chars", type=int, default=int(env("TC_TAP_RECENT_CHARS", "300")))
    args = p.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    try:
        return run(args)
    except chatdb.ChatDbUnavailableError as exc:
        # Skip the run rather than overwrite a good snapshot with a partial one.
        log.error("chat.db unavailable this run, skipping (previous snapshot kept): %s", exc)
        return 3


if __name__ == "__main__":
    sys.exit(main())
