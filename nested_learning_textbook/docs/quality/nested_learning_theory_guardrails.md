# Nested Learning Theory Guardrails
**Version**: 1.0 | **Date**: 2026-04-16

This page is the local guardrail file for work touching Chapter 11, NL summaries, paper notes, handoffs, or any prose that could accidentally present the Nested Learning worldview as settled theory.

---

## Why This File Exists

The NL paper contains a mix of:

- exact local derivations
- definitional reformulations
- broad interpretive claims
- a few as-written derivations that should not be cited as strict proofs

Agents and human editors should not blur these layers.

---

## Safe To State As Facts

These are acceptable as mechanism-level statements when the assumptions are named:

- linear attention recurrences can be written as optimization updates under a chosen objective
- delta-rule memory can be written as an `L2` objective plus a retention term
- softmax attention can be presented as a non-parametric weighted-regression solution
- backpropagation / gradient descent can be rewritten as a proximal update around local error signals

Recommended wording:

- “在给定目标函数和假设下，可以重写为……”
- “这是一个局部机制层面的等价 / 重写”

---

## Must Be Framed As Viewpoint Or Research Agenda

These are not to be presented as settled textbook facts:

- “架构是算法的幻像”
- “所有现代架构本质上都是统一前馈层”
- “pre-training 是 in-context learning”
- “ICL 不是 emergent，而只是多层嵌套的直接结果”
- “NL 已经统一解释了深度学习的本质”

Recommended wording:

- “这是 NL 提出的统一视角”
- “这是一个研究议程，而不是社区定论”
- “在 NL 的重写语言里，可以这样理解”

Forbidden wording:

- “已经严格证明……”
- “已经揭示了本质……”
- “已经解释了一切……”

---

## Known Proof Caveats

### 1. Muon Derivation

- Do not cite the NL paper's Muon objective-to-update derivation as theorem-level proof.
- Safe wording:
  - “论文给出了设计动机，但 as-written derivation 仍需补齐。”

### 2. DGD Appendix

- Do not cite the NL paper's DGD appendix as a clean strict derivation without caveat.
- Safe wording:
  - “正文中的更新式可作为归一化输入特例下的启发性结果，但 appendix 写法仍需整理。”

### 3. Adam “Optimal Associative Memory”

- Only say this relative to the paper's constructed element-wise objective.
- Do not let readers infer this is a general theorem about Adam itself.

Recommended wording:

- “相对于论文自造的目标函数，Adam-like 更新是自然或最优的。”

---

## Required Cross-Checks Before Editing Chapter 11

1. Read `docs/quality/claim_honesty_policy.md`
2. Read `notes/tables/nested_learning_claim_audit.md`
3. If adding a strong theoretical sentence, ask:
   - is this a recurrence-level equivalence?
   - or only a unifying interpretation?
   - or an as-written proof that already has caveats?

---

## Teaching Rule

The right teaching pattern for NL is:

1. state the local mechanism
2. name the exact assumptions
3. explain the larger viewpoint
4. clearly mark where the proof stops

If a sentence skips step 2 or step 4, it is probably too strong.
