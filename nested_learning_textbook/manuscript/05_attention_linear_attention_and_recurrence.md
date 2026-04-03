# 第 5 章：Attention、Linear Attention 与递推视角

## 本章想回答什么问题？
Transformer 最核心的自注意力机制 (Self-Attention) 看上去非常消耗内存（$O(N^2)$ 的开销），我们能不能把它写成时间上自给自足的一步步累加关系，即“把它看成一种 RNN”？如果可以，它背后与第四章的关联记忆有什么不可告人的联系？

## 从普通注意力到线性核心 (Toy Problem)
回忆标准注意力机制中用于寻找关联的重要部分及 Softmax 函数的影响：
$$y_i = \text{softmax}(q_i K^T) V$$
因为 Softmax 中不可分离的 $e^{q_i k_j}$ 项，此时对于新进来的第 $i$ 个词 $q_i$，模型必须翻开前面所有时间步留存的实打实的高维矩阵 $K$ 和 $V$ （叫做法术：KV-Cache）。

如果我们剥离这层 Softmax 的不可分离性，简单地（或者通过核函数映射 $\phi(\cdot)$ ）将它写成点乘，即**线性注意力 (Linear Attention)**：
$$y_i = \sum_{j \le i} (\phi(q_i) \phi(k_j)^T) v_j$$

## 矩阵乘法的结合律魔术主公式
如果我们对点乘注意力稍微用一个小小的矩阵结合律转写，奇迹发生了（请把上式的 $a(b^Tc)$ 抽出标量重新组合成 $(ac^T) \times b$）：
$$y_i = \phi(q_i) \left[ \sum_{j \le i} \phi(k_j) v_j^T \right]$$

如果我们将括号内的矩阵大累加重命名为一个随时间累积并滚动的维护变量 $W_i$：
$$W_{i} = W_{i-1} + \phi(k_i) v_i^T$$
$$y_i = \phi(q_i) W_i$$

**这直接和第 4 章快权重（Fast Weights）联想内存更新方程一模一样！**
这揭示了一项重大的机制共识：**线性注意力层本质上就是利用每一个新的 token 生成外积去即时更新一个隐式的记忆矩阵库 $W$，然后又把它作为一个生成参数来被查询！**

## 代表论文
- Katharopoulos, Angelos, et al. *"Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention."* ICML 2020. 这是首次明确推导出这套加权结合律解构并加速推理的经典文章。
- Schlag, Imanol, et al. *"Linear Transformers Are Secretly Fast Weight Programmers."* ICML 2021. 首次明确将二者的桥梁完全建立并提出等效理论。

## 机制性共识与认知局限
本书在此强调：这套关联转换虽然在数学形式上无可挑剔极其优美，且确凿存在于模型当中。然而具有 Softmax 的非线性注意力虽然可被泰勒展开为类似的矩阵生成，但其中的缩放分母与非线性竞争（例如防止一个大向量覆盖一切）占据了模型容量不可割舍的作用（因此只用线性注意力跑不到极品泛化性能）。但这作为了解“推理阶段学习”的窗口已极为强悍。

## 可做的 Lab
写一个极小的 PyTorch 脚本（20 行）：首先生成一段长为 1024 的随机张量代表 $(Q, K, V)$，通过去掉 Softmax 的 `y = x @ K.T @ V` （注意此处是批处理版本）计算结果并打时间戳。接着实现它的递归累加版本 `W += k @ v.T`。比较二者的输出张量重合度（应极大）和运行速度。

## 常见误解
- **误解**：只有 Linear Transformer 才是更新隐藏状态的 RNN 算法。
- **纠正**：所有的 Transformer （即使带了非线性 Softmax）也可以被看做隐式构建了一个越来越庞大的关联缓存池。

## 练习题
5.1 利用结合律对公式重组，推断每次执行累计的 $W$ 矩阵所占据的空间维数，与传统保存 $K, V$ 会随着序列长度 $N$ 变大有何显著不同的优势？
