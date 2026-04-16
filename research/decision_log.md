# Decision Log

Append decisions here when scope, methods, or standards change.

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
