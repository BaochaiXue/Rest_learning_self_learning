# Pedagogy Principles
**Version**: 2.0 | **Date**: 2026-04-03  
**Supersedes**: Any prior informal writing conventions  
**Applies to**: All chapter `.tex` files in `book/chapters/`

This document is the **canonical reference for how this textbook is written**.  
Every contributor and agent must read this before editing any chapter.

---

## Core Mandate (B11)

This textbook simultaneously optimizes three goals. They are **not** in tension; all three must be present in every section:

1. **Mathematically rigorous** — formal definitions, precise symbols, derivations with trackable steps
2. **Pedagogically clear** — a CS undergraduate with linear algebra and basic calculus can follow everything
3. **Neuroscience-grounded intuition** — analogies from brain science that help build intuition, with *explicit* similarity and difference statements

> **One-sentence style target**: Use rigorous formalization to guarantee truth, clear explanation to guarantee understanding, neuroscience analogy to guarantee intuition — but never substitute analogy for conclusion.

---

## The Three-Layer Explanation Structure (B12, B18)

Every **core concept**, **key mechanism**, and **principal formula** must be explained with the following three layers, in this order:

### Layer 1: Formal Statement
- Precise definition, symbols, objective, assumptions, main formula
- Each variable defined on first appearance
- The problem this formalization solves, stated explicitly
- If there is a key derivation: give the minimum-but-genuine derivation sketch

### Layer 2: Algorithmic/System Intuition
- What is being *computed*?
- Why is the computation organized this way?
- How does this connect to adjacent chapters?
- The reader must understand what is happening at the *computation* level — not just what to call it

### Layer 3: Bounded Neuroscience Analogy
- Which neuroscience phenomenon gives intuition for this mechanism?
- **Required content** (B14 — all four must appear):
  1. What does this analogy help the reader understand?
  2. Which computation or memory function does it correspond to?
  3. Where does the analogy differ from the real biological mechanism?
  4. What must the reader *not* incorrectly conclude from this analogy?
- Use the standard Analogy Template below

### Chapter-level rhythm (B18)
```
minimal problem → intuitive picture → formal object → minimal derivation
→ neuroscience analogy → analogy boundary → back to main thread
```
Analogy belongs *after* the math, not instead of it.

---

## The Standard Analogy Template (B22)

When invoking any neuroscience analogy, use this four-block structure.  
It may appear inside a `neurosciencebox` or inline in prose, but all four blocks must be present.

```
[类比对象]
这里我们把 <神经科学概念 X> 视为帮助理解 <模型机制 Y> 的一个类比。

[共同之处]
X 和 Y 在以下层面相似：
- 计算角色上：……（都在做某种 … ）
- 时间尺度上：……（都有 … ）
- 信息流组织上：……（都区分 … ）

[不同之处]
X 和 Y 在以下层面根本不同：
- 更新规则：……
- 实现机制：……（生物是局部/能量约束/噪声；模型是可微/全局目标）
- 学习信号：……

[读者不应推出的结论]
这个类比不支持以下主张：
- 不能推出"Y 就是 X"
- 不能推出"……"
```

---

## Distinguishing Similarity Levels (B13)

When using brain/neuro analogies, explicitly classify which level the similarity is at:

| Similarity Level | Description | Example |
|-----------------|-------------|---------|
| **计算角色相似** | Both perform the same abstract function | Both do associative retrieval |
| **算法组织相似** | Both have fast/slow variables, online/offline distinction | Both distinguish short-term state from long-term storage |
| **实现机制不同** | Concrete update rules differ | Model uses explicit matrix ops + global loss; biology uses local Hebbian rules + neuromodulation |
| **学习信号不同** | How the system knows what to update | TTT uses explicit gradient; synaptic plasticity uses local activity correlations + dopamine |
| **表征与时间尺度不同** | "One step" means different things | Model's "one step" ≠ a single biological process |

At least the first two levels (similarities) and at least two of the last three (differences) must be discussed in every major analogy.

---

## Required Box Environments (B16)

Every chapter **must** have at least one of each:

### `neurosciencebox` — 神经科学直觉
```latex
\begin{neurosciencebox}[title=神经科学直觉：<具体现象名>]
...内容按 B22 模板写...
\end{neurosciencebox}
```

