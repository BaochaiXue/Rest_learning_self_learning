# 全书章节地图与核心设计 (Chapter Map)

本书采用模块化、小步快跑的组织结构。每一章由**一个核心问题**驱动，携带一个不可缺少的**主公式**和**贯穿案例 (Toy Problem)**。

## 第 0 章：前言与指南
- **核心问题**：什么是推理阶段的学习？我们要去哪里？
- **学习目标**：定标，了解全书不打算卷入庞杂的 LLM 调参术，而是提炼机制。
- **玩具实验**：无。

## 第 1 章：术语与地图
- **核心问题**：当我们在说“更新”或“学习”时，不同社群到底在指什么？
- **主公式**：$f_\theta(x_t; s_t) \rightarrow y_t$, 分别追踪 $\theta$ (持久参数) 和 $s_t$ (动态状态)。
- **核心论文**：综合。
- **玩具实验**：纸笔梳理 RNN、Transformer 变量时间尺度。

## 第 2 章：为什么模型能在测试时学习？
- **核心问题**：模型上线后，遇到未知情况分布偏移，只能重新训练吗？
- **主要公式**：$\min_{\theta} L_{\text{test self-sup}}(\theta; x_{\text{test}})$，经典的 TTT 目标函数。
- **核心论文**：*Test-Time Training with Self-Supervision* (2020), *Dynamic Evaluation*。
- **玩具实验**：**分布偏移 Toy Problem**，在带有截距项变化的单变量回归上测试手动梯度下降。

## 第 3 章：双层优化与元学习
- **核心问题**：如何优雅地把学习微调的过程“自动化”并让模型为其做好准备？
- **主要公式**：$\min_\theta \sum L_{\text{val}}(\theta - \eta \nabla L_{\text{train}}(\theta))$ (MAML 核心更新律)。
- **核心论文**：*MAML* (2017)。
- **玩具实验**：MAML 拟合正弦波 (Sinusoid Regression)，区分 Inner/Outer loop。

## 第 4 章：快权重、外部记忆与时间尺度
- **核心问题**：不用反向传播，仅凭网络的向前推演，能否改变一个矩阵实现“记忆的更新”？
- **主要公式**：$W_{t+1} = \lambda W_t + v_t k_t^T$ (外积法则与遗忘因子)。
- **核心论文**：*HyperNetworks* (2016), *Fast Weights to Attend* (2016)。
- **玩具实验**：编写一个小前馈网络输出另一个前馈网络的权重（极为基础的 HyperNet）。

## 第 5 章：Attention、Linear Attention 与递推视角
- **核心问题**：为什么 Transformer 可以被视作某种 RNN，以及线性注意力与快权重的秘密联系何在？
- **主要公式**：$y_i = \sum_{j} (q_i^T k_j) v_j = q_i^T \sum_{j} (k_j v_j^T)$。
- **核心论文**：*Transformers are RNNs*, *Linear Transformers Are Secretly Fast Weight Programmers*。
- **玩具实验**：**Key-Value 联想匹配 Toy Problem**，手写由 $O(N^2)$ 改为递推求和的自回归注意力函数。

## 第 6 章：ICL 到底是不是学习？
- **核心问题**：当我们给大模型提供 Few-shot examples 时，它是怎样产生输出改变的？它在进行梯度下降吗？
- **主要公式**：$\theta^{(k+1)} = \theta^{(k)} - \eta X^T (X \theta^{(k)} - Y)$ 等价于线性注意力层。
- **核心论文**：*Transformers learn in-context by gradient descent*, *Induction Heads*。
- **玩具实验**：**在线线性回归 Toy Problem**，给出一个 2 层 Linear Attention Transformer 并可视化其与普通最小二乘回归的预测偏离度。

## 第 7 章：Learning to (Learn at Test Time)
- **核心问题**：如果把模型隐藏状态看做参数，我们能否把架构设计转化为设计一种优化器？
- **主要公式**：$s_{t} = s_{t-1} - \eta \nabla_s \ell(s_{t-1}; x_t, y_t)$（隐藏状态作为学习器本体）。
- **核心论文**：*Learning to (Learn at Test Time)* (2023)。
- **玩具实验**：复现最简单基于一维标量函数的“模型内部模拟梯度流”。

## 第 8 章：TTT layers：隐藏状态就是学习器
- **核心问题**：如何基于内嵌学习器的视角，创造出具有更强表达能力的 RNN 层机制（例如超越 Mamba）？
- **核心论文**：*RNNs with Expressive Hidden States* (2024), *Test-Time Training Done Right* (2025)。
- **玩具实验**：搭建一个最小化的 TTT-MLP 层，对比由于隐变量变成了“含有权重信息的矩阵”而增加的算力与效果提升。

## 第 9 章：Titans 与多时间尺度记忆系统
- **核心问题**：短时记忆 (Attention) 和长期微调之间，是否存在兼顾推理速度且带有永久遗存能力的结构？
- **主公式**：Surprise 梯度法则计算记忆更新 $\Delta M$ 以及对偶的门控聚合。
- **核心论文**：*Titans: Learning to Memorize at Test Time* (2025)。
- **玩具实验**：长草堆找针（Needle in a haystack），给一个由 Short-cut 和 Neural Memory 并行的微缩 Titan 结构下发千级数据长度记忆任务。

## 第 10 章：统一视角：在线回归与相关性连接
- **核心问题**：到目前为止，我们能否用单一甚至更加精练的视角把 Fast-weights、Mamba、TTT-Layers 以及联想记忆结合在一起？
- **主公式**：Sherman-Morrison 逆矩阵更新公式 / 在线共方差矩阵。
- **核心论文**：*Test-time regression*, *It’s All Connected*。
- **玩具实验**：利用 OLS（普通最小二乘）推导复现 TTT-Linear Layer 特性。

## 第 11 章：Nested Learning (终局视角)
- **核心问题**：如果一切显式的神经网络架构都是某一层联想记忆或者优化器，我们的下一代 AI 的本质是什么？
- **核心论文**：*Nested Learning: The Illusion of Deep Learning Architectures* (2025)。
- **玩具实验**：对深度学习不同演进概念与 Nested Learning 抽象映射机制的填字游戏与讨论。

## 附录 12 / 13：数学速查与实验指南
- 汇总前置矩阵微积分；针对每章的小型实验给予基于 PyTorch 的代码模板骨架。
