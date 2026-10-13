# TC Assistant

A transaction-coordination assistant for a real estate agent or team on **Follow Up Boss**. It
turns an accepted contract into a fully set-up FUB deal, drafts the transaction emails, answers
what's still missing on a file, runs the daily sweep and inbox watch, keeps a live pipeline
board, and learns the sender's email voice over time. Additive to FUB, drafts-only outbound,
broker signs off.

**Configured for:** Ernie Aguilar at Kase. Ernie is the agent and does his own TC work, so
"the agent" and "the TC" in the skills are the same person.

- **Team config:** [`TEAM.md`](TEAM.md) — every name, email, FUB id, template prefix, folder,
  calendar, vendor and the compliance checklist. The skills contain none of these; set the
  plugin up for another agent or brokerage by editing `TEAM.md` only. Values still marked
  `[fill-in]` make a skill stop and ask instead of guessing.
- **Setup:** [`INSTALL.md`](INSTALL.md) — connectors, Executor + FUB key, filling in `TEAM.md`,
  scheduled tasks.
- **Working on the skills:** [`docs/skill-ops.md`](docs/skill-ops.md) — how we version,
  measure, audit and tune them.

## Skills

| Skill | What it does |
|---|---|
| `create-deal` | Accepted contract → a fully set-up FUB deal (dates, tags, tasks); also updates an existing deal |
| `dashboard` | Refresh the Pipeline Board artifact from FUB (read-only) |
| `daily-sweep` | Morning/afternoon reconcile + one digest; also refreshes the board |
| `inbox-watch` | Match new arrivals to deals and surface them (never auto-close) |
| `whats-missing` | What's blocking a deadline on one file |
| `draft-emails` | Draft the transaction emails from the team's FUB templates (drafts only); applies learned voice rules |
| `feedback-loop` | Learn the sender's voice from draft-vs-sent; maintain the shared voice-rules file |
| `manage-file` | Move a deal's stage, log a note, set an appointment, reassign, mark a task done (confirm-first) |
| `setup` | First-run: connectors, FUB key, fill in `TEAM.md`, and the three scheduled tasks |

## How Follow Up Boss is reached

Through the **Executor** MCP (`.mcp.json` ships the endpoint — set the team's workspace URL
there), which holds the FUB API key in its own vault — the key never enters Cowork, a prompt,
an artifact, or this repo. See [`references/executor-fub.md`](references/executor-fub.md) and
[`executor/fub-openapi.json`](executor/fub-openapi.json).

## Guardrails

- Additive to FUB — never deletes, and only edits the specific fields a person confirmed.
- Drafts only outbound — every email is left for a human to send.
- The FUB key stays in the Executor vault — never printed, logged, or committed.
- The broker of record (in `TEAM.md`) signs off at the end.

## Working on the skills

The skills are versioned and measured — see [`docs/skill-ops.md`](docs/skill-ops.md):
`version:` in every `SKILL.md`, one skill per behavior-changing commit, tags
`<skill>/v<semver>`, a hypothesis per change in [`CHANGELOG.md`](CHANGELOG.md), and a run
record per invocation via [`scripts/log_run.py`](scripts/log_run.py) (full detail stays local in
`runs/`; a de-identified line lands in [`metrics/runs.jsonl`](metrics/README.md)).
