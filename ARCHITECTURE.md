# ARCHITECTURE.md — Repo Layers

## Top-Level Model

This repository is intentionally split into two layers:

```text
Rest_learning/
├── root research OS               # planning, skills, agents, durable state
└── nested_learning_textbook/      # active child project and canonical manuscript
```

The root layer exists to standardize how Codex plans, decomposes, verifies, logs, and resumes research work.
The child project keeps its own domain-specific docs and build rules.

## Root Research OS

```text
.
├── AGENTS.md
├── PLANS.md
├── .codex/
├── .agents/skills/
├── docs/
├── research/
└── templates/
```

Responsibilities:

- repo-wide operating rules
- repo-local custom agents
- repo-scoped skills
- durable research state
- reusable templates
- batch workflow conventions

## Child Project: `nested_learning_textbook/`

`nested_learning_textbook/` remains the canonical textbook workspace.
Its system of record is still `nested_learning_textbook/docs/`.
Its canonical manuscript is still `nested_learning_textbook/book/`.
Its legacy markdown drafts are still `nested_learning_textbook/manuscript/` and must not be overwritten.

## Source-Of-Truth Rule

- Root docs orchestrate research work across the repo.
- Child docs govern the textbook subtree.
- Root docs must reference child docs rather than duplicate them.
