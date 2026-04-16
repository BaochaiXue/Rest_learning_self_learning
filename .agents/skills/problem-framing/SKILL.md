---
name: problem-framing
description: Turn a fuzzy research idea into a scoped plan with non-goals, success criteria, risks, dependencies, and a minimal validation path. Use when the problem is broad, under-specified, or missing evaluation criteria. Do not use when the task is already tightly scoped or when the work is purely literature gathering, implementation, or drafting.
---

# Problem Framing

## Inputs

- user goal or rough idea
- current repo context
- existing plans, decisions, and open questions

## Outputs

- `research/research_plan.md` created from `research/research_plan.template.md` or updated in place
- updated `research/open_questions.md` when uncertainty remains
- updated `research/decision_log.md` when scope is narrowed

## Do This

1. Read `AGENTS.md`, `PLANS.md`, and `research/README.md`.
2. Restate the objective in one sentence.
3. Define scope and non-goals before proposing work.
4. Identify the smallest success criteria and the minimal verification path.
5. List evidence dependencies, risks, and unresolved questions.
6. If the topic is still ambiguous, recommend explicit subagents such as `research_architect`, `literature_scout`, and `novelty_auditor`.
7. Write the resulting plan to `research/research_plan.md`.

## Guardrails

- Do not move into implementation without evaluation criteria.
- Do not pretend missing evidence is already known.
- Do not leave planning logic only in chat.
