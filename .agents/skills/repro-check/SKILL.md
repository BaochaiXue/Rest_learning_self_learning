---
name: repro-check
description: Review whether a result is reproducible enough for sharing by checking seeds, environments, data splits, evaluation protocol, and artifact coverage. Use before external sharing, publication, or strong result claims. Do not use during early ideation or when no environment and evaluation details exist yet.
---

# Repro Check

## Inputs

- current result summary or draft claim
- run artifacts, config files, environment notes, and evaluation details
- `research/reviews/repro_checklist.md`

## Outputs

- updated `research/reviews/repro_checklist.md`
- blocking items or risk notes in `research/open_questions.md`

## Do This

1. Check seed handling, environment capture, versions, and dependencies.
2. Check data splits, evaluation protocol, and metric definitions.
3. Check whether artifacts are sufficient for another person to reproduce the result.
4. Assign a risk level and list the missing pieces.
5. Refuse to certify reproducibility when critical evidence is absent.

## Guardrails

- Do not ignore leakage risks.
- Do not treat a one-off successful run as reproducible by default.
- Do not close the review until blockers are recorded clearly.
