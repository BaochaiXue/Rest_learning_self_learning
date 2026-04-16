# Multi-Agent Vibe Research OS

This repository has two layers:

1. A root research operating system for Codex-driven work.
2. An existing child project at `nested_learning_textbook/` with its own canonical docs and build flow.

The root layer is the coordination and documentation system.
The child subtree remains the canonical workspace for the inference-time learning book.

## Root Map

```text
.
├── AGENTS.md
├── PLANS.md
├── README.md
├── ARCHITECTURE.md
├── docs/
│   ├── index.md
│   ├── design-docs/
│   ├── exec-plans/
│   ├── handoffs/
│   ├── quality/
│   ├── references/
│   ├── generated/
│   ├── reliability.md
│   ├── USAGE.md
│   └── BATCH_WORKFLOWS.md
├── research/
├── templates/
└── nested_learning_textbook/
```

## Default Workflow

Use the same loop for most research tasks:

`plan -> gather evidence -> implement / run -> verify -> log -> synthesize`

Practical implications:

- Start non-trivial work by creating or updating a plan.
- Read `docs/index.md` before you decide where an artifact belongs.
- Keep evidence in files under `research/` and in the relevant root docs page, not only in chat.
- Update `research/findings.md` after substantive experiments or code changes.
- Mark claims as `verified` or `uncertain`.

## Skills And Agents

Repo-scoped skills live under `.agents/skills/`.
Custom agents live under `.codex/agents/`.
Use them explicitly when you want clear responsibility boundaries.

Examples:

```text
Use $problem-framing and create `research/research_plan.md` from the template.
Spawn `research_architect`, `literature_scout`, and `novelty_auditor` in parallel.
Wait for all three before synthesizing the answer.
```

Recommended handoff chain:

`research_architect -> literature_scout / novelty_auditor -> experiment_designer -> implementer -> repro_reviewer -> writer`

Fresh threads are safer after creating or editing custom agent files because some Codex surfaces do not hot-load them reliably in the same conversation.

## Start A New Research Topic

1. Read `AGENTS.md`, `docs/index.md`, `PLANS.md`, `research/README.md`, and the relevant skill files.
2. Copy `research/research_plan.template.md` to `research/research_plan.md`.
3. Run a first pass with `problem-framing`.
4. Spawn `research_architect`, `literature_scout`, and `novelty_auditor` in parallel if the topic is still ambiguous.
5. Write outputs back to:
   - `research/research_plan.md`
   - `research/literature_map.md`
   - `research/claims_registry.md`
   - `research/open_questions.md`
   - `research/decision_log.md`
6. Use `docs/handoffs/latest_handoff.md` whenever a phase boundary needs a durable checkpoint.
7. Only then move into `experiment-loop`, implementation, drafting, or reproducibility review.

## Working With `nested_learning_textbook/`

If the task touches `nested_learning_textbook/`, also follow that subtree's operating rules:

- read `nested_learning_textbook/AGENTS.md`
- use `nested_learning_textbook/docs/` as the textbook source of truth
- do not overwrite `nested_learning_textbook/manuscript/*.md`
- update `nested_learning_textbook/docs/handoffs/latest_handoff.md` after substantial work
- run `make check` before calling a phase done

See `docs/USAGE.md` for prompt examples and `docs/BATCH_WORKFLOWS.md` for queue-driven parallel workflows.
