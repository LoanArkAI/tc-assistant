# Install & Setup — TC Assistant

One-time setup, per person, on the computer they'll use. Plan ~20 minutes. When it's done, the
agent can say "Create a new deal" (or drop in a contract) and everything downstream works.

> **Who runs what.** Day to day the agent works in **Claude Cowork** — no code, no terminal,
> no Follow Up Boss API key. This is the setup they (or whoever installs for them) walk once.

---

## 1. What you need first

| Dependency | Why | Who provides it |
|---|---|---|
| **Claude** with **Cowork** + connectors | where the agent works and where connectors live | their Claude account |
| **Follow Up Boss** account | the system of record — deals, tasks, contacts, templates | the agent / brokerage FUB admin |
| **A Follow Up Boss API key** | lets the plugin read/write FUB through Executor | FUB → Admin → API |
| **Executor** workspace (executor.sh) | the vault that holds the FUB key so it never enters Cowork | free tier is fine |
| **Google Drive** folder | contracts in, the email-voice-rules file, filed docs | the agent |

## 2. Point the plugin at the team

Before installing, edit two files in this repo and commit:

- **`.mcp.json`** — replace `REPLACE-WITH-WORKSPACE` with the team's Executor workspace, so the
  URL reads `https://executor.sh/<workspace>/mcp`.
- **`TEAM.md`** — fill in what you know now (emails, broker, folders, calendar). The `setup`
  skill pulls the FUB ids for you in step 5, so leave those as `[fill-in]`.

## 3. Install the plugin

Add this repo as a plugin marketplace in the Claude app and install **tc-assistant**. It ships
the nine skills and the Executor endpoint — not the connectors or the schedules (steps 4–6).

## 4. Connect the Claude connectors

| Connector | Required? | Used for |
|---|---|---|
| **Gmail** | **Required** | deal email, leaving drafts, the feedback loop (draft vs. sent) |
| **Google Calendar** | Required | the deadlines calendar named in `TEAM.md` |
| **Google Drive** | Required | contracts folder + the voice-rules file |
| **DocuSign** | Recommended | envelope completions as evidence |

## 5. Connect Executor, add the FUB key, fill in `TEAM.md`

Run the **`setup`** skill ("set up the TC assistant"). It walks through:

1. **Connect Executor** — sign in to the workspace when the `executor` MCP connects.
2. **Add the FUB key once** — in Executor, add the `follow_up_boss_subset` connection from
   `executor/fub-openapi.json` as an **API-key header**: header `Authorization`, **prefix
   empty**, value `Basic <base64 of THE_FUB_KEY:>` (key + a colon, blank password).
3. **Verify** — `getIdentity` returns 200 with the team's FUB account.
4. **Fill in `TEAM.md`** — it reads the account name, deal stage ids, user ids and template
   prefix from FUB, asks for the rest, and shows the changes before saving.

## 6. Scheduled jobs (cloud)

`setup` registers three **cloud routines** on the agent's claude.ai account, so they run
whether or not the computer is on. Before it can: add **Executor** as a custom connector
(claude.ai/customize/connectors, the URL in `.mcp.json`) and sign in, and create a cloud
environment at claude.ai/code with the `LoanArkAI/tc-assistant` repository attached.

| Task | Runs | Does |
|---|---|---|
| **TC — Daily Sweep** | 7:27am & 4:27pm | reconcile files, draft the digest, refresh the Pipeline Board |
| **TC — Inbox Watch** | every 2h, business hours | match new arrivals to deals, surface (never auto-close) |
| **TC — Feedback Loop** | 9am on the 1st | learn the sender's voice from draft-vs-sent |

Setup runs each one once right away so any missing connector shows up while you're there.
Each run is a fresh cloud session, so scheduled runs don't add to `metrics/runs.jsonl`.

## 7. Texts (Mac only, optional)

See [`mac-tap/README.md`](mac-tap/README.md): install python.org Python once, run
`mac-tap/install.sh` with the Drive folder, grant Full Disk Access, then ask Claude to
"set up texts" to build the work-contacts list from Follow Up Boss.

## 8. The Pipeline Board

The first "Refresh the pipeline board" publishes a new private artifact and records its URL
in `TEAM.md`. Share it from the artifact's Share menu with anyone else who should see it.

---

## Checklist

- [ ] `.mcp.json` points at the team's Executor workspace
- [ ] FUB API key issued; plugin **tc-assistant** installed
- [ ] Connectors: Gmail ✱, Google Calendar ✱, Google Drive ✱, DocuSign
- [ ] Executor connected, FUB key in the vault, `getIdentity` returns 200
- [ ] `TEAM.md` has no `[fill-in]` left that the team can answer
- [ ] Brokerage checklists imported (`checklists/<team>.json` exists)
- [ ] Executor added as a custom connector; cloud environment with this repo
- [ ] `setup` run → 3 cloud routines created, each with a good first run

✱ = required.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Executor "Expired" / 401 | Value must be `Basic <base64 of key + ":">`, **prefix empty**, no trailing space |
| A skill keeps asking for a value | It's still `[fill-in]` in `TEAM.md` — fill it in and commit |
| Stage move rejected | Stage ids come from `listPipelines`, not `listStages` |
| Drafts don't sound like the sender | Expected at first — `feedback-loop` learns after a month of sends |
