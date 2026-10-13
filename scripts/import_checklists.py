#!/usr/bin/env python3
"""Import a brokerage's master checklist workbook into checklists/<team>.json + .md.

The workbook is the brokerage's compliance checklists, one sheet per transaction type
(listing / purchase / lease / ...), as exported from or mirrored on the compliance system
(e.g. SkySlope). Each item row is:  item name | section | optional help notes.
Section header rows have no section column. A trailing or embedded "*" marks an item as
conditional ("only if applicable").

The item names are also the team's document naming convention: a filed document is named
exactly as its checklist slot (asterisks removed).

    python3 scripts/import_checklists.py MASTER_CHECKLISTS.xlsx --team kase

Writes checklists/<team>.json (what the skills read) and checklists/<team>.md (for people).
Re-run after the brokerage changes a checklist; review the diff before committing.
"""
import argparse, json, pathlib, re, sys
from datetime import date

try:
    import openpyxl
except ImportError:
    sys.exit("needs openpyxl: pip install openpyxl")

ROOT = pathlib.Path(__file__).resolve().parent.parent

SECTIONS = {
    "listing documentation": "Listing Documentation",
    "sales documentation": "Sales Documentation",
    "sales documenation": "Sales Documentation",
    "disclosures": "Disclosures",
    "disclosure documentation": "Disclosures",
    "reports": "Reports",
    "closing documents": "Closing Documents",
}
HEADER_ROWS = {"disclosure documentation", "disclosures", "reports", "closing documents",
               "sales documentation"}

# Conditional item -> the intake tag that turns it on. First match wins. Conditional items
# matching nothing are "if-applicable": never pre-created as tasks, but recognized on arrival.
CONDITIONS = [
    (r"^BHAA\b|HOA Receipt|HOA Document", "cond:hoa"),
    (r"^PSD\b", "cond:condo"),
    (r"^LPD\b", "cond:pre1978"),
    (r"Earthquake", "cond:pre1960"),
    (r"^SOLAR\b", "cond:solar"),
    (r"^FHDS\b", "cond:firezone"),
    (r"^TA - |^Trust, |^RCSD|^Entity Docs", "cond:trust"),
    (r"^COP\b", "cond:contingent-sale"),
    (r"^PA-PA\b|^PA- |Probate", "cond:probate"),
    (r"^FVAC\b|^HID\b", "cond:fha-va"),
    (r"^TIC-", "cond:tic"),
    (r"^COOP-", "cond:coop"),
    (r"^ESD\b|^WHSD\b", "cond:esd"),
    (r"^AAA\b|^ABA\b", "cond:team"),
    (r"LESS THAN 2%", "cond:low-commission"),
    (r"^RFA\b|^RFR - Referral|Referral (Fee )?Agreement|^W-9", "cond:referral"),
    (r"^SCO\b|^BCO\b|^SMCO\b", "cond:counter"),
    (r"^9a\b|^COC\b", "cond:la-city"),
    (r"^RLAS\b|^SIP\b|^SIPA\b", "cond:seller-in-possession"),
    (r"^TOPA\b", "cond:tenant-occupied"),
    (r"^SPRP\b", "cond:replacement-property"),
    (r"^BIW\b", "cond:inspection-waived"),
    (r"Coming Soon", "cond:coming-soon"),
    (r"^SELI\b", "cond:off-internet"),
    (r"^COL\b|^CC - |^CLR\b|^Cancellation", "cond:canceled"),
    (r"^BRBC\b", "side:buy"),
]


def clean(v):
    return re.sub(r"\s+", " ", str(v)).strip() if v not in (None, "") else ""


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def parse_sheet(ws):
    rows = [[clean(c) for c in r] for r in ws.iter_rows(values_only=True)]
    rows = [r for r in rows if any(r)]
    if not rows:
        return None
    title = rows[0][0]
    if title.upper() in ("TASK", "Π") and len(rows) > 1:
        title = rows[1][0]
    title = re.sub(r"\s*-\s*DONE$", "", title, flags=re.I).strip()
    items, seen, section = [], set(), None
    for r in rows:
        a, b = r[0], (r[1] if len(r) > 1 else "")
        notes = " · ".join(x for x in r[2:] if x and x.upper() != "DONE")
        if not a or a.upper() in ("TASK", "Π") or a == title or b.upper() == "DONE" and a.lower() in SECTIONS:
            continue
        if re.sub(r"\s*-\s*DONE$", "", a, flags=re.I).strip() == title:
            continue
        sec = SECTIONS.get(b.lower())
        if not sec:
            if a.lower() in HEADER_ROWS:
                section = SECTIONS.get(a.lower(), a.title())
                continue
            sec = section or "Closing Documents"
        section = sec
        conditional = "*" in a
        name = re.sub(r"\s*\*\s*", " ", a).strip()
        name = re.sub(r"\s+", " ", name)
        if name.lower() in seen:
            continue
        seen.add(name.lower())
        kind = "field" if re.match(r"(?i)^(broker notes|tc for file)", name) else "document"
        m = re.match(r"^([A-Z0-9][A-Za-z0-9&/]*(?:-[A-Z0-9]+)*)\s*-\s*\S", name)
        code = m.group(1) if m and m.group(1).isupper() and len(m.group(1)) <= 8 else None
        when = None
        if conditional:
            when = next((tag for pat, tag in CONDITIONS if re.search(pat, name, re.I)), "if-applicable")
        items.append({"name": name, "code": code, "section": sec, "kind": kind,
                      "required": not conditional, "when": when, "notes": notes or None})
    return {"id": slugify(title), "title": title, "sheet": ws.title, "items": items}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("workbook")
    ap.add_argument("--team", required=True, help="short name, e.g. kase")
    a = ap.parse_args()
    wb = openpyxl.load_workbook(a.workbook, data_only=True)
    lists = [c for c in (parse_sheet(ws) for ws in wb.worksheets) if c and c["items"]]
    out = ROOT / "checklists"
    out.mkdir(exist_ok=True)
    data = {"team": a.team, "imported": date.today().isoformat(),
            "source": pathlib.Path(a.workbook).name, "checklists": lists}
    (out / f"{a.team}.json").write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")

    md = [f"# {a.team.title()} checklists",
          "",
          f"Imported {data['imported']} from `{data['source']}` by `scripts/import_checklists.py` — "
          "edit the workbook and re-import rather than editing this file.",
          "",
          "**Naming convention:** a filed document is named exactly as its checklist item below.",
          "",
          "Legend: **req** = always required · `cond:…` = required when the deal carries that tag · "
          "*if applicable* = only if the document exists for this deal · *field* = a compliance-system "
          "field, not a document.",
          ""]
    for c in lists:
        md += [f"## {c['title']}", f"`{c['id']}` · {len(c['items'])} items", ""]
        sec = None
        for it in c["items"]:
            if it["section"] != sec:
                sec = it["section"]
                if md[-1] != "":
                    md.append("")
                md += [f"**{sec}**", ""]
            tag = ("*field*" if it["kind"] == "field" else "req" if it["required"]
                   else "*if applicable*" if it["when"] == "if-applicable" else f"`{it['when']}`")
            note = f" — {it['notes']}" if it["notes"] else ""
            md.append(f"- {it['name']} · {tag}{note}")
        md.append("")
    (out / f"{a.team}.md").write_text("\n".join(md))
    n = sum(len(c["items"]) for c in lists)
    print(f"{len(lists)} checklists, {n} items -> checklists/{a.team}.json, checklists/{a.team}.md")


if __name__ == "__main__":
    main()
