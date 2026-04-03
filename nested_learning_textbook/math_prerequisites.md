# 前置知识清单 (Math Prerequisites)

本书遵照**“最低必要原则”**，不进行为满足数学严谨性而进行的炫技式推导。以下是进入本书核心内容需要掌握的数学地图。

## 1. 线性代数 (Linear Algebra)
- **为什么需要**：在讲解 Attention、Fast Weights 以及 Test-Time Regression 时，大量运算基于矩阵的乘法、外积（Outer Product）。
- **需要学到什么程度**：
  - 了解向量内积、矩阵加减乘法。
  - **核心点**：必须理解“矩阵外积”（$u v^T$）是一种存储关联（associative relation）的神奇方式（这将在讲快权重和联想记忆时起决定性作用）。
  - 知道什么是半正定矩阵以及特征值分解（对理解海森矩阵/优化有微小帮助）。

## 2. 多元微积分 (Multivariable Calculus)
- **为什么需要**：优化也就是求导，神经网络的基础引擎是梯度下降。
- **需要学到什么程度**：
  - 会求多变量函数的偏导数和梯度（Gradient）。
  - 理解链式法则（Chain Rule）。
  - 知道梯度是指向函数增长最快方向的向量。知道海森矩阵（Hessian）包含曲率信息就够了。能够看懂泰勒展开式的一阶/二阶近似。

## 3. 概率统计 (Probability & Statistics)
- **为什么需要**：一切模型都是在拟合分布；分布偏移（Distribution Shift）是 TTT (2020) 能够生效的前提。
- **需要学到什么程度**：
  - 知道期望（Expectation）、方差（Variance）。
  - 理解什么是联合分布 $P(X, Y)$ 和边缘/条件分布。
  - 理解什么是经验风险（Empirical Risk），即我们在训练集上优化的那个平均 Loss。

## 4. 优化 (Optimization)
- **为什么需要**：Inference-time learning 的本质就是在 inference 阶段延续了一定形式的优化过程。
- **需要学到什么程度**：
  - 完全掌握梯度下降（Gradient Descent）及其更新公式 $\theta = \theta - \eta \nabla L$。
  - 听说过动量（Momentum）和预处理（Preconditioning，比如简单理解“给梯度乘个矩阵改变方向”）。
  - 了解什么是局部极小值和全局极小值。特别是岭回归（Ridge Regression）的闭式解公式形式。

## 5. 最小 Learning Theory / Regret 直觉
- **为什么需要**：我们需要一套语言来评价“测试时学习到底有没有用”，但不希望陷入繁琐的 PAC 学习界。
- **需要学到什么程度**：
  - 不要求会证明 VC Bound 或 Rademacher 复杂度。
  - **Online Learning 直觉**：理解什么是数据流（流式数据不断到来），什么是 Regret（“我现在的在线累计损失，与如果我一开始就知道最优模型所能达到的损失之差”）。我们只要这个“比大小”的思维。
  - **Bilevel Optimization（双层优化）直觉**：只要能看懂 $\min_{\theta} L_{out}(\theta^*)$ s.t. $\theta^* = \arg\min L_{in}(\theta, \phi)$ 这种包含内外圈优化的结构即可，它对理解 Meta-Learning 极其重要。
  
> **推荐学习路径**：
> 以上内容大部分本科生在一年级都已学过。如果你忘了外积矩阵更新和在线学习直觉，不用担心，本书将在**第 3 章（双层优化）**与**第 10 章（在线回归视角）**通过具体的 Toy Problem 直接温习这部分直觉，不会作为生硬的拦路虎出现。
