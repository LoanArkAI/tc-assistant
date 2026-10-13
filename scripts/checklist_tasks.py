#!/usr/bin/env python3
"""Which checklist items does this deal need? Deterministic, from checklists/<team>.json.

    python3 scripts/checklist_tasks.py --team kase --list
    python3 scripts/checklist_tasks.py --team kase --checklist kase-purchase-includes-sfr-condo \
        --tags side:buy cond:hoa cond:pre1978

Prints JSON: the items to create as tasks (required documents, plus conditional ones whose tag
the deal carries), and the if-applicable items to recognize but not pre-create. Fields are
never returned as tasks. Doing this in code rather than by eye is the point — a skipped
required item is the gap the broker finds at review.
"""
import argparse, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--team", required=True)
    ap.add_argument("--checklist")
    ap.add_argument("--tags", nargs="*", default=[])
    ap.add_argument("--list", action="store_true", help="list checklist ids and titles")
    a = ap.parse_args()
    src = ROOT / "checklists" / f"{a.team}.json"
    if not src.exists():
        sys.exit(f"{src} missing -- import the workbook with scripts/import_checklists.py")
    data = json.loads(src.read_text())
    lists = {c["id"]: c for c in data["checklists"]}
    if a.list or not a.checklist:
        for c in data["checklists"]:
            print(f"{c['id']}\t{c['title']}")
        return
    c = lists.get(a.checklist)
    if not c:
        sys.exit(f"unknown checklist {a.checklist!r}; run with --list")
    tags = set(a.tags)
    tasks, optional = [], []
    for it in c["items"]:
        if it["kind"] != "document":
            continue
        entry = {"name": it["name"], "section": it["section"]}
        if it["required"] or it["when"] in tags:
            tasks.append(entry)
        elif it["when"] == "if-applicable":
            optional.append(entry)
    print(json.dumps({"checklist": c["id"], "title": c["title"], "tags": sorted(tags),
                      "tasks": tasks, "if_applicable": optional}, indent=1))


if __name__ == "__main__":
    main()
