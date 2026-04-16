---
name: literature-triangulation
description: Gather and compare papers, official documentation, benchmark sources, and related references while separating primary from secondary sources and verified from uncertain claims. Use when validating claims, filling related work, comparing methods, or finding baseline coverage. Do not use for speculative synthesis, coding, or conclusion writing before the sources are checked.
---

# Literature Triangulation

## Inputs

- current research question or claim to verify
- source candidates, search terms, or benchmark names
- existing entries in `research/literature_map.md` and `research/claims_registry.md`

## Outputs

- updated `research/literature_map.md`
- updated `research/claims_registry.md`
- optional updates to `research/open_questions.md` when evidence is still missing

## Do This

1. Prefer primary sources first: original papers, benchmark owners, official documentation, official repos.
2. Record each source with its role, relevance, and confidence.
3. Mark whether a source is primary or secondary.
4. Mark each extracted claim as `verified` or `uncertain`.
5. Note missing comparisons, unknown setup details, and baseline gaps.
6. Update the claim registry with evidence pointers instead of prose-only summaries.

## Guardrails

- Do not make strong conclusions from abstracts alone.
- Do not mix primary and secondary evidence without labeling them.
- Do not claim novelty here; hand novelty judgments to `novelty_auditor`.
