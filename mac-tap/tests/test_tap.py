import json
import sqlite3
import time

from tc_tap import chatdb, tap

NOW = time.time()
NS = lambda unix: int((unix - chatdb.APPLE_EPOCH_UNIX) * 1e9)  # noqa: E731

CLIENT = "+17145550101"
FRIEND = "+19495550202"
STRANGER = "+13105550303"


def make_db(path):
    conn = sqlite3.connect(path)
    conn.executescript(
        """
        CREATE TABLE message (ROWID INTEGER PRIMARY KEY, guid TEXT, date INTEGER,
            is_from_me INTEGER, handle_id INTEGER, text TEXT, attributedBody BLOB,
            associated_message_type INTEGER DEFAULT 0, item_type INTEGER DEFAULT 0);
        CREATE TABLE chat (ROWID INTEGER PRIMARY KEY, chat_identifier TEXT, style INTEGER);
        CREATE TABLE chat_message_join (chat_id INTEGER, message_id INTEGER);
        CREATE TABLE handle (ROWID INTEGER PRIMARY KEY, id TEXT);
        """
    )
    conn.executemany("INSERT INTO handle VALUES (?, ?)", [(1, CLIENT), (2, FRIEND), (3, STRANGER)])
    conn.executemany(
        "INSERT INTO chat VALUES (?, ?, ?)", [(1, CLIENT, 45), (2, FRIEND, 45), (3, STRANGER, 45)]
    )
    rows = [
        (1, "a", NS(NOW - 7200), 1, 0, "Sent the SPQ for signature", 1),
        (2, "b", NS(NOW - 3600), 0, 1, "Signed it — also is the inspection Thursday?", 1),
        (3, "c", NS(NOW - 600), 0, 2, "dinner sunday? 🍝", 2),
        (4, "d", NS(NOW - 300), 0, 3, "who is this", 3),
    ]
    for rowid, guid, date, from_me, handle, text, chat in rows:
        conn.execute(
            "INSERT INTO message (ROWID, guid, date, is_from_me, handle_id, text) VALUES (?,?,?,?,?,?)",
            (rowid, guid, date, from_me, handle, text),
        )
        conn.execute("INSERT INTO chat_message_join VALUES (?, ?)", (chat, rowid))
    conn.commit()
    conn.close()


def write_csv(path):
    path.write_text(f"Category,Name,Contact\nClient,Pat Buyer,{CLIENT}\nPersonal,Sam,{FRIEND}\n")


def run(tmp_path, monkeypatch, csv=True, dry_run=False):
    db = tmp_path / "chat.db"
    make_db(db)
    contacts_csv = tmp_path / "work-contacts.csv"
    if csv:
        write_csv(contacts_csv)
    monkeypatch.setattr(tap.contacts_mod, "name_map", lambda: {CLIENT: "Pat Buyer", FRIEND: "Sam"})
    out = tmp_path / "drive" / "imessage-threads.json"
    argv = ["--chat-db", str(db), "--contacts-csv", str(contacts_csv), "--output", str(out)]
    rc = tap.main(argv + (["--dry-run"] if dry_run else []))
    return rc, out


def test_only_work_threads_are_written_personal_and_unknown_dropped(tmp_path, monkeypatch):
    rc, out = run(tmp_path, monkeypatch)
    assert rc == 0
    snap = json.loads(out.read_text())
    assert [t["contact"] for t in snap["threads"]] == [CLIENT]
    assert snap["personal_threads_skipped"] == 2  # the friend AND the unknown number
    blob = out.read_text()
    for leaked in (FRIEND, STRANGER, "Sam", "dinner", "who is this"):
        assert leaked not in blob


def test_work_thread_shape_and_awaiting_reply(tmp_path, monkeypatch):
    _, out = run(tmp_path, monkeypatch)
    t = json.loads(out.read_text())["threads"][0]
    assert set(t) == {
        "contact", "name", "category", "last_inbound_at", "last_outbound_at",
        "awaiting_reply", "inbound_count", "outbound_count", "recent",
    }
    assert t["name"] == "Pat Buyer" and t["category"] == "Client"
    assert t["awaiting_reply"] is True  # client's question is newer than the last sent text
    assert [m["from_me"] for m in t["recent"]] == [True, False]
    assert "inspection Thursday" in t["recent"][-1]["text"]


def test_missing_csv_writes_nothing_but_a_count(tmp_path, monkeypatch):
    _, out = run(tmp_path, monkeypatch, csv=False)
    snap = json.loads(out.read_text())
    assert snap["work_contacts_csv_found"] is False
    assert snap["threads"] == [] and snap["personal_threads_skipped"] == 3


def test_dry_run_writes_no_file(tmp_path, monkeypatch):
    rc, out = run(tmp_path, monkeypatch, dry_run=True)
    assert rc == 0 and not out.exists()


def test_unavailable_chat_db_keeps_previous_snapshot(tmp_path, monkeypatch):
    out = tmp_path / "imessage-threads.json"
    out.write_text('{"previous": true}')
    rc = tap.main(["--chat-db", str(tmp_path / "missing" / "chat.db"), "--output", str(out)])
    assert rc == 3
    assert json.loads(out.read_text()) == {"previous": True}


def test_snapshot_file_is_private(tmp_path, monkeypatch):
    _, out = run(tmp_path, monkeypatch)
    assert oct(out.stat().st_mode & 0o777) == "0o600"
