---
name: setup
version: 1.0.0
description: >-
  First-run setup for the TC assistant plugin. Use when the agent or TC (or
  whoever is installing) says "set up the TC assistant plugin", "finish setup", "install my
  schedules", "get me started", or right after installing the plugin. It checks the required
  Claude connectors, confirms the Follow Up Boss key is in place, fills in the team's
  TEAM.md from Follow Up Boss, and registers the three
  scheduled tasks (daily sweep, inbox watch, monthly feedback loop) on THIS machine — because scheduled tasks are
  per-machine and don't travel inside a plugin. Run it once per person/computer.
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
- **Dropbox** (or Drive) — the team's forms + filed deal docs, folder in `TEAM.md`
- **DocuSign** — envelope completions (evidence)
- **Google Drive** — filed working docs
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
- Everything else (emails, broker, folders, calendar, vendors, the compliance checklist) —
  ask. Leave `[fill-in]` on anything the person doesn't know yet rather than guessing.
Show the proposed changes to `TEAM.md` and get a yes before saving. In Cowork, where the
plugin folder can't be edited, give the person the finished file to commit to the plugin's
repo, and note that skills will keep asking for those values until it's in.

### 3. Register the three scheduled tasks (on this machine)
Create all three as local scheduled tasks. Use the exact prompts the plugin ships — they are
self-contained and carry the guardrails (unattended-safe, drafts-only, read-only on
compliance). The three tasks:

- **TC — Daily Sweep** — cron `27 7,16 * * *` (7:27am & 4:27pm). Prompt: run the
  `daily-sweep` skill; reconcile active deals vs Gmail/DocuSign/Dropbox/Drive; draft one
  digest to the TC (cc the agent if a different person). (The sweep also refreshes the Pipeline Board at the end of its run.)
- **TC — Inbox Watch** — cron `13 8-18/2 * * *` (every 2h, business hours). Prompt: run
  the `inbox-watch` skill; match recent arrivals to deals; surface (never auto-close).
- **TC — Feedback Loop** — cron `0 9 1 * *` (9:00am on the 1st of each month). Prompt: run
  the `feedback-loop` skill; compare the drafts this plugin created against what was actually
  sent, extract the repeatable edits as voice rules, update the voice-rules file named
  in `TEAM.md`, and prune to 15. Read-only on the mailbox; writes only that one file.

Pull the full prompt text from each skill's SKILL.md so the scheduled copy stays in sync
with the skills. After creating them, tell the person to click **Run now** once on each
(Scheduled sidebar) to pre-approve the connector/FUB tool prompts, so future runs don't
pause.

### 4. Explain the one limitation
These are local scheduled tasks: **the Claude app must be open for them to fire** (a missed
window runs at next launch). That's the trade for using the Claude connectors directly. If
they need true always-on later, that's a separate infrastructure conversation.

## Done check
Confirm back: which connectors are green, that the FUB key verified, and that all three
scheduled tasks show in the Scheduled sidebar with their next run times. List anything still missing.
