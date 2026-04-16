---
name: claim-audit
description: Audit whether draft claims, novelty statements, and result summaries are fully supported by sources or experiment artifacts. Use before writing conclusions, abstracts, related-work judgments, or novelty claims. Do not use as a substitute for literature gathering or experiment execution.
---

# Claim Audit

## Inputs

- candidate claims from notes, drafts, or summaries
- `research/claims_registry.md`
- source links, findings, and experiment artifacts

## Outputs

- updated `research/claims_registry.md`
- a short risk list in `research/open_questions.md` or the working draft

## Do This

1. Check every candidate claim against a source, artifact, or file path.
2. Downgrade unsupported statements to `uncertain`.
3. Identify missing citations, missing runs, or missing controls.
4. Point to the exact evidence gap that blocks a safe claim.
5. Require follow-up verification before the claim appears in a final draft.

## Guardrails

- Do not leave unsupported claims in final prose.
- Do not let interpretive framing masquerade as consensus.
- Do not assume chat summaries count as evidence.
