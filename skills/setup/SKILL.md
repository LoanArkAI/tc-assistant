---
name: setup
version: 2.0.0
description: >-
  First-run setup for the TC assistant plugin. Use when the agent or TC (or
  whoever is installing) says "set up the TC assistant plugin", "finish setup", "install my
  schedules", "get me started", or right after installing the plugin. It checks the required
  Claude connectors, confirms the Follow Up Boss key is in place, fills in the team's
  TEAM.md from Follow Up Boss, and registers the three scheduled jobs (daily sweep, inbox
  watch, monthly feedback loop) as cloud routines on the person's claude.ai account, so they
  run even when the computer is off. Run it once per person.
---

# Setup (TC assistant plugin)

Get a new install working: connectors connected, FUB key in place, and the three scheduled
tasks registered on this computer. Scheduled tasks live in each user's own Claude
(`~/.claude/scheduled-tasks/`), so installing the plugin ships the *skills* but not the
*schedules* — this skill creates them here. Run once per person/machine.

## Walk the person through it, in order

### 1. Connect the Claude connectors
Confirm these are connected (Claude connector settings). The skills read from them:
- **Gmail** — deal communication, packets, evidence (required)
- **Google Calendar** — the deadlines calendar named in `../../TEAM.md`
- **Google Drive** — contracts, filed deal docs and the voice-rules file (folder in `TEAM.md`)
- **DocuSign** — envelope completions (evidence)
If any is missing, point them to connector settings and stop until it's connected — the
scheduled tasks can't read what isn't connected.

### 2. Connect Executor + add the FUB key once (Cowork-native)
FUB is reached through the **Executor** MCP, which holds the key in its own vault — the key
never enters Cowork, a prompt, or the dashboard. The plugin's `.mcp.json` already points at the
Executor workspace endpoint. First-run, per person:
1. **Connect Executor** — sign into the Executor workspace when the MCP connects (the plugin
   ships the endpoint; each person authenticates as themselves).
2. **Add the FUB key to Executor once** — in Executor, add/confirm the `follow_up_boss_subset`
   connection: API key header, header `Authorization`, **prefix empty**, value = `Basic <base64>`
   where `<base64>` = base64 of `theFUBkey:` (key + trailing colon, blank password). This is a
   one-time paste into Executor's vault; connections are per-user, so each person does it once.
3. **Verify** — run the `getIdentity` health check (or `search`+`invoke getIdentity`). A 200
   returning the team's FUB account confirms it works.
See `../../references/executor-fub.md` for the call pattern. Never handle the raw key in Cowork.

### 2b. Fill in `TEAM.md` from Follow Up Boss
Every skill reads `../../TEAM.md`. Walk its `[fill-in]` values with the person, pulling what
FUB can answer instead of asking:
- **FUB account name** — from `getIdentity`.
- **Deal stage ids** — from `pipelines.listPipelines` (each pipeline's `stages[]`). Never
  `listStages`.
- **FUB user ids** — from `users.listUsers`, matched to the people in the table.
- **Template prefix** — from `templates.listTemplates`; if the team has no templates yet,
  record "none yet" and `draft-emails` will write from scratch.
- **Compliance checklists** — if the brokerage has a master checklist workbook, import it:
  `python3 ../../scripts/import_checklists.py <workbook> --team <team>`, and fill in the
  checklist-picking table in `TEAM.md` with the ids it prints.
- Everything else (emails, broker, folders, calendar, vendors) — ask. Leave `[fill-in]` on anything the person doesn't know yet rather than guessing.
Show the proposed values and get a yes before saving. Save personal values (emails, phones,
folder names, the broker's name) to `TEAM.private.md` in the agent's TC Assistant folder in
Google Drive — never into the repo, which is public. Only non-personal values (stage ids,
template prefix, checklist choices) may go into `TEAM.md`.

### 2c. Texts — the iMessage tap (Mac only, optional)
If the person works on a Mac and wants texts counted as evidence, follow
`../../mac-tap/README.md`: install python.org Python once, run `mac-tap/install.sh` with the
team's Google Drive folder, grant Full Disk Access. Then fill the allowlist: build
`work-contacts.csv` in that Drive folder from FUB — the people on open deals, plus the escrow
officers, lenders and other-side agents on them — as `Category,Name,Contact` rows (one row per
phone number or email). Show the list before saving. Only these contacts' threads are ever
read; everyone else stays private. Record "installed" in `TEAM.md` → Texts.

### 3. Register the three scheduled tasks as cloud routines
They run in the cloud, on the person's own claude.ai account, so they fire on time whether or
not their computer is on. Each run is a fresh Claude Code on the web session; nothing runs on
the person's machine. Create them **from the person's own account** — a routine reads the
Gmail, Drive and DocuSign of the account it was created on.

Prerequisites on that account (check each; stop with the fix if one is missing):
- **Connectors** at claude.ai/customize/connectors: Gmail, Google Calendar, Google Drive,
  DocuSign — plus **Executor** added as a custom connector (the URL in `.mcp.json`) and signed
  in. A routine can't do an interactive sign-in, so Executor must be a connector, not the
  plugin's `.mcp.json` server.
- **A cloud environment** (claude.ai/code) with this plugin's repository
  (`LoanArkAI/tc-assistant`) attached, so each run has the skills, scripts and checklists.

Create three routines (Claude Code on the web → Routines, or `create_trigger` with
`create_new_session_on_fire: true` and the connectors above when this session has it). Use the
person's time zone in the schedule:

- **TC — Daily Sweep** — `CRON_TZ=<tz> 27 7,16 * * *` (7:27am & 4:27pm).
- **TC — Inbox Watch** — `CRON_TZ=<tz> 13 8-18/2 * * 1-6` (every 2 hours, 8am–6pm, Mon–Sat).
- **TC — Feedback Loop** — `CRON_TZ=<tz> 3 9 1 * *` (9:03am on the 1st of each month).

Each prompt is self-contained, because every run starts from nothing:
```
Scheduled run. Use the <skill> skill in skills/<skill>/SKILL.md of this repository
(read TEAM.md first, then its private settings file in Google Drive).
Run unattended: drafts only, never send; never close a checklist item; never write to
Follow Up Boss except what the skill allows unattended. If a connector is unavailable,
say so in the output instead of guessing. Do not commit or push anything to the repository.
```
(`<skill>` = `daily-sweep`, `inbox-watch`, `feedback-loop`.) Then **run each once now** and
check its output — that run surfaces any missing connector while the person can still fix it.

### 4. What changes in the cloud
- **Run logs:** each cloud session is thrown away after it finishes, so scheduled runs don't
  add lines to `metrics/runs.jsonl`. The digest, drafts and reports themselves are the record.
- **The Pipeline Board** is republished by the daily sweep as before.
- **Texts** still come from the Mac tap's file in Google Drive; the cloud run reads it there.
  When the Mac has been off, the file is older — the skills say "texts as of <time>".

## Done check
Confirm back: which connectors are green, that the FUB key verified, and that all three
routines exist with their next run times and a good first run. List anything still missing.
