---
name: experiment-loop
description: Run the default hypothesis-to-execution loop for a minimal experiment, including implementation, verification, logging, and next-step decisions. Use when a hypothesis is ready to become a concrete experiment or analysis run. Do not use for pure literature reading, abstract planning, or broad benchmark wishlists without a first closed loop.
---

# Experiment Loop

## Inputs

- active `research/research_plan.md`
- current hypothesis and verification criteria
- code or scripts needed for the smallest executable step

## Outputs

- updated `research/findings.md`
- updated `research/experiment_queue.csv`
- optional updates to `research/decision_log.md` and `research/open_questions.md`

## Do This

1. Confirm the minimal experiment and its stop condition.
2. Limit the implementation to the smallest diff needed.
3. Run or prepare the experiment with explicit verification steps.
4. Log observations, artifacts, and failures in `research/findings.md`.
5. Update `research/experiment_queue.csv` with status and next action.
6. Recommend whether to iterate, stop, or gather more evidence.

## Guardrails

- Do not run experiments without a logging path.
- Do not call an experiment complete before verification.
- Do not let scope grow while the first loop is still unresolved.
