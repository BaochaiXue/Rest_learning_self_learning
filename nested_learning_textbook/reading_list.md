# 阅读清单 (Reading List)

为配合本教材的学习与讲授，我们将相关文献划分为三大类。每篇文献在 `papers/` 文件夹下游有更详尽的单篇讲义，在此仅做鸟瞰式汇总。

## 1. 核心必读（正文主干）
这些论文是支撑本书叙事结构的关键里程碑。**强烈建议读者在阅读对应章节时精读。**

* **Test-Time Training with Self-Supervision... (Sun et al., 2020)**
  * **一句话摘要**：在遇到分布偏移的测试阶段，利用自监督信号现场做一轮即时的梯度下降微调模型。
  * **重要性**：开启了狭义 TTT (Test-Time Training 2020) 时代的概念宗师。
  * **归属章节**：第 2 章、第 3 章。

* **Learning to (Learn at Test Time) (Sun et al., 2023)**
  * **一句话摘要**：把模型的前向传播改造为一个内部嵌套的最小化优化过程（自回归的隐状态本质是不断拟合新输入的内部学习器）。
  * **重要性**：标志着 TTT 从“外挂型（利用反向传播微调权重）”转向“内在架构设计层面的新型 RNN”。
  * **归属章节**：第 7 章。

* **Linear Transformers Are Secretly Fast Weight Programmers (Schlag et al., 2021)**
  * **一句话摘要**：严谨地在数学上证明了线性注意力（Linear Attention）等同于 1990 年代提出的“快权重（Fast Weights）”联想记忆。
  * **重要性**：是连接旧体系与新组件、揭示注意力深层本质的最美论文之一。
  * **归属章节**：第 4 章、第 5 章。

* **Transformers learn in-context by gradient descent (von Oswald et al., 2022)**
  * **一句话摘要**：提出将 In-Context Learning 视为在 Transformer 的前向传递过程中显式地执行了梯度下降算法。
  * **重要性**：打破了“权重是学来的，隐状态是计算的”二元边界，正式将 ICL 与优化等同。
  * **归属章节**：第 6 章。

* **Titans: Learning to Memorize at Test Time (Behrouz et al., 2025)**
  * **一句话摘要**：设计了一种新型长时限神经网络记忆模块，并在推理阶段学习将新内容持续写出（记住）。
  * **重要性**：在注意力之外引入“持续可变的辅助网络作为动态库”，提供了目前时间多尺度问题的 SOTA 架构视角。
  * **归属章节**：第 9 章。

## 2. 作者/备课必读（教师应当吃透）
对于需要进一步深究这些主张“为什么能统御复杂架构”的读者及教师，需精读。

* **Nested Learning: The Illusion of Deep Learning Architectures (Behrouz et al., 2025)**
  * **一句话摘要**：提出一切已知的深度架构与底层优化器（SGD、Adam 等）本质上都仅仅是联想记忆的某个层级压缩，是一个嵌套的多级优化系统。
  * **重要性**：终局理论框架，可能重塑对 Deep Learning 本质的认知。
  * **归属章节**：第 10 章、第 11 章。

* **Test-time regression: a unifying framework... (Xiong et al., 2025)**
  * **一句话摘要**：用在线最小二乘回归的视角解构并统一了众多高效序列模型架构。
  * **归属章节**：第 10 章。

* **Model-Agnostic Meta-Learning for Fast Adaptation (Finn et al., 2017)**
  * **一句话摘要**：大名鼎鼎的 MAML，提出为了未来的微调而预先学习良好权重的算法。
  * **归属章节**：第 3 章。

## 3. 选读（扩展视野）
这类论文可以跳读或略读，通常用于扩宽对早年历史或者纯工程视角的理解。

* **Attention Is All You Need (Vaswani et al., 2017)**
  * **摘要**：Transformer 鼻祖。
* **Learning to learn by gradient descent by gradient descent (Andrychowicz et al., 2016)**
  * **摘要**：元学习历史先验。
* **Transformers Learn to Achieve Second-Order Convergence Rates... (Ahn et al., 2023)**
  * **摘要**：论证大模型学到了比一阶梯度下降更高阶、更稳的在线优化算法，数学推导较多。