**Content requirements**:
- Identify the neuroscience phenomenon
- Explain the similarity at the right level (B13)
- State what intuition this builds

### `analogyboundarybox` — 类比边界与失效条件
```latex
\begin{analogyboundarybox}[title=这个类比在哪里会失效]
...
\end{analogyboundarybox}
```

**Content requirements**:
- At least two concrete mechanistic differences
- At least one explicit "读者不能从此类比推出……"
- Language must be precise, not emotive

**Both boxes must appear.** A chapter with only `neurosciencebox` but no `analogyboundarybox` fails Dimension 12.

---

## Recommended Neuroscience Analogy Sources by Chapter (B20, B21)

These are **resources for analogy**, not claims of mechanism equivalence.

| Chapter | Recommended neuroscience direction | Similarity level |
|---------|-----------------------------------|-----------------|
| Ch02 test-time learning | Sensorimotor calibration; error-driven online adjustment | 计算角色 |
| Ch03 bilevel optimization | Slow rule formation vs. fast within-task adaptation | 算法组织 |
| Ch04 fast weights | Short-term synaptic plasticity; transient state retention; working memory | 计算角色 + 算法组织 |
| Ch05 attention | Selective attention; context-dependent retrieval | 计算角色 |
| Ch06 ICL | Within-task fast adjustment; temporary rule formation | 计算角色 |
| Ch07 learning to TTT | Systems carrying fast update rules; local plasticity | 算法组织 |
| Ch08 TTT layers | Episode-internal fast plasticity; short-term task-specific reconfiguration | 计算角色 |
| Ch09 Titans | Complementary Learning Systems (CLS): hippocampus + neocortex | 算法组织 |
| Ch10 unified regression | Continuous integration of recent experience | 计算角色 |
| Ch11 Nested Learning | Multi-timescale coordination: neural activity → synaptic change → consolidation | 算法组织 |

---

## Failure Conditions (B25)

A chapter **fails quality review** if any of the following are true:

- [ ] Math is rigorous but too compressed for a CS undergraduate to follow
- [ ] Readability was achieved by sacrificing precision ("大致上来说……")
- [ ] Neuroscience analogy appears but has no explicit difference statement
- [ ] Text contains "模型像大脑一样……" or equivalent imprecise phrasing
- [ ] A section has only `neurosciencebox` but no `analogyboundarybox`
- [ ] The analogy section is longer than the formal explanation section but the mechanism is not clearly explained
- [ ] The reader could finish the chapter knowing only the analogy, not the algorithm
- [ ] A model component is mapped to a specific brain region without explicit caveat that this is an inspirational analogy, not a mechanism claim
- [ ] Functional similarity is written as implementation-level equivalence

---

## Mathematical Writing Standards (B17)

1. Every important symbol is explained at first occurrence
2. Every equation has a sentence explaining what each term *does* (not just what it is)
3. Derivations are not skipped with "可得" — at minimum explain the key step
4. The **preferred sequence** for introducing a formula:
   - First: state the problem
   - Then: introduce each object in the formula
   - Then: explain how the formula expresses the desired computation
   - Then: connect to the next derivation step

---

## Style Target (B15)

Write like a **textbook**, not a philosophy essay. Even when using neuroscience analogies:

| Avoid | Prefer |
|-------|--------|
| "模型像大脑一样思考" | "在计算角色上，这与大脑的X功能相似，即……" |
| "惊奇门阀直接封挡了..." | "当 $s_t < \theta$，参数更新幅度被缩减至接近零" |
| "注定成为……的不朽基石" | "这是理解后续章节的基础" |
| "这就是为什么大脑不会……" | "在神经科学中，对应的机制是……，但实现方式根本不同：……" |

Analogies reduce the barrier to understanding. They must not *replace* the technical explanation.

---

## Toy Problem Backbone (B19)

All chapters maintain two core toy problems as the algorithmic backbone:

1. **Online linear regression / associative recall** — the key-value memory story
2. **Key-value retrieval / MQAR / long-context retrieval** — the needle-in-haystack story

Neuroscience analogies serve as the *intuition layer* on top of these toy problems, not as replacements.

---

## Change Log

| Version | Date | Change |
|---------|------|--------|
| 2.0 | 2026-04-03 | Full rewrite incorporating B11–B26 principles |
| 1.0 | — | (Did not exist; informal conventions only) |
