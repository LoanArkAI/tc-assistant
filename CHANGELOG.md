# Changelog

One entry per skill version, stating the **hypothesis** — what the change should do to the
numbers in `metrics/runs.jsonl`. See [`docs/skill-ops.md`](docs/skill-ops.md).
Skills are tagged `<skill>/v<semver>`; the plugin version in `.claude-plugin/plugin.json`
moves independently.

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
