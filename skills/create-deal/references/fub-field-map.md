# FUB field map, tags, and the RPA JSON shape

The connective tissue between the contract and Follow Up Boss. All values synthetic.

## FUB access
- Base `https://api.followupboss.com/v1`. HTTP Basic: the FUB API key as username, blank password (held in Executor's vault — never in this repo).
- Account: the one named in `../../../TEAM.md`. The key's FUB user decides what it can see.
- Writes used here: `POST /deals`, `POST /tasks`. Reads: `GET /deals`, `GET /people`, `GET /templates`.
- Never `PUT`/`PATCH`/`DELETE` on an existing deal, person, or task.

## Proven create shapes (live-verified 2026-09-18 on a production FUB account; re-verify once on this one)
**`POST /deals`** — the native date fields post directly on create (no `customFields` wrapper):
```json
{"name":"123 Example St — Buyer (Client Last)","stageId":16,"price":850000,
 "mutualAcceptanceDate":"2026-10-01","dueDiligenceDate":"2026-10-08",
 "customCR1":"2026-10-08","customCR2Date":"2026-10-15","projectedCloseDate":"2026-11-02"}
```
- **`stageId` is required and numeric.** `pipelineName`, `stageName`, and even `pipelineId` are REJECTED ("Invalid fields") — send `stageId` only; the stage implies the pipeline.
- Date fields read back with a `T00:00:00Z` suffix on some (`mutualAcceptanceDate`), plain date on others (`customCR1`) — send plain `YYYY-MM-DD`, both are accepted.

**`POST /tasks`** — tasks attach to a **person, not a deal**:
```json
{"name":"16 AVID — request from both agents","type":"Closing","dueDate":"2026-10-03","personId":12345}
```
- There is **no `dealId` field** — sending it fails ("Invalid fields: dealId"). Resolve/create the contact first and pass `personId`. So the flow is: create/find person → create deal → create tasks on the person.

### Deal stage IDs
Stage ids differ per FUB account. Read them from `pipelines.listPipelines` and record them in
`TEAM.md` → Deal stage ids. Never use `stages.listStages` — those are contact stages.

## Deal date fields (write these; ISO YYYY-MM-DD)
| Field key | Meaning | Source |
|---|---|---|
| `mutualAcceptanceDate` | Day 0 — binding acceptance | RPA `acceptance_date` |
| `dueDiligenceDate` | Investigation removal | RPA `investigation_contingency_removal` |
| `customCR1` | Contingency removal 1 (all except loan/appraisal) | derived (see date-rules) |
| `customCR2Date` | Contingency removal 2 (all remaining) — custom field id 2 | derived |
| `projectedCloseDate` | Close of escrow | RPA `close_of_escrow` |
| `possessionDate` | Possession, if stated | RPA `terms.possession_date` |
| `earnestMoneyDueDate` | EMD (~day 3) | not from contract — leave unless human gives it |
| `finalWalkThroughDate` | Final walkthrough (COE − 3–5d) | derived from COE |

A refused date → leave the field unset. Never write a placeholder.

## RPA JSON export shape (input, optional)
The authoritative contract is the RPA Processor's export spec (`ca-rpa-processor` repo).
```json
{
  "schema_version": "1",
  "acceptance_date": "2026-10-01",
  "deadlines": [
    {"name": "close_of_escrow", "due": "2026-10-31", "days_after_acceptance": 30,
     "basis": "default", "set_by": "RPA 12/25 page 1", "shifted_from": null, "date_confirmed": true}
  ],
  "refusals": [{"name": "loan_contingency_removal", "reason": "could not be read from the contract"}],
  "warnings": ["All periods counted in calendar days..."],
  "terms": {"possession_date": {"value": "...", "set_by": "...", "confidence": 0.0}}
}
```
Engine deadline names: `investigation_contingency_removal`, `loan_contingency_removal`,
`appraisal_contingency_removal`, `common_interest_disclosures`, `close_of_escrow`.

## Conditional tags (from the Q&A, not the contract)
The tag list and what each turns on live in `TEAM.md` → Condition tags. Tags are created on
first application (there is no standalone tag-create endpoint).

## The checklist task set
The team's compliance checklist lives in `TEAM.md` → Compliance checklist. Create a task per
item that survives the tag filter, taskType `Closing`, with the item's due date where one
applies (deadline-linked items) and no due date for "as it arrives" items. If the checklist
is still `[fill-in]`, create only the dated-deadline tasks and say so.

## Email templates (draft, don't send)
Templates carry the prefix in `TEAM.md` (`GET /templates`, filter by prefix). The usual set:
Listing Intro (Sellers), Accepted Offer Intro — Escrow / Lender / Buyer, New Transaction Intro
+ Doc Request — Listing Agent, Warranty Order, Disclosure Package to Buyer, Final Walkthrough
Scheduling, Commission Confirmation, Docs Request / Reminder / Send. If the team hasn't built
them yet, `draft-emails` writes from scratch in the agent's voice.
