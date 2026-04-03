# AGENTS.md — 导航地图

本文件是所有 agent 或贡献者的**入口**。  
先读这里，不要跳过直接改文件。

## 本项目是什么

一个 harness 管理的 LaTeX-canonical 本科教材，主题：**Inference-Time Learning**  
叙事主线：TTT (2020) → 元学习 → fast weights → attention → ICL → TTT layers → Titans → Nested Learning

**正式书稿（canonical）**：`book/`（LaTeX，xelatex + ctexbook）  
**v0 草稿（legacy/seed material）**：`manuscript/`（Markdown，不能视为 canonical）  
**系统记录（system of record）**：`docs/`（所有设计决策、计划、QA）  
**文献语料**：`papers/`（每篇一个 folder，含 `merged_paper.tex`）  
**清单（ground truth）**：`manifests/papers_manifest.csv`

## 开始任何任务前，必须先读

1. `docs/index.md` — docs 地图
2. `docs/project_state/current_repo_audit.md` — 真实现状
3. `docs/handoffs/latest_handoff.md` — 上一次进度
4. `docs/exec-plans/active/` — 当前计划
5. `docs/quality/qa_rubric.md` — 质量标准

## 固定执行规则

- **绝对不写绝对路径**（`/Users/...`）。所有路径一律 repo-relative。
- **绝对不覆盖 `manuscript/*.md`** — 这些是 v0 legacy，保留为 source material。
- **每次实质性工作后必须更新 `docs/handoffs/latest_handoff.md`**。
- **canonical manuscript 是 `book/`** — 所有新章节内容进入 `book/chapters/*.tex`。
- **manifest 是 ground truth** — `papers_manifest.csv` 说缺就是缺。
- **完成 phase 前必须能跑通 `make check`**（或等价脚本）。

## 关键文件位置

| 用途 | 路径（相对于 nested_learning_textbook/） |
|---|---|
| Docs 索引 | `docs/index.md` |
| 书稿入口 | `book/main.tex` |
| 清单 | `manifests/papers_manifest.csv` |
| 参考文献 | `book/bibliography/library.bib` |
| 审计报告 | `docs/project_state/current_repo_audit.md` |
| 卫生报告 | `docs/generated/repo_hygiene_report.md` |
| 最新 handoff | `docs/handoffs/latest_handoff.md` |
| QA rubric | `docs/quality/qa_rubric.md` |
| 学术诚实政策 | `docs/quality/claim_honesty_policy.md` |
| 语料审计 | `docs/generated/corpus_audit.md` |

## 脚本入口

```bash
# 从 nested_learning_textbook/ 目录执行：
python3 scripts/validate_manifest.py       # 校验 manifest
python3 scripts/check_absolute_paths.py    # 扫描绝对路径
python3 scripts/check_book_structure.py    # 验证 LaTeX 章节结构
python3 scripts/corpus_pipeline.py         # 增量文献管线

# 从 book/ 目录编译书稿：
latexmk -xelatex main.tex

# 或从 nested_learning_textbook/ 用 Makefile：
make audit    # 跑所有检查脚本
make corpus   # 跑文献管线
make book     # 编译 LaTeX
make check    # 全部检查
make clean    # 清理构建产物
```

## 学术诚实政策

详见 `docs/quality/claim_honesty_policy.md`。简版：
- 机制级共识 = 可作为事实陈述
- 解释框架（ICL = GD，NL 作为统一视角）= 必须注明"一种视角"/"研究议程"
- 推测性主张 = 绝不能写成定理
