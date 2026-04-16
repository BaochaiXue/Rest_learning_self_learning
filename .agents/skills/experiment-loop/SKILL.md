---
name: experiment-loop
description: Run the default hypothesis-to-execution loop for a minimal experiment, including implementation, verification, logging, and the next handoff. Use when a hypothesis is ready to become a concrete experiment or analysis run. Do not use for pure literature reading, abstract planning, or broad benchmark wishlists without a first closed loop.
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
- a short handoff note naming the next action, owner, and acceptance criteria

## Do This

1. Confirm the minimal experiment and its stop condition.
2. Write or restate the experiment contract before touching code: inputs, controls, metrics, stop criteria, and rollback.
3. Limit the implementation to the smallest diff needed.
4. Run or prepare the experiment with explicit verification steps.
5. Log observations, artifacts, and failures in `research/findings.md`.
6. Update `research/experiment_queue.csv` with status and next action.
7. Recommend whether to iterate, stop, or gather more evidence.
8. Leave a handoff note that another agent can pick up without rereading chat.

## Guardrails

- Do not run experiments without a logging path.
- Do not call an experiment complete before verification.
- Do not let scope grow while the first loop is still unresolved.
- Do not start a second loop until the first loop is closed in the queue and findings.
