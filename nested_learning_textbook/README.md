# Inference-Time Learning: From TTT to Nested Learning

本项目旨在构建一本适用于 CS 系本科生阅读的推理期学习（Inference-time learning）开源教材初稿。

## 项目结构
- `papers/`: 下载和结构化处理过的开源论文 TeX 源代码文件夹。每一篇论文如果有 TeX 源码，会自动生成合并了所有子文件的 `merged_paper.tex`，并且移除了注释与多余空行。
- `manifests/`: 文献清单（`papers_manifest.csv` / `papers_manifest.md`），登记了所有涉猎论文的下载状态、本地路径、是否有 tex 源码。
- `downloads/`: 下载过程的中间缓存或无法提取源码的纯 PDF 文件。
- `notes/papers/`: 按论文生成的简短笔记，概述每篇论文在教材主线中的角色与其核心价值。
- `scripts/`: 下载与处理流程的自动化脚本 `literature_engineer.py`，供复用和增量更新。
- `manuscript/`: 教材初稿的所有 Markdown 原文件（00-13 章节）。

## 论文整理状态
当前我们使用 `literature_engineer.py` 自动化提取了包含 Titans、Nested Learning、Test-time regression 等最新前沿，以及 TTT、MAML 等经典算法在内的 24 篇核心文献。对于能够访问 arXiv source 的论文，我们提取了全部 TeX 结构。由于没有采用重型的 Web Scraper，部分仅存于旧版开放会议平台（如带有 PDF 但无公开 source 的 ICLR 2017 早期版本）在 manifest 中标记为 pdf_only。

## 后续可扩展方向
1. **代码化**：将书里口语化描述的 toy problems（在线线性回归、key-value 记忆提取）转换为交互式 Jupyter Notebook，作为开源随书附件。
2. **可视化**：补充更多关于 Attention 与 Neural Memory 结构对比的插图。
3. **补充长上下文内容**：进一步深化 Infinite Context 或 Mamba 等关联技术的讨论。
