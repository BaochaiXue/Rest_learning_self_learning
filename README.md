# Multi-Agent Vibe Research OS

This repository now serves two roles:

1. A reusable root-level research operating system for Codex-driven work.
2. An existing child project at `nested_learning_textbook/` with its own canonical docs and build flow.

The root is for planning, skills, custom agents, durable research state, and batch workflows.
The textbook subtree remains the canonical workspace for the inference-time learning book.

## What Lives Here

```text
.
├── AGENTS.md                      # Repo-wide operating contract
├── PLANS.md                       # Reusable planning template
├── .codex/                        # Repo-local Codex config and custom agents
├── .agents/skills/                # Repo-scoped skills
├── docs/                          # Root-level usage and batch workflow docs
├── research/                      # Durable state for active and future topics
├── templates/                     # Reusable note templates
└── nested_learning_textbook/      # Existing child project with its own rules
```

## Default Workflow

Use the same loop for most research tasks:

`plan -> gather evidence -> implement / run -> verify -> log -> synthesize`

Practical implications:

- Start non-trivial work by creating or updating a plan.
- Keep evidence in files under `research/`, not only in chat.
- Update `research/findings.md` after substantive experiments or code changes.
- Mark claims as `verified` or `uncertain`.

## Root-Level Skills

The repo ships with six repo-scoped skills:

- `problem-framing`: turn a fuzzy idea into a scoped research plan
- `literature-triangulation`: compare sources and register evidence-backed claims
- `experiment-loop`: move from hypothesis to a minimal executed loop
- `claim-audit`: inspect whether a draft claim is actually supported
- `paper-drafting`: draft prose from verified artifacts only
- `repro-check`: review reproducibility before sharing results

Skill definitions live under `.agents/skills/`.
If a task clearly matches a skill, explicitly invoke it in your prompt, for example:

```text
Use $problem-framing and create `research/research_plan.md` from the template.
```

## Custom Agents

Repo-local agents live under `.codex/agents/`.
Use them explicitly when you want clear responsibility boundaries, for example:

```text
Spawn `research_architect`, `literature_scout`, and `novelty_auditor` in parallel.
Wait for all three before synthesizing the answer.
```

Recommended handoff chain:

`research_architect -> literature_scout / novelty_auditor -> experiment_designer -> implementer -> repro_reviewer -> writer`

Fresh threads are safer after creating or editing custom agent files because some Codex surfaces do not hot-load them reliably in the same conversation.

## Start A New Research Topic

1. Read `AGENTS.md`, `PLANS.md`, `research/README.md`, and the relevant skill files.
2. Copy `research/research_plan.template.md` to `research/research_plan.md`.
3. Run a first pass with `problem-framing`.
4. Spawn `research_architect`, `literature_scout`, and `novelty_auditor` in parallel if the topic is still ambiguous.
5. Write outputs back to:
   - `research/research_plan.md`
   - `research/literature_map.md`
   - `research/claims_registry.md`
   - `research/open_questions.md`
   - `research/decision_log.md`
6. Only then move into `experiment-loop`, implementation, drafting, or reproducibility review.

## Working With `nested_learning_textbook/`

If the task touches `nested_learning_textbook/`, also follow that subtree's operating rules:

- read `nested_learning_textbook/AGENTS.md`
- use `nested_learning_textbook/docs/` as the textbook source of truth
- do not overwrite `nested_learning_textbook/manuscript/*.md`
- update `nested_learning_textbook/docs/handoffs/latest_handoff.md` after substantial work
- run `make check` before calling a phase done

See `docs/USAGE.md` for prompt examples and `docs/BATCH_WORKFLOWS.md` for queue-driven parallel workflows.
