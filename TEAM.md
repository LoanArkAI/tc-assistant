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
| Compliance system (where the broker reviews files) | `[fill-in: e.g. SkySlope, Dotloop, Lone Wolf]` |
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
| Dropbox (or Drive) folder for contracts and filed deal docs | `[fill-in]` |
| Email voice-rules file (written by `feedback-loop`) | `<that folder>/email-voice-rules.md` |
| Deadlines calendar (a dedicated Google calendar, NOT the primary — FUB two-way-syncs the primary) | `[fill-in: e.g. "Escrow Deadlines"]` |
| Pipeline Board artifact URL (set on first `dashboard` run) | `[fill-in]` |

## Vendors and house rules

| Setting | Value |
|---|---|
| Preferred / affiliated escrow company (if it changes the checklist) | `[fill-in, or "none"]` |
| Home-warranty ordering contact (for buyer-paid warranties) | `[fill-in]` |
| Default contingency periods (when the contract relies on the printed default) | Loan 14 · Appraisal 14 · Investigation 7 days `[confirm]` |
| Group contingency removals as CR1 (all but loan/appraisal) + CR2 (loan + appraisal)? | yes `[confirm]` |

## Compliance checklist

The list of items a file must contain before the broker signs off, with which side it applies
to, who supplies it, and what closes it. `create-deal` creates a task per applicable item;
`whats-missing` and `daily-sweep` reconcile against it.

`[fill-in: paste Kase's checklist here, one item per line — "number · name · side (buy/list/both) · condition tag if any · due (deadline or 'as it arrives')"]`

Until it is filled in, skills work from the deal dates and FUB tasks only and say plainly
that the checklist isn't configured.

### Condition tags (from the intake Q&A)

These are generic California conditions; map each to the checklist items it turns on once
the checklist is in.

| Answer | Tag | Typically turns on |
|---|---|---|
| Buyer side | `side:buy` | buyer-side items |
| Listing side | `side:list` | listing-side items |
| HOA | `cond:hoa` | HOA addendum / docs |
| Built before 1978 | `cond:pre1978` | lead-based paint disclosure |
| Built before 1960 | `cond:pre1960` | earthquake booklet / report |
| Solar | `cond:solar` | solar addendum |
| High fire zone | `cond:firezone` | wildfire disclosures |
| Trust / LLC / POA seller or buyer | `cond:trust` | trust / entity docs |
| Buyer must sell first | `cond:contingent-sale` | contingency-for-sale addendum |
| Buyer-paid home warranty | `cond:warranty` | warranty order task |
| Affiliated escrow (if configured above) | `cond:affiliated-escrow` | affiliated-business disclosure |
