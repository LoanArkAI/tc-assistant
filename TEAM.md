# Team configuration

Every skill in this plugin reads this file for the people, accounts, IDs and house rules it
needs. Nothing team-specific is written into the skills themselves — to set the plugin up for
a different agent or brokerage, edit this file, not the skills.

Values marked **`[fill-in]`** are not known yet. A skill that needs one of them must stop and
ask the person rather than guess, and should say which line of this file to fill in.

**This copy is configured for:** Ernie Aguilar at Kase.

---

## People and roles

| Role | Who | Email | FUB user id |
|---|---|---|---|
| **Agent** — the person whose book of business this is | Ernie Aguilar | `[fill-in]` | `[fill-in]` |
| **Transaction coordinator** — runs the files, owns drafts and checklists | Ernie Aguilar (does his own TC work) | same as above | same as above |
| **Broker of record** — final compliance sign-off | `[fill-in]` (Kase) | `[fill-in]` | — |

When the agent and the TC are the same person (as here), "send to the TC, cc the agent"
collapses to one recipient — never address the same person twice.

## Brokerage

| Setting | Value |
|---|---|
| Brokerage name | Kase `[fill-in: full legal name]` |
| Brokerage email domain (internal) | `[fill-in]` |
| State / contract forms | California, C.A.R. forms (RPA) `[confirm]` |
| Compliance system (where the broker reviews files) | SkySlope (the checklists below mirror its slots) |
| Brokerage holidays / closures beyond US federal holidays | `[fill-in, or "none"]` |

## Follow Up Boss

| Setting | Value |
|---|---|
| FUB account name (as `getIdentity` returns it) | `[fill-in]` |
| Executor workspace MCP URL (also in `.mcp.json`) | `[fill-in: https://executor.sh/<workspace>/mcp]` |
| Executor connection name for FUB | `follow_up_boss_subset` |
| Email-template prefix in FUB | `[fill-in: e.g. "KASE |"]` — templates not built yet |
| CR2 custom deal field key | `customCR2Date` `[confirm the field exists in this account]` |
| CR1 custom deal field key | `customCR1` `[confirm]` |

**Deal stage ids** — read them from `pipelines.listPipelines` once and record them here.
(Never from `listStages`; those are contact stages.)

| Pipeline | Stage | stageId |
|---|---|---|
| Buyers | In Escrow | `[fill-in]` |
| Buyers | Closed | `[fill-in]` |
| Buyers | Canceled | `[fill-in]` |
| Sellers | Pre-listing / Coming Soon | `[fill-in]` |
| Sellers | Active (on MLS) | `[fill-in]` |
| Sellers | In Escrow | `[fill-in]` |
| Sellers | Closed | `[fill-in]` |

"Transaction stages" for sweeps and the board = every stage above except Closed and Canceled.

## Files, calendar, voice

| Setting | Value |
|---|---|
| File storage (where contracts and filed deal docs live) | **Google Drive** |
| Drive folder for contracts and filed deal docs (one subfolder per deal) | `[fill-in]` |
| Email voice-rules file (written by `feedback-loop`) | `<that folder>/email-voice-rules.md` |
| Deadlines calendar (a dedicated Google calendar, NOT the primary — FUB two-way-syncs the primary) | `[fill-in: e.g. "Escrow Deadlines"]` |
| Pipeline Board artifact URL (set on first `dashboard` run) | `[fill-in]` |

## Texts (Mac iMessage tap)

| Setting | Value |
|---|---|
| iMessage tap installed? | `[fill-in: yes once mac-tap/install.sh has run on Ernie's Mac]` |
| Snapshot file | `<Drive folder>/imessage-threads.json` (see `references/imessage-tap.md`) |
| Work-contacts allowlist | `<Drive folder>/work-contacts.csv` — only these threads are ever read |

## Vendors and house rules

| Setting | Value |
|---|---|
| Preferred / affiliated escrow company (if it changes the checklist) | `[fill-in, or "none"]` |
| Home-warranty ordering contact (for buyer-paid warranties) | `[fill-in]` |
| Default contingency periods (when the contract relies on the printed default) | Loan 14 · Appraisal 14 · Investigation 7 days `[confirm]` |
| Group contingency removals as CR1 (all but loan/appraisal) + CR2 (loan + appraisal)? | no — Kase's purchase checklist files one CR per contingency (Inspection, Appraisal, Loan) or a single "Removal of ALL Contingencies"; record each removal date separately `[confirm]` |

## Compliance checklists

Kase's master checklists — 18 of them, one per transaction type — are imported from
`MASTER_CHECKLISTS.xlsx` (kept by Ernie, not in this public repo) into [`checklists/kase.json`](checklists/kase.json) (what the
skills read) and [`checklists/kase.md`](checklists/kase.md) (for people). To update them,
edit the workbook and re-run `python3 scripts/import_checklists.py <workbook> --team kase`;
never hand-edit the JSON.

