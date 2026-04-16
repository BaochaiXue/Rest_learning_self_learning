# Batch Workflows

This repo does not yet include an automatic batch runner.
Use the CSV queues as declarative worklists that can be processed manually or by explicit multi-agent fan-out.

## Queue Files

- `research/paper_queue.csv`: source triage and literature coverage work
- `research/experiment_queue.csv`: experiment design, execution, and review work

## Recommended Status Values

Use these values consistently:

- `queued`
- `in_progress`
- `blocked`
- `done`
- `dropped`

## `paper_queue.csv` Conventions

Recommended meaning of columns:

- `id`: stable row identifier
- `title_or_query`: paper title, search query, or benchmark page name
- `source_hint`: URL, venue hint, or repo name
- `priority`: `P0`, `P1`, `P2`, or `P3`
- `status`: queue state
- `assigned_agent`: usually `literature_scout` or `novelty_auditor`
- `depends_on`: upstream row ID if sequencing matters
- `output_path`: usually `research/literature_map.md`
- `notes`: short operator note

## `experiment_queue.csv` Conventions

Recommended meaning of columns:

- `id`: stable experiment ID
- `hypothesis_slice`: smallest question this row tests
- `priority`: `P0`, `P1`, `P2`, or `P3`
- `status`: queue state
- `assigned_agent`: usually `experiment_designer`, `implementer`, or `repro_reviewer`
- `depends_on`: upstream experiment ID if needed
- `artifact_path`: where findings or outputs should be logged
- `verification_gate`: metric, stop condition, or comparison that must be met
- `next_action`: the next concrete move if this row is picked up

## Manual Parallel Pattern

Use the queues to drive explicit parallel work:

1. Pick independent rows with no unresolved dependencies.
2. Spawn one narrow agent per row or per small row bundle.
3. Require each agent to write results back to the queue target file.
4. Wait for all critical rows to finish before synthesizing conclusions.
5. Update queue status immediately after the result is logged.

## Safe Operating Rules

- Do not batch rows that depend on the same unresolved evidence.
- Do not let parallel agents write to the same output section without a merge plan.
- Do not call a queue item done until its result is logged in `research/findings.md` or the designated output file.
- If automatic batching is added later, keep these CSV schemas stable so the runner can remain thin.
