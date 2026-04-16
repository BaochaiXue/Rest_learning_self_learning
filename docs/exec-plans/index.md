# docs/exec-plans/index.md

This directory holds execution-plan structure for root-level work.
Use it when a task needs a durable operational plan, phase checkpoints, or a resumable status trail.

## Structure

- `active/`: current plans and live phase notes
- `completed/`: archive later, if the repo grows enough to need it

## Rules

- Keep one file per plan or workstream.
- Keep plans short enough to scan quickly.
- Include objective, dependencies, verification, rollback, and next checkpoint.
- If a topic already has a topic-specific plan in `research/`, link to it rather than duplicating it here.