**Picking the checklist for a deal** — by side and property type, at intake. Record it on the
FUB contact as the tag `checklist:<id>`; every later skill reads that tag.

| Property type | Listing side | Buyer / tenant side |
|---|---|---|
| Residential (SFR / condo) | `kase-listing-includes-sfr-condo` | `kase-purchase-includes-sfr-condo` |
| Vacant land | `kase-vacant-land-listing` | `kase-vacant-land-purchase` |
| Mobile / manufactured home | `kase-mobile-home-listing` | `kase-mobile-home-purchase` |
| New construction | `kase-new-construction-listing` | `kase-new-construction-purchase` |
| New construction — buyer referral only | — | `kase-new-construction-buyer-referral` |
| Commercial | `kase-commercial-list` | `kase-commercial-purchase` |
| Commercial & residential income (5+ units) | `kase-commercial-residential-income-listing-5-units` | `kase-commercial-residential-income-purchase-5-units` |
| Residential lease | `kase-lease-listing` | `kase-lease-tenant` |
| Commercial lease | `kase-commercial-lease-listing` | `kase-commercial-lease-tenant` |
| Outgoing referral | — | `kase-referral` |

**What each item means**
- `required: true` — always needed on that checklist; create a task for it.
- `when: "cond:…"` / `"side:…"` — conditional (`*` on the sheet); needed only when the deal
  carries that tag (table below). Create its task only then.
- `when: "if-applicable"` — conditional with no intake question (addenda, extra inspections,
  rejected offers, miscellaneous). Never pre-created; recognized and filed when it shows up.
- `kind: "field"` — a SkySlope field (Broker Notes, "TC for file"), not a document. Never
  chased, never a task.

## Document naming convention

Name every document exactly as its checklist item — the SkySlope slot name — with the
asterisk removed, e.g. `TDS - Transfer Disclosure Statement`, `CR - Inspection`,
`AVID - Listing Agent Visual Inspection Disclosure`. Numbered slots keep their number
(`ADM - Addendum #2`). Use the same name for the file, the FUB task, and every mention in a
digest or report, so a document can be matched to its slot by name alone.
No property address or other prefix — the file name is the slot name alone, plus the file
extension (`TDS - Transfer Disclosure Statement.pdf`). The deal is identified by the folder or
SkySlope transaction the file sits in, never by its name.

### Condition tags (from the intake Q&A)

| Ask at intake | Tag | Turns on (examples) |
|---|---|---|
| Which side? | `side:buy` / `side:list` | BRBC on buyer-side checklists |
| HOA? | `cond:hoa` | BHAA, HOA Receipt from Escrow |
| Condo? | `cond:condo` | PSD - Parking & Storage Disclosure |
| Built before 1978? | `cond:pre1978` | LPD |
| Built before 1960? | `cond:pre1960` | Residential Earthquake Hazard Report |
| Solar? | `cond:solar` | SOLAR - Solar Questionnaire |
| High fire zone (per NHD)? | `cond:firezone` | FHDS |
| Trust, LLC, corp or POA on either side? | `cond:trust` | TA, Trust / Cert of Trust, Entity Docs, RCSD |
| Probate? | `cond:probate` | PA-PA, PA - Probate Advisory |
| Buyer must sell first? | `cond:contingent-sale` | COP |
| FHA / VA loan? | `cond:fha-va` | FVAC, HID |
| TIC or stock co-op? | `cond:tic` / `cond:coop` | TIC-PA / TIC-OA / TIC-FD, COOP-PA / COOP-OA |
| Seller exempt from TDS? | `cond:esd` | ESD, WHSD |
| Another agent or broker on our side? | `cond:team` | AAA, ABA |
| Commission under 2%? | `cond:low-commission` | APPROVAL of LESS THAN 2% commission |
| Referral fee paid or owed? | `cond:referral` | RFA, W-9 for Other Broker |
| Counter offers? | `cond:counter` | SCO, BCO, SMCO |
| City of LA? | `cond:la-city` | 9a Report, COC |
| Seller staying after close? | `cond:seller-in-possession` | SIP, SIPA, RLAS |
| Tenant-occupied? | `cond:tenant-occupied` | TOPA |
| Seller buying a replacement? | `cond:replacement-property` | SPRP |
| Buyer waiving inspection? | `cond:inspection-waived` | BIW |
| Coming-soon / off-internet listing? | `cond:coming-soon` / `cond:off-internet` | Coming Soon Form, SELI |
| File canceled? | `cond:canceled` | COL, CC, CLR — added when it happens, not at intake |
