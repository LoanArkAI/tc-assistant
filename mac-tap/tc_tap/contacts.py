"""READ-ONLY access to macOS Contacts (AddressBook sqlite) and contact
normalization shared by every data source.

The root AddressBook-v22.abcddb is often a near-empty stub on iCloud-synced
Macs; the real records live under Sources/<UUID>/. We enumerate and merge all
of them (Fable review M4).
"""

from __future__ import annotations

import re
import sqlite3
from datetime import UTC, datetime, timedelta
from pathlib import Path

APPLE_EPOCH = datetime(2001, 1, 1, tzinfo=UTC)
_DIGITS = re.compile(r"\D+")


def normalize_contact(value: str | None) -> str | None:
    """Canonical form for matching across iMessage handles, the contact
    work-contacts CSV, and Follow Up Boss: E.164 for US numbers, lowercase for
    emails, bare digits for short codes (Fable review M2)."""
    if not value:
        return None
    value = value.strip()
    if "@" in value:
        return value.lower()
    digits = _DIGITS.sub("", value)
    if not digits:
        return None
    if len(digits) == 11 and digits.startswith("1"):
        return f"+{digits}"
    if len(digits) == 10:
        return f"+1{digits}"
    return digits  # short codes and international stay as-is


def addressbook_paths(home: Path | None = None) -> list[Path]:
    home = home or Path.home()
    base = home / "Library" / "Application Support" / "AddressBook"
    paths = [base / "AddressBook-v22.abcddb"]
    paths.extend(sorted(base.glob("Sources/*/AddressBook-v22.abcddb")))
    return [p for p in paths if p.exists()]


def _open_ro(path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    conn.execute("PRAGMA busy_timeout = 5000")
    return conn


def read_contacts(home: Path | None = None) -> list[dict]:
    """Names, normalized phones/emails, and birthdays from every
    AddressBook source DB, deduped by normalized contact value."""
    people: dict[str, dict] = {}
    for db_path in addressbook_paths(home):
        conn = _open_ro(db_path)
        try:
            rows = conn.execute(
                """
                SELECT r.Z_PK, r.ZFIRSTNAME, r.ZLASTNAME, r.ZBIRTHDAY
                FROM ZABCDRECORD r
                WHERE r.ZFIRSTNAME IS NOT NULL OR r.ZLASTNAME IS NOT NULL
                """
            ).fetchall()
            phones: dict[int, list[str]] = {}
            for owner, number in conn.execute(
                "SELECT ZOWNER, ZFULLNUMBER FROM ZABCDPHONENUMBER WHERE ZFULLNUMBER IS NOT NULL"
            ):
                phones.setdefault(owner, []).append(number)
            emails: dict[int, list[str]] = {}
            for owner, address in conn.execute(
                "SELECT ZOWNER, ZADDRESS FROM ZABCDEMAILADDRESS WHERE ZADDRESS IS NOT NULL"
            ):
                emails.setdefault(owner, []).append(address)
        finally:
            conn.close()

        for pk, first, last, birthday_raw in rows:
            name = " ".join(p for p in (first, last) if p).strip()
            birthday = None
            if birthday_raw is not None:
                try:
                    birthday = (
                        (APPLE_EPOCH + timedelta(seconds=float(birthday_raw))).date().isoformat()
                    )
                except (ValueError, OverflowError):
                    birthday = None
            handles = [normalize_contact(v) for v in phones.get(pk, []) + emails.get(pk, [])]
            handles = [h for h in handles if h]
            for handle in handles:
                existing = people.get(handle)
                if existing is None:
                    people[handle] = {"name": name, "contact": handle, "birthday": birthday}
                elif birthday and not existing.get("birthday"):
                    existing["birthday"] = birthday
    return sorted(people.values(), key=lambda p: p["contact"])


def name_map(home: Path | None = None) -> dict[str, str]:
    """normalized handle -> display name, from Contacts (tap v2). Blank names
    and handle-less rows are excluded; unknown handles simply won't be in the
    map, so callers treat a miss as 'no name' (None)."""
    return {
        p["contact"]: p["name"] for p in read_contacts(home) if p.get("name") and p.get("contact")
    }


def load_categories(csv_path: Path) -> dict[str, str]:
    """normalized contact -> category from the Contact Categories CSV."""
    import csv

    categories: dict[str, str] = {}
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            normalized = normalize_contact(row.get("Contact", ""))
            if normalized:
                categories[normalized] = row.get("Category", "").strip()
    return categories


PERSONAL_CATEGORIES = {"Friends & Family", "Personal", "Family"}


def is_personal(category: str | None) -> bool:
    return (category or "") in PERSONAL_CATEGORIES
