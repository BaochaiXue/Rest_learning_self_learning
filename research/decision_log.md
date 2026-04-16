# Decision Log

Append decisions here when scope, methods, or standards change.
This log should explain what changed, why it changed, and what it supersedes.

## Decision Contract

- Keep decisions append-only unless you are correcting metadata.
- Include the alternatives considered.
- Link the decision to the files or artifacts that motivated it.
- Use this file when a change affects workflow, scope, or review standards.

## Entry Template

### YYYY-MM-DD | Decision title

- Decision:
- Why:
- Alternatives considered:
- Evidence:
- Supersedes:

### 2026-04-15 | Layer the research OS at repo root

- Decision: Keep the new research operating system at the repo root and keep `nested_learning_textbook/` as a child project with its own canonical docs.
- Why: The repository is not empty; replacing the child project's governance would create competing sources of truth.
- Alternatives considered: Creating a second textbook-specific planning tree at root.
- Evidence: `AGENTS.md`, `README.md`, and `ARCHITECTURE.md`.
- Supersedes: none

### 2026-04-15 | Add execution-contract workflow

- Decision: Use a sprint contract template for bounded execution chunks and add a root-level research check target.
- Why: Planning, evidence gathering, and execution need a lightweight handoff artifact so future topics can stay small and reviewable.
- Alternatives considered: Encoding the same structure only inside ad hoc prompts or only inside the live plan file.
- Evidence: `research/research_plan.template.md`, `templates/sprint_contract.md`, `scripts/research_check.py`, `Makefile`.
- Supersedes: none
