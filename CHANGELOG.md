# Changelog

One entry per skill version, stating the **hypothesis** — what the change should do to the
numbers in `metrics/runs.jsonl`. See [`docs/skill-ops.md`](docs/skill-ops.md).
Skills are tagged `<skill>/v<semver>`; the plugin version in `.claude-plugin/plugin.json`
moves independently.

---

## plugin 0.4.0 — 2026-10-13

### setup 2.0.0 (MAJOR — the scheduled jobs move from local tasks to cloud routines)
**Hypothesis:** the daily sweep, inbox watch and feedback loop only fired while the Claude app
was open on the agent's computer, so a closed laptop meant an unwatched inbox. Running them as
cloud routines on the agent's own claude.ai account should make every scheduled run fire on time.
**Changed:** setup creates three cloud routines (fresh session per run, the agent's Gmail /
Calendar / Drive / DocuSign / Executor connectors, an environment with this repo) and runs each
once. Executor must be a custom connector, since a routine can't sign in interactively.
Personal settings move to `TEAM.private.md` in the agent's Drive folder, because the repo is
public and cloud runs read `TEAM.md` from it.
**Watch:** first-run failures from a missing connector; scheduled runs no longer reach
`metrics/runs.jsonl` (cloud sessions are discarded).

---

## plugin 0.3.2 — 2026-10-13

### create-deal 1.3.0 (MINOR — it stops writing the CR1/CR2 fields for teams that don't group removals)
Final review fixes. Step 5 no longer tells the skill to write `customCR1`/`customCR2Date`
when `TEAM.md` says removals aren't grouped (Kase): per-contingency removal dates go on the
`CR - Inspection` / `CR - Appraisal` / `CR - Loan` / `CR - Removal of ALL Contingencies` tasks,
with the mapping spelled out. `fub-field-map.md` no longer forbids the field-scoped updates the
skill's update path allows.

---

## plugin 0.3.1 — 2026-10-13

### create-deal 1.2.0
**Hypothesis:** contracts reach the agent in Google Drive, but create-deal only took a PDF
dropped into chat, so the board's "Review new contracts (Drive)" command had nothing behind it.
Reading contracts from the Drive contracts folder — one at a time or as a sweep for contracts
with no FUB deal — should cut files opened late because the contract sat unnoticed.
**Changed:** step 1b (sweep the Drive contracts folder), route (b) reads from Drive; `TEAM.md`
splits the contracts inbox folder from the filed-docs folder. Also adds
`scripts/build_audit_section.py`, which renders the checklists + setup section for the agent's
loanark.com AI audit page.
**Watch:** contracts skipped as not fully executed (false skips are the failure).

---

## plugin 0.3.0 — 2026-10-13

### mac-tap 1.0.0 · whats-missing, daily-sweep, inbox-watch 1.2.0 · setup 1.1.0
**Hypothesis:** much of a transaction moves by text, and every report said "texts aren't
visible". A read-only iMessage tap that writes work-contact threads to Drive should cut the
`items_missing` that turn out to have been handled by text, and surface clients waiting on a
reply the same day.
**Changed:** `mac-tap/` (adapted from the EA tap: same read-only chat.db reader, but local file
output, no network, and personal threads dropped entirely), `references/imessage-tap.md`,
`TEAM.md` → Texts; the three evidence skills read the snapshot and report its age; setup builds
the work-contacts allowlist from FUB.
**Watch:** snapshot age at read time (how often the Mac is asleep), and any deal contact
missing from the allowlist.

---

## plugin 0.2.0 — 2026-10-13

### create-deal, whats-missing, inbox-watch, daily-sweep 1.1.0 · setup 1.0.1
**Hypothesis:** the skills were reconciling against an empty checklist, so "what's missing"
could only see dates. Importing Kase's 18 master checklists and choosing one per deal at
intake should make every file's task list match what the broker reviews in SkySlope, and
naming tasks and documents by the slot name should let arrivals match items by name.
**Changed:** `scripts/import_checklists.py` (workbook → `checklists/kase.json` + `.md`),
`scripts/checklist_tasks.py` (checklist + tags → tasks, deterministic), `TEAM.md` checklist
picker, condition tags and naming convention; the four skills read the deal's
`checklist:<id>` tag. Conditional (`*`) items with an intake question become tagged tasks;
the rest are recognized on arrival but never pre-created.
**Watch:** `items_missing` that turn out to be filed already (a naming mismatch), and any
broker-review gap on an item the checklist marked if-applicable.

---

## plugin 0.1.0 — 2026-10-13

### all skills 1.0.0 — baseline
Forked from a production TC plugin for a single brokerage and made team-agnostic: every
person, FUB id, template prefix, folder, calendar, vendor and the compliance checklist moved
into `TEAM.md`, and the skills read it instead of carrying their own. First configuration:
Ernie Aguilar at Kase, where the agent does his own TC work.

**Hypothesis:** behavior matches the source plugin wherever `TEAM.md` is filled in. Where a
value is still `[fill-in]`, a skill stops and asks instead of guessing — so early runs will
show more `blocked` outcomes, falling to near zero once `setup` has filled the file.
**Watch:** `blocked` outcomes by skill until `TEAM.md` is complete; then `human_edits` on
`draft-emails`, which starts without templates or voice rules for this sender.

**Not carried over:** the source team's email templates, compliance checklist, pipeline board
data and HTML guides. The board shell here is de-branded with demo data until the first
`dashboard` run.
