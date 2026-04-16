# Reliability

This page collects the operating rules that make the root research OS usable over long sessions.

## What Reliability Means Here

- Long tasks can be resumed from files.
- Important decisions are not trapped in chat history.
- Plans, handoffs, and logs stay in sync.
- Verification is explicit instead of implied.
- Queue-driven or multi-agent work can be repeated without reconstructing context.

## Operating Rules

- Use repo-relative paths everywhere in docs.
- Update `docs/handoffs/latest_handoff.md` at phase boundaries.
- Update `research/findings.md` after substantive execution or evaluation.
- Keep claim status in `research/claims_registry.md`.
- Keep open blockers in `research/open_questions.md`.
- Use explicit verification gates before declaring a phase complete.
- Prefer fresh threads after creating or editing custom agents.

## Failure Handling

- If evidence is weak, record the gap instead of overstating the result.
- If a task stalls, log the blocker and the smallest possible next check.
- If a plan becomes stale, refresh it before continuing.
