# Nested Learning: The Illusion of Deep Learning Architectures

## Citation

- Ali Behrouz, Zeman Li, Praneeth Kacham, Majid Daliri, Yuan Deng, Peilin Zhong, Meisam Razaviyayn, Vahab Mirrokni. 2025. *Nested Learning: The Illusion of Deep Learning Architectures*. arXiv:2512.24695.

## 在本教材中的角色

- 这是第 11 章 `book/chapters/11_nested_learning.tex` 的主文献。
- 它的真正贡献不是“证明万物本质相同”，而是提供一个把优化器、注意力、RNN 记忆、meta-learning 和 test-time adaptation 放进同一坐标系的统一视角。

## Core Problem

- 论文想回答的问题是：
  - 能否把现代模型的“架构”重新表述为多个时间尺度上的嵌套优化系统
  - 能否把优化器、记忆模块、attention、RNN、test-time adaptation 放到同一个 associative-memory / optimization 语言里
  - 这样做是否能导出新的架构和优化器设计

## Method Summary

- 先定义 associative memory 为“把 key 映到 value 的算子”，并把很多已知更新写成“目标函数 + 更新规则”。
- 再用 update frequency 给不同更新过程分层，得到 nested system / nested system of associative memories。
- 然后把若干已知对象放进这个形式化里：
  - linear attention / Hebbian memory
  - delta-rule memory
  - softmax attention 作为 non-parametric regression solution
  - backprop / momentum / Adam / AdaGrad 的 associative-memory 重写
- 在此基础上提出新的设计：
  - DGD
  - Delta Momentum / Deep Momentum
  - CMS
  - self-referential Titans / HOPE

## Datasets / Tasks

- Continual learning / class incremental:
  - CLINC
  - Banking
  - DBpedia
- Long-context / in-context understanding:
  - MK-NIAH (RULER)
  - LongHealth
  - QASPER
  - BABILong
- Language modeling / reasoning:
  - WikiText, LAMBADA, PIQA, HellaSwag, WinoGrande, ARC-e, ARC-c, SIQA, BoolQ
- Retrieval / synthetic:
  - SWDE, NQ, DROP, FDA, SQuAD, TQA
  - MAD
- Formal-language tasks:
  - follow `irie2023practical`

## Strongest Results

- `HOPE` / `model` 在文中报告为：
  - 在 class-incremental continual-learning baselines 上最好
  - 在 NIAH / long-context attention-free baselines 上最好
  - 在 BABILong 上维持到更长上下文
  - 在 language modeling + commonsense 平均指标上优于 attention-free baselines
  - 在 recall tasks 上优于其他 attention-free baselines，但仍落后 Transformer
- 证据锚点：
  - `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Experiments.tex:37-45`
  - `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Experiments.tex:89-103`
  - `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Experiments.tex:168-175`
  - `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Experiments.tex:184-233`

## Theory Audit

### 哪些推导是硬的

- linear attention recurrence 可以严格写成一个 dot-product objective 的一步优化：
  - `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Methods.tex:77-88`
- softmax attention 作为 Nadaraya-Watson / weighted regression 视角是成立的：
  - `.../Methods.tex:593-602`
- delta-rule memory 写成 `L2` regression + retention 是成立的：
  - `.../Methods.tex:611-615`
- backprop / GD 写成 proximal step，映射 layer input 到 local error，这个重写本身是成立的：
  - `.../Methods.tex:303-316`
  - `.../Methods.tex:525-567`

### 哪些是“重写成立，但结论不能说太满”

- momentum / Adam / AdaGrad 被写成 associative-memory module，这更像“构造一个目标函数来解释更新式”，不是传统意义上的新定理：
  - `.../Methods.tex:328-353`
  - `.../merged_paper.tex:1641-1687`
- DGD 的 closed-form 直觉是对的，但它成立依赖 normalized-input 假设，而且 appendix 写法不够干净：
  - `.../Methods.tex:534-543`
  - `.../merged_paper.tex:1689-1717`

### 哪些话说过头了

- “all elements ... are associative memory systems”
- “Transformers are in fact linear layers with different frequency updates”
- “a neural learning module is a uniform model”
- “ICL is not emergent”
- “pre-training is in-context learning”
- “all modern architectures are uniform feedforward layers”
- “CMS can circle back knowledge and hardly forget important knowledge”

这些表述更适合标成：

- 一种统一视角
- 一种解释框架
- 一种研究议程

而不是机制级共识。

### 哪些证明本身有问题

- Muon 那段“由目标函数推出更新式”不成立，因为写出来的 objective 不含 `||o - g||^2` 之类的 closeness term，但梯度步里却出现了 `o_i - g_t`：
  - `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Methods.tex:383-392`
- DGD appendix 的一阶条件和 Sherman-Morrison 展开有系数 / 符号不一致：
  - `papers/nested_learning_the_illusion_of_deep_learning_architectures/merged_paper.tex:1694-1717`

## Limitations / Failure Modes

- 论文最强的是“局部机制统一”，最弱的是“全局本体论结论”。
- 很多大结论来自定义扩张，而不是来自新的不可回避的证明。
- “optimal” 一词在 Adam 那里容易误导，因为它只对论文自造的目标成立。
- 证明部分偶有写作级错误，说明教材在引用时应该把“公式可核查”与“世界观主张”分层。

## Evidence Anchors

- Theory core:
  - `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Methods.tex`
- Strong worldview claims:
  - `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Intro.tex`
  - `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Conclusion.tex`
- Appendix derivations:
  - `papers/nested_learning_the_illusion_of_deep_learning_architectures/merged_paper.tex:1641-1717`
- Textbook claim boundary:
  - `docs/quality/claim_honesty_policy.md`
