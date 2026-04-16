# Research State

`research/` is the durable state layer for the repo-level research OS.
Keep important intermediate reasoning here, not only in chat.

## Operating Model

Default loop: `plan -> gather evidence -> implement / run -> verify -> log -> synthesize`.

1. Start from `research/research_plan.md` when a topic is active.
2. If the topic is new, instantiate it from `research/research_plan.template.md`.
3. Use `templates/sprint_contract.md` for any bounded execution chunk that needs explicit acceptance checks.
4. After substantive code or experiment changes, append a traceable entry to `research/findings.md`.
5. If scope, methods, or standards change, record the decision in `research/decision_log.md`.
6. Keep claims in `research/claims_registry.md`, not only in prose drafts or chat.
7. Keep file paths repo-relative.

## File Roles

| File | Role | Update Style | When To Touch |
|---|---|---|---|
| `research_plan.md` | live plan for the active topic | edit in place | when a topic is active |
| `research_plan.template.md` | reusable topic plan template | copy, then adapt | when starting a new topic |
| `findings.md` | append-only evidence log | append | after substantive work or verification |
| `literature_map.md` | source inventory and evidence map | edit in place | when sources are added or reclassified |
| `claims_registry.md` | claim-level status and support pointers | edit in place | when a claim changes status or support |
| `decision_log.md` | decisions, alternatives, and rationale | append | when method, scope, or standards shift |
| `open_questions.md` | blockers and unresolved evidence gaps | edit in place | when a question blocks progress |
| `paper_queue.csv` | paper or source triage queue | edit status rows | when batching source work |
| `experiment_queue.csv` | experiment execution queue | edit status rows | when batching experimental work |
| `reviews/repro_checklist.md` | reproducibility gate before sharing | edit in place | before release or external sharing |
| `library/index.md` | root research library index | edit in place | when papers are added or retired |
| `templates/sprint_contract.md` | execution contract for one sprint or batch | copy, then adapt | before a bounded implementation round |

## Working Rules

- Non-trivial work starts with a plan file, not with implementation.
- Every substantive experiment or code change must leave a trail in `findings.md`.
- Every research claim must be traceable to a source, run artifact, or file path.
- Use `verified`, `uncertain`, or `rejected` consistently in the claim registry.
- Never leave a final conclusion only in chat.
- Separate observation from interpretation whenever possible.
- Favor small, reviewable batches over large unstructured tasks.
- Store user-added papers under `research/library/<slug>/` with a note file and local artifact path when the paper is meant for the generic root research library rather than the textbook child project.

## Resume Sequence

1. Read `AGENTS.md` and this file.
2. Read `research/research_plan.md` if it exists; otherwise instantiate it from the template.
3. Read `findings.md`, `claims_registry.md`, `open_questions.md`, and `decision_log.md`.
4. If the work is being resumed after a pause, use the latest finding or decision as the next starting point.

## Handoff Rule

End each meaningful chunk of work with a short handoff entry in either `findings.md` or `decision_log.md`.
The handoff should point to the exact files, artifacts, or checks the next agent should read first.
