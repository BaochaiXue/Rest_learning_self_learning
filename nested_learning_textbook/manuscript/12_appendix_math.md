# 附录 A：最简化数学与符号补丁 (Math Appendix)

本篇包含部分未在正文中进行繁复展开的手工代数证明与极简映射指南，专门为喜欢在草稿纸上亲手划掉对应项公式读者准备。

## A.1 为什么带软最大值的多头注意力阻碍直接线性转化？
原 Attention: $Y = \text{Softmax}(QK^T)V$
$$ Softmax_{i, j}(QK^T) = \frac{\exp(q_i k_j^T)}{\sum_{l} \exp(q_i k_l^T)} $$
这个基于指数和分母全局关联累加的操作阻止了我们执行分离式的结合律操作。
在去除了全局指数核后变为简单的正系数线性内积相似核 $\phi(q)$，该操作才能得到释放：
$$ Y_i = \sum_{j} (\phi(q_i) \phi(k_j)^T) v_j $$
通过标量提出来结合即为在第 4、5 章中进行推算的关键。

## A.2 Outer Product 与矩阵微改的基础引理 (Sherman-Morrison Formula)
如果你想深入了解第 10 章在线回归为何能等效在低等级复杂度推倒更新 $S_t$，你要知道以下关于求秩为 1 且带有额外更新量矩阵逆的解法：
$$(A + u v^T)^{-1} = A^{-1} - \frac{A^{-1} u v^T A^{-1}}{1 + v^T A^{-1} u}$$
这个公式是很多推断阶段利用逆共分布项进行极快算法推进的神器基石！

## A.3 双层优化的偏导数链式延展简述
在外圈需要获取对于整体表现的梯度 $\nabla_\theta L_{out}(\theta - \eta \nabla L_{in})$ 时，你需要经过对内部迭代状态结果执行求导操作：
$$ \nabla_{\theta_{outer}} L(\theta_{inner}^*) \approx \nabla L_{val}(\phi) \cdot (I - \eta \nabla^2 L_{train}(\theta)) $$
这揭示了要极为完美完成 MAML 等元学习最快推演适配，你需要计算带有包含 Hessian 矩计算属性的高阶依赖操作（尽管通常采用截断式和一阶化近似）。
