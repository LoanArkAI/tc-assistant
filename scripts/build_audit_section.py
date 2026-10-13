#!/usr/bin/env python3
"""Render the "Your TC Assistant" section for the agent's loanark.com AI audit page.

    python3 scripts/build_audit_section.py checklists/kase.json docs/audit-section.html

The section (checklists + setup steps) is spliced into the audit report between
<!-- tc-assistant:start --> and <!-- tc-assistant:end --> markers, so it can be
replaced or removed without touching the rest of the report.
"""
import json, html, sys
d = json.load(open(sys.argv[1]))
COND = {
 "side:buy":"Buyer side","cond:hoa":"HOA","cond:condo":"Condo","cond:pre1978":"Built before 1978",
 "cond:pre1960":"Built before 1960","cond:solar":"Solar","cond:firezone":"High fire zone",
 "cond:trust":"Trust, LLC, corp or POA","cond:probate":"Probate","cond:contingent-sale":"Buyer must sell first",
 "cond:fha-va":"FHA / VA loan","cond:tic":"Tenancy in common","cond:coop":"Stock co-op",
 "cond:esd":"Seller exempt from TDS","cond:team":"Another agent or broker on our side",
 "cond:low-commission":"Commission under 2%","cond:referral":"Referral fee","cond:counter":"Counter offers",
 "cond:la-city":"City of LA","cond:seller-in-possession":"Seller stays after close",
 "cond:tenant-occupied":"Tenant-occupied","cond:replacement-property":"Seller buying a replacement",
 "cond:inspection-waived":"Buyer waives inspection","cond:coming-soon":"Coming-soon listing",
 "cond:off-internet":"Off-internet listing","cond:canceled":"File canceled",
}
e = html.escape
def label(it):
    if it["kind"] == "field": return '<td class=f>'
    if it["required"]: return '<td class=r>'
    if it["when"] == "if-applicable": return '<td class=o>'
    return f'<td class=c>{e(COND.get(it["when"], it["when"]))}'
out = ['<!-- tc-assistant:start -->', '<section id="tc-assistant">', '''<style>
#tc-assistant details{border:1px solid var(--line);border-radius:6px;margin:0 0 10px;background:var(--ground)}
#tc-assistant summary{cursor:pointer;padding:12px 16px;font-weight:600;color:var(--ink);display:flex;justify-content:space-between;gap:12px}
#tc-assistant summary span{color:var(--ink-3);font-weight:400;font-size:.85rem;white-space:nowrap}
#tc-assistant table{width:100%;border-collapse:collapse;font-size:.88rem}
#tc-assistant th{text-align:left;font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3);font-weight:600;padding:8px 16px;background:var(--surface)}
#tc-assistant td{padding:7px 16px;border-top:1px solid var(--line);vertical-align:top}
#tc-assistant td.s{background:var(--surface);font-weight:600;color:var(--navy);font-size:.8rem}
#tc-assistant td small{color:var(--ink-3);font-size:.8rem;display:block}
#tc-assistant td.r,#tc-assistant td.c,#tc-assistant td.o,#tc-assistant td.f{font-size:0}
#tc-assistant td.r:before,#tc-assistant td.c:before,#tc-assistant td.o:before,#tc-assistant td.f:before{display:inline-block;font-size:.72rem;font-weight:600;padding:2px 8px;border-radius:99px}
#tc-assistant td.r:before{content:"Required";background:var(--good-soft);color:var(--good)}
#tc-assistant td.o:before{content:"If applicable";background:var(--surface);color:var(--ink-2);border:1px solid var(--line)}
#tc-assistant td.f:before{content:"SkySlope field";background:var(--warn-soft);color:var(--warn)}
#tc-assistant td.c{font-size:.72rem;font-weight:600;color:var(--sky)}
#tc-assistant td.c:before{content:"If\\00a0";font-size:.72rem;padding:0;background:none}
#tc-assistant ol.tc-steps li{margin:0 0 .5rem;max-width:70ch}
#tc-assistant code{font-size:.85em;background:var(--surface);padding:1px 5px;border-radius:4px}
@media (max-width:640px){#tc-assistant th:last-child,#tc-assistant td:last-child{width:40%}}
</style>''',
 '<p class="eyebrow">Your TC Assistant</p>',
 '<h2>Your transaction checklists and setup</h2>',
 '<p class="lede">Your Claude TC Assistant is set up for Kase. Every file it opens follows the Kase checklist for that transaction type, '
 'and every document is named exactly as its checklist item &mdash; the SkySlope slot name, with no property address.</p>',
 '<h3>Setting it up</h3><ol class="tc-steps">',
 '<li><b>Download and install the plugin.</b> <a href="https://loanark.com/downloads/tc-assistant.zip" target="_blank" rel="noopener"><b>Download the TC Assistant</b></a> (tc-assistant.zip). '
 'Then in Claude (desktop app or claude.ai): Customize &rarr; Plugins &rarr; Add &rarr; Upload plugin, and choose that file.</li>',
 '<li><b>Connect your accounts</b> in Claude: Gmail, Google Calendar, Google Drive and DocuSign.</li>',
 '<li><b>Run setup.</b> Tell Claude &ldquo;set up the TC assistant&rdquo;. It connects Follow Up Boss and asks for anything it still needs.</li>',
 '<li><b>Texts (optional, on your Mac).</b> Unzip the same tc-assistant.zip, '
 'run <code>mac-tap/install.sh</code> with your TC Assistant folder in Google Drive, allow Full Disk Access for Python, then tell Claude &ldquo;set up texts&rdquo;. '
 'It only reads texts with the work contacts Claude lists from your deals, and it never sends a message.</li>',
 '</ol>',
 f'<h3>Kase checklists</h3><p>All {len(d["checklists"])} checklists, imported from the Kase master checklist workbook. '
 'Claude picks the one that matches the side and property type when it opens a file.</p>']
for c in d["checklists"]:
    docs = [i for i in c["items"] if i["kind"] == "document"]
    req = sum(1 for i in docs if i["required"])
    out.append(f'<details><summary>{e(c["title"])}<span>{req} required &middot; {len(docs)} documents</span></summary>')
    out.append('<table><tr><th>Document name<th>When it&rsquo;s needed')
    sec = None
    for it in c["items"]:
        if it["section"] != sec:
            sec = it["section"]
            out.append(f'<tr><td class=s colspan=2>{e(sec)}')
        n = (it.get("notes") or "").strip()
        if n.replace("*", "").strip().lower() == it["name"].lower():
            n = ""
        note = f'<small>{e(n)}</small>' if n else ""
        out.append(f'<tr><td>{e(it["name"])}{note}{label(it)}')
    out.append('</table></details>')
out += ['</section>', '<!-- tc-assistant:end -->']
s = "\n".join(out)
assert "$tcsec$" not in s
open(sys.argv[2], "w").write(s)
print(len(s))
