# Latest Handoff

## Current State

The root repository has been refactored into a harness-style research OS.
`docs/index.md` is the primary map for the root layer.
`AGENTS.md`, `README.md`, and `ARCHITECTURE.md` now point at the docs tree instead of acting like standalone policy blobs.
`research/` is the live state layer, and `templates/sprint_contract.md` is the bounded execution contract for the next topic.

## What Changed

- Added a root `docs/index.md` entrypoint.
- Added `docs/design-docs/` for durable operating beliefs.
- Added `docs/exec-plans/` for active plan structure.
- Added `docs/handoffs/` for resumable checkpoints.
- Added `docs/quality/` for claim honesty and quality gates.
- Added `docs/reliability.md` for operating safeguards.
- Added `docs/references/` for source inventory conventions.
- Added `docs/generated/` for machine-produced audits and reports.
- Added `docs/exec-plans/completed/` so root-level plans have an archive destination.
- Added a live `research/research_plan.md` shell and stronger queue/checklist contracts.
- Tightened `.codex/agents/` and `.agents/skills/` around explicit handoffs, skeptical review, and single-loop execution.
- Added `scripts/research_check.py` and `make research-check` for root-level validation.

## Open Follow-Ups

- If a future task needs a concrete root-level plan, instantiate one under `docs/exec-plans/active/`.
- If a future task needs evidence-backed writing, keep the claims in `research/` and cross-link from the relevant docs page.
- If the child textbook project is touched, its own docs remain authoritative and must be updated separately.
- `make check` still fails in the child textbook audit because of pre-existing absolute-path hits in downloaded paper sources and generated reports.

## Next Recommended Action

Before a new topic starts, read `docs/index.md`, instantiate the topic plan in `research/research_plan.md`, create a sprint contract from `templates/sprint_contract.md`, then spawn the narrow agents needed for that topic.
