---
name: paper-drafting
description: Draft paper-style sections from verified findings, explicit source pointers, and tracked evidence gaps. Use when verified artifacts already exist and you need aligned prose for abstracts, methods, experiments, or appendices. Do not use to invent citations, results, or settings, and do not use before claim audit is complete.
---

# Paper Drafting

## Inputs

- verified findings and artifact links
- `research/claims_registry.md`
- source pointers and any approved citation placeholders

## Outputs

- structured draft text in the requested destination
- explicit citation placeholders where sources are known but not yet inserted
- optional updates to `research/open_questions.md` when drafting exposes evidence gaps
- a short handoff note if the draft exposed a missing claim or repro issue

## Do This

1. Read the claims registry before writing.
2. Use only verified findings and explicit evidence pointers.
3. Keep related-work comparisons calibrated.
4. Add citation placeholders rather than inventing references.
5. Call out unresolved evidence gaps instead of smoothing over them.
6. Route unsupported statements back to claim audit instead of drafting them as facts.

## Guardrails

- Do not fabricate citations, results, setups, or baselines.
- Do not present uncertain claims as conclusions.
- Do not trigger this skill before claim audit unless the user explicitly wants an early rough draft.
- Do not let prose outrun the artifact chain.
