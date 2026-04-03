# 关于 Learning Theory 涵盖范围的说明 

作为一本系统探讨 Inference-Time Learning 与相关拓展架构的教材，我们有意识地**舍弃了**全套传统统计学习理论（Statistical Learning Theory），包括但不限于 PAC 学习框架、VC 维（Vapnik-Chervonenkis Dimension）以及 Rademacher 复杂度等。 

## 为什么做出这种取舍？

1. **核心议题不同**
   传统的学习理论主要研究“泛化问题”的基本面，即：在给定的假设空间（Hypothesis Space）中，当训练误差很低时，测试误差的上界可以通过样本量和模型复杂度进行控制。
   然而，本书探讨的**“推理期学习 (Inference-Time Learning)”**核心关心的并不是静态参数的泛化边界，而是**当推理期的输入分布不再服从独立同分布 (i.i.d) 假设**（如发生了分布偏移），或者**当序列本身就蕴含了需要现场摄取的规则**时，模型内部如何通过状态转移或显式梯度更新来进行“二次学习”的过程。

2. **语言工具的适配性**
   描述 Inference-Time Learning，当前最有效的科学语言工具并非 PAC 框架，而是以下四个直觉工具的组合：
   - **双层优化 (Bilevel Optimization)**：用于刻画带有“学会学习 (Learn to Learn)”性质的层次化更新架构。
   - **在线更新与遗憾界 (Online Update & Regret Intuition)**：因为推理序列通常单向到来且不能回头（Causal），利用 Regret 的思路更能直观反映隐状态微型学习器的迭代性能。
   - **闭式解回归分析 (Closed-Form Regression)**：以在线岭回归（Online Ridge Regression）为模型，能完美对应 Linear Attention 等架构的行为。
   - **分布偏移直觉 (Distribution Shift)**：简单解释为何静态网络会在推断时失败，为 TTT 奠定动机。

## 本土化 Learning Theory
本书不是在否认传统 Learning Theory 的价值，而是做出了“**为当前主题精简服务**”的妥协。我们构建的是一个“动态、流式、嵌套”的模型世界观。如果在其中塞入深奥的静态泛化界证明，会打断读者的思路，阻碍主线的推进体验。所有的“学习理论直觉”，都会在全书两个最简化的 Toy Problems（在线线性回归与联想记忆键值检索）中被生动、具象地展现出来，让本科生真正做到“能算、能懂、能用”。
