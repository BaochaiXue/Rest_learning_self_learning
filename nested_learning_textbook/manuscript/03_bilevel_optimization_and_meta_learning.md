# 第 3 章：双层优化与元学习的语法

## 本章想回答什么问题？
当我们手动在推断阶段做梯度下降时，总是调不好学习率等超参数。能不能在训练阶段就“专门训练模型，好让它在推断时候能更好地被微调更新”？

## 直觉解释
双层优化 (Bilevel Optimization) 指的是在一个大优化问题中，其变量往往受制于内部较小优化问题的闭式解。这就好比公司的领导（大圈，Outer Loop）设置考核目标（模型初始参数），但员工（内圈，Inner Loop）根据当下客户反馈（测试集数据）进行局部优化适应。如果考核目标定得很差，员工怎么自适应都救不回来；如果在训练时，领导设置的初始点非常好，员工遇到任何客户只要稍微挪动半步就能全盘胜利。
元学习（Meta-Learning，也就是 Learn to Learn）的核心正源于此。

## 最小例子与数学形式化
我们将模型预训练权重视为 $\theta$。当推断时，针对小数据任务 $\tau_i$ 进行一步梯度更新，产生任务相关的特殊权重 $\phi_i$：

$$\phi_i = \theta - \eta_{inner} \nabla_\theta L_{\tau_i}^{\text{train}}(\theta)$$

这叫 **Inner Loop (内循环)**，它在“模拟推断阶段现场更新的过程”。
然后我们在一个更泛的预训练评估集上优化这个“经过变化后的新权重”，并以此求梯度更新初始状态的大 $\theta$：

$$\min_\theta \sum_{\tau_i} L_{\tau_i}^{\text{val}}(\phi_i) = \min_\theta \sum_{\tau_i} L_{\tau_i}^{\text{val}}(\theta - \eta_{inner} \nabla_\theta L_{\tau_i}^{\text{train}}(\theta))$$

这就是 **Outer Loop (外循环)**，其最终得到的 $\theta$ 即是 “MAML 极力寻找的最佳适应点”。

## 代表论文
- Finn, Chelsea, et al. *"Model-agnostic meta-learning for fast adaptation of deep networks (MAML)."* ICML 2017.
- Andrychowicz, Marcin, et al. *"Learning to learn by gradient descent by gradient descent."* NIPS 2016. 此文用小神经网络代替了上面的 $-\eta \nabla$，做出了学会优化器的突破。

## 和前后章节的关系
没有 MAML（2017）带来的这种 Inner-Outer 的形式化分析语言，我们后面的 Learning to (Learn at Test Time) 的内生结构设计就成了空中楼阁。Bilevel Optimization 是把静态网络动态化的数学“语法基础”。

## 可做的 Lab
**MAML on Sinusoid Regression**（小实验要求：用 100 行 PyTorch 代码实现）。任务：外层我们要训练一个能够迅速拟合不同频率正弦波的网络。内层赋予测试数据 5 个样本并做 1 步手工纯 Python 代码级别的 `weight -= lr * grad` 更新。这是元学习的入门级红宝书级实验。

## 常见误解
- **误解**：外圈也是针对训练集，内圈也是针对训练集。
- **纠正**：为了防止模型直接“背下面”内层训练集，计算外圈需要新的未见过的小样本验证集，即所谓的 Query Set，而内圈用的是 Support Set（这是元学习特有时态）。

## 练习题
3.1. 这个数学公式里，当我们计算外循环 $\nabla_\theta L_{val}(\phi)$ 时，是否需要计算关于梯度的梯度（Second-order derivative / Hessian）？为什么？
