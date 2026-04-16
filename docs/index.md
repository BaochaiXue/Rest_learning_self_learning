# docs/index.md — Root System Of Record

This directory is the root map for the vibe-research operating system.
It is not the active research log.
It is the durable place for structure, policy, plans, handoffs, quality rules, references, and generated audits.

Use this page as the entrypoint when you need to know where something belongs.

## Read Order

1. `AGENTS.md`
2. `docs/index.md`
3. `README.md`
4. `PLANS.md`
5. `research/README.md`
6. The specific docs page for the current task
7. `nested_learning_textbook/AGENTS.md` and child docs if the task touches the textbook subtree

## Map

```text
docs/
├── index.md
├── design-docs/
│   ├── index.md
│   └── core-beliefs.md
├── exec-plans/
│   ├── index.md
│   ├── active/
│   │   └── index.md
│   └── completed/
│       └── index.md
├── handoffs/
│   ├── index.md
│   └── latest_handoff.md
├── quality/
│   ├── index.md
│   ├── qa_rubric.md
│   └── claim_honesty_policy.md
├── references/
│   └── index.md
├── generated/
│   ├── index.md
│   └── repo_hygiene_report.md
├── reliability.md
├── USAGE.md
└── BATCH_WORKFLOWS.md
```

## Where To Write What

- Use `docs/design-docs/` for durable architecture and operating beliefs.
- Use `docs/exec-plans/` for active plans, checkpoints, and phase-level intent.
- Use `docs/handoffs/latest_handoff.md` for phase boundaries and resumable summaries.
- Use `docs/quality/` for claim honesty and quality gates.
- Use `docs/reliability.md` for reproducibility, traceability, and failure handling guidance.
- Use `docs/references/` for source inventories, canonical links, and external anchors.
- Use `docs/generated/` for machine-produced audits, hygiene reports, and derived summaries.

## Operating Rules

- Keep paths repo-relative.
- Do not use chat as the only record for an important decision.
- Keep root docs concise enough to read before work starts.
- Let the root docs explain where evidence lives; do not duplicate research state here.
- Preserve `nested_learning_textbook/` as the child project source of truth.
