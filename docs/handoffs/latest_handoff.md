# Latest Handoff

## Current State

The root research OS is active and now also contains a completed theory audit for Nested Learning plus textbook-facing guardrail work in the child project.

The most important current fact is:

- the NL paper has several valid local equivalences
- its strongest worldview claims remain interpretive
- the textbook subtree now explicitly warns readers and future agents not to blur those two layers

## What Changed

- Added a root audit for NL theory under `research/nested_learning_theory_audit/`.
- Added claim-level NL audit entries to `research/claims_registry.md`.
- Hardened child-project policy and chapter wording through:
  - `nested_learning_textbook/docs/quality/nested_learning_theory_guardrails.md`
  - `nested_learning_textbook/docs/quality/claim_honesty_policy.md`
  - `nested_learning_textbook/docs/quality/qa_rubric.md`
  - `nested_learning_textbook/AGENTS.md`
  - `nested_learning_textbook/book/chapters/11_nested_learning.tex`
- Updated child-project notes so future NL work has a local claim-audit table and expanded paper note.

## Verification

- `python3 scripts/research_check.py` | ✅ Passed
- `git diff --check` | ✅ Passed
- `cd nested_learning_textbook && make book` | ✅ Passed
- `cd nested_learning_textbook && make check` | ❌ Failed on the same 24 pre-existing absolute-path hits in downloaded paper sources and generated hygiene reports

## Open Follow-Ups

- If future work touches Chapter 11 or NL theory language, start from:
  - `nested_learning_textbook/docs/quality/nested_learning_theory_guardrails.md`
  - `nested_learning_textbook/notes/tables/nested_learning_claim_audit.md`
- The child-project absolute-path hygiene issue is still unresolved and remains the blocker for a clean `make check`.
- The BCI sprint artifacts are still missing under `research/experiments/bci/`; that work is orthogonal to the NL guardrail changes.

## Next Recommended Action

If the next task is textbook-related, do one of these:

1. propagate the new NL caution language into any other chapter or summary that currently overstates the theory
2. clean up or formally exempt the 24 known absolute-path hits so textbook verification can go fully green
