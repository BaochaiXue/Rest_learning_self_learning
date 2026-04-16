# AGENTS.md — Research OS Contract

## Repo Purpose

This repository is a reusable multi-agent research operating system layered over an existing child project.
Treat the repo root as the durable orchestration layer.
Treat `nested_learning_textbook/` as an active child workspace with its own stricter local rules.

## Read Order

1. Read this file.
2. Read `README.md`.
3. Read `PLANS.md`.
4. Read `research/README.md`.
5. If a task touches `nested_learning_textbook/`, also read:
   - `nested_learning_textbook/AGENTS.md`
   - `nested_learning_textbook/docs/index.md`
   - `nested_learning_textbook/docs/project_state/current_repo_audit.md`
   - `nested_learning_textbook/docs/handoffs/latest_handoff.md`
   - `nested_learning_textbook/docs/exec-plans/active/`
   - `nested_learning_textbook/docs/quality/qa_rubric.md`

## Default Work Loop

Use this loop unless the user explicitly asks for something narrower:

`plan -> gather evidence -> implement / run -> verify -> log -> synthesize`

Do not jump from a vague idea straight into implementation.

## Planning Rules

- For any non-trivial task, create or update a plan before substantial work.
- Use `PLANS.md` as the reusable template.
- For an active research topic, instantiate `research/research_plan.md` from `research/research_plan.template.md` if it does not exist.
- Plans must state objective, non-goals, dependencies, verification, rollback, and files to touch.

## Durable State Rules

- Important work must land in repo files, not only in chat.
- After any substantive experiment, code change, config change, or evaluation, update `research/findings.md`.
- Record literature structure in `research/literature_map.md`.
- Record claim status in `research/claims_registry.md`.
- Record decisions and reversals in `research/decision_log.md`.
- Record unresolved blockers in `research/open_questions.md`.

## Claim Discipline

- Every research claim must point to a source, experiment artifact, or file path.
- Mark claims as `verified` or `uncertain`.
- Do not fabricate citations, baselines, datasets, benchmarks, settings, or results.
- Do not write conclusions that cannot be traced back to evidence.
- If work touches the textbook subtree, also follow `nested_learning_textbook/docs/quality/claim_honesty_policy.md`.

## Subagent Rules

Spawn subagents explicitly when work can proceed independently and in parallel.
Good cases:

- literature scouting across distinct source questions
- novelty audit separate from source gathering
- experiment design separate from implementation
- reproducibility review after implementation
- alternative plan decompositions for a fuzzy topic

Do not assume the surface auto-parallelizes.
Wait for all critical subagents to return before writing the synthesis.
Keep roles narrow; do not create a general-purpose "do everything" agent.

## Path And Scope Rules

- Use repo-relative paths in files.
- Do not let important state hide in temporary notes or shell history.
- Do not overwrite `nested_learning_textbook/manuscript/*.md`.
- New root-level docs should orchestrate work; they must not replace `nested_learning_textbook/docs/` as the textbook source of truth.

## Done-When

Work is done only when:

- the requested artifact or change exists in the right file
- verification has been run or an explicit blocker is recorded
- `research/findings.md` reflects substantive work
- conclusions are traceable to evidence
- if `nested_learning_textbook/` changed, `nested_learning_textbook/docs/handoffs/latest_handoff.md` is updated
- if `nested_learning_textbook/` changed, run `make check`
- if LaTeX content changed, also run `make book`

## Operating Bias

- Prefer small, reversible diffs.
- Prefer primary sources over summaries.
- Prefer a minimal closed loop over a sprawling plan.
- Prefer explicit evidence gaps over confident guessing.
