# ARCHITECTURE.md — Repo Layers

## Top-Level Model

This repository is intentionally split into two layers:

```text
Rest_learning/
├── root docs + research OS        # maps, policies, plans, handoffs, durable state
└── nested_learning_textbook/      # active child project and canonical manuscript
```

The root layer standardizes how Codex plans, decomposes, verifies, logs, and resumes research work.
The child project keeps its own domain-specific docs and build rules.

## Root Documentation System Of Record

```text
docs/
├── index.md
├── design-docs/
├── exec-plans/
├── handoffs/
├── quality/
├── references/
├── generated/
├── reliability.md
├── USAGE.md
└── BATCH_WORKFLOWS.md
```

Responsibilities:

- `docs/index.md`: root map and read order
- `docs/design-docs/`: durable beliefs and architecture rationale
- `docs/exec-plans/`: phase plans and operational plans
- `docs/handoffs/`: checkpoint summaries and phase transitions
- `docs/quality/`: claim honesty and QA rubric
- `docs/reliability.md`: reproducibility and operating safeguards
- `docs/references/`: source inventory and external anchors
- `docs/generated/`: machine-produced audits and reports

## Child Project: `nested_learning_textbook/`

`nested_learning_textbook/` remains the canonical textbook workspace.
Its system of record is still `nested_learning_textbook/docs/`.
Its canonical manuscript is still `nested_learning_textbook/book/`.
Its legacy markdown drafts are still `nested_learning_textbook/manuscript/` and must not be overwritten.

## Source-Of-Truth Rule

- Root docs orchestrate research work across the repo.
- Child docs govern the textbook subtree.
- Root docs must reference child docs rather than duplicate them.
