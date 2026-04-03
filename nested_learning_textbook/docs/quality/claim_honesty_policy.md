# Claim Honesty Policy
**Version**: 1.0 | **Date**: 2026-04-03

This policy governs what kinds of claims can be stated as facts vs. must be framed as interpretations, in both the LaTeX book and in documentation.

---

## The Core Distinction

| Type | What it is | How to write it |
|---|---|---|
| **Mechanism-level consensus** | Mathematically proven, reproducible, well-established in literature | State as fact. Cite the paper(s). |
| **Interpretive framing** | A useful lens, a suggestive analogy, or a theoretical proposal | Frame as "一种視角" / "一种解释" / "研究议程" |
| **Speculative claim** | An extrapolation beyond what papers actually show | Must NOT appear as a confident assertion; label as "开放问题" |

---

## Specific Rulings for Key Claims in This Book

### ICL = Gradient Descent

- **What's stable**: Single-layer linear self-attention computes exactly one step of gradient descent on a linear regression objective (von Oswald et al., 2022). This is a mathematical theorem; it can be stated as fact.
- **What's interpretive**: "Large language models do in-context learning by running gradient descent under the hood." This extrapolates from toy settings to billion-parameter nonlinear models. Must be framed as: *"这是一种富有启发性的解释视角，在线性玩具模型上有严格对应，但在完整大模型上尚无等价的严格证明。"*
- **Forbidden formulation**: "大语言模型的 ICL 已被证明等价于梯度下降。"

### Linear Attention = Fast Weights

- **What's stable**: With specific kernel choices (no Softmax), the update rule for the output of a linear attention layer is mathematically identical to the outer-product fast weight update. This is a formal equivalence; state as fact (cite Schlag et al., 2021).
- **What's interpretive**: "Softmax attention is also a form of fast weights." This is a suggestive analogy; frame as interpretation.

### TTT Layers = Learning at Test Time

- **What's stable**: TTT-Linear and TTT-MLP update their hidden state via gradient descent on a self-supervised objective at inference time. This is the mechanism; state as fact.
- **What's interpretive**: "Therefore all RNNs are implicitly doing test-time learning." This overgeneralizes; label as pedagogical analogy.

### Nested Learning as Unifying Framework

- **What's stable**: Nested Learning provides a formal framework in which gradient-based optimizers can be rewritten as associative memory update rules. The mathematical formulation in Behrouz et al. (2025) is a specific contribution.
- **What's interpretive**: "Nested Learning proves that all deep learning architectures are illusions." This is an interpretive claim about the *scope* of the framework. Must be framed as: *"这是 NL 论文提出的一个大统一视角，而不是已被整个社区接受的定论。"*
- **Forbidden formulation**: "深度学习的本质已被 Nested Learning 完整揭示。"

---

## Writing Rules

1. **Use theorem/definition/corollary environments ONLY for mathematically rigorous statements.**
2. **Use `\begin{remark}` or custom `\begin{insight}` environments for interpretive claims.**
3. **Use `\begin{openproblem}` for speculative claims and research directions.**
4. **Always cite the paper** that is the source of any specific claim.
5. **"教材解释" label**: When the textbook synthesizes across papers in a way that no single paper states, add: *（以下为教材归纳，非直接引用某篇论文结论）*

---

## Enforcement

Every chapter, before being marked complete, must be reviewed against this policy.  
The `docs/quality/qa_rubric.md` Dimension 9 checks enforce this at the chapter level.
