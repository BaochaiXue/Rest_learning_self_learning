# Nested Learning Theory Audit Plan

## Objective

- Audit the theory section of the Nested Learning paper and separate:
  - exact algebraic derivations
  - definition-dependent reformulations
  - interpretive or overstated claims
  - proof steps that are incorrect or too loose as written

## Scope / Non-Goals

- In scope:
  - `nested_learning_textbook/papers/nested_learning_the_illusion_of_deep_learning_architectures/`
  - `nested_learning_textbook/book/chapters/11_nested_learning.tex`
  - `nested_learning_textbook/docs/quality/claim_honesty_policy.md`
  - durable audit artifacts under `research/` and `nested_learning_textbook/notes/`
- Out of scope:
  - rewriting chapter prose
  - rerunning paper experiments
  - judging novelty against the full external literature
  - proving or disproving the entire NL agenda from first principles

## Inputs / Dependencies

- Primary source:
  - `nested_learning_textbook/papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Intro.tex`
  - `nested_learning_textbook/papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Methods.tex`
  - `nested_learning_textbook/papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Experiments.tex`
  - `nested_learning_textbook/papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Conclusion.tex`
  - `nested_learning_textbook/papers/nested_learning_the_illusion_of_deep_learning_architectures/merged_paper.tex`
- Local policy and textbook framing:
  - `nested_learning_textbook/docs/quality/claim_honesty_policy.md`
  - `nested_learning_textbook/book/chapters/11_nested_learning.tex`

## Work Breakdown

1. Preparation:
   - read the NL paper sections that contain definitions, derivations, and takeaway claims
2. Evidence gathering:
   - extract exact claim anchors for derivations, interpretations, and proof steps
3. Analysis:
   - classify statements into exact, reformulation-only, or overstated
4. Verification:
   - inspect appendix derivations for algebraic consistency
5. Logging and synthesis:
   - write a root audit memo, a paper note, a claim table, and findings

## Verification Plan

- Check algebra against the displayed objectives and updates.
- Run `python3 scripts/research_check.py`.
- Run `make check` in `nested_learning_textbook/` and record blockers honestly.

## Failure / Rollback Plan

- If a derivation cannot be certified, mark it `uncertain` instead of forcing a verdict.
- Do not modify canonical textbook content.
- Keep changes confined to notes, audit files, and handoffs.

## Files To Touch

- `research/nested_learning_theory_audit/plan.md`
- `research/nested_learning_theory_audit/audit.md`
- `research/findings.md`
- `research/claims_registry.md`
- `nested_learning_textbook/notes/papers/nested_learning_the_illusion_of_deep_learning_architectures.md`
- `nested_learning_textbook/notes/tables/nested_learning_claim_audit.md`
- `nested_learning_textbook/docs/handoffs/latest_handoff.md`

## Completion Checklist

- [x] Primary NL source read locally
- [x] Exact derivations separated from interpretation
- [x] Overclaims identified with evidence anchors
- [x] Verification run or blocker recorded
- [x] `research/findings.md` updated
- [x] Child-project handoff updated
