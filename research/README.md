# Research State

Use `research/` as the durable state layer for active and future topics.
Do not keep important intermediate conclusions only in chat.

## File Roles

| File | Role | Update Style |
|---|---|---|
| `research_plan.template.md` | template for a concrete topic plan | copy, then adapt |
| `findings.md` | append-only log of actions, outcomes, and artifacts | append |
| `literature_map.md` | source map and evidence inventory | edit in place |
| `claims_registry.md` | claim-level status and evidence pointers | edit in place |
| `decision_log.md` | decisions, reversals, and rationale | append |
| `open_questions.md` | blockers and unresolved evidence needs | edit in place |
| `paper_queue.csv` | paper/source triage queue | edit status rows |
| `experiment_queue.csv` | experiment work queue | edit status rows |
| `reviews/repro_checklist.md` | reproducibility gate before sharing | edit in place |

## Working Rules

- Create `research/research_plan.md` from the template when a concrete topic starts.
- After substantive experiments or code changes, append to `findings.md`.
- Claims belong in `claims_registry.md`, not only in prose drafts.
- Keep file paths repo-relative.
- Separate observation from interpretation whenever possible.

## Minimal Resume Sequence

1. Read `AGENTS.md`.
2. Read `research/research_plan.md` if it exists, otherwise start from the template.
3. Read `findings.md`, `claims_registry.md`, and `open_questions.md`.
4. Resume from the highest-priority unresolved item.
