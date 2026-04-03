# Corpus Audit Report
**Generated**: 2026-04-03  
**Source**: Automated scan of `papers/` against manifest seed definitions

## Summary

| Status | Count |
|---|---|
| `source_and_merged` (TeX + merged_paper.tex) | 22 |
| `pdf_only` (no public TeX source) | 1 |
| `missing` (no local folder) | 1 |
| **Total** | **24** |

## All 24 Papers

| # | Title | Slug | Status |
|---|---|---|---|
| 1 | Titans: Learning to Memorize at Test Time | `titans_...` | ✅ source_and_merged |
| 2 | Nested Learning: The Illusion... | `nested_learning_...` | ✅ source_and_merged |
| 3 | Test-time regression: a unifying framework... | `test_time_regression_...` | ✅ source_and_merged |
| 4 | It's All Connected... | `its_all_connected_...` | ✅ source_and_merged |
| 5 | Dynamic Evaluation of Neural Sequence Models | `dynamic_evaluation_...` | ✅ source_and_merged |
| 6 | Test-Time Training with Self-Supervision... | `test_time_training_with_...` | ✅ source_and_merged |
| 7 | Model-Agnostic Meta-Learning (MAML) | `model_agnostic_...` | ✅ source_and_merged |
| 8 | Optimization as a Model for Few-Shot Learning | `optimization_as_a_model_...` | ❌ missing |
| 9 | Learning to learn by GD by GD | `learning_to_learn_by_gradient_...` | ✅ source_and_merged |
| 10 | Meta-Learning with Memory-Augmented Networks | `meta_learning_with_...` | ⚠️ pdf_only |
| 11 | One-shot Learning with MANN (proxy) | `one_shot_learning_...` | ✅ source_and_merged |
| 12 | HyperNetworks | `hypernetworks` | ✅ source_and_merged |
| 13 | Using Fast Weights to Attend to the Recent Past | `using_fast_weights_...` | ✅ source_and_merged |
| 14 | Attention Is All You Need | `attention_is_all_you_need` | ✅ source_and_merged |
| 15 | Transformers are RNNs (Linear Attention) | `transformers_are_rnns_...` | ✅ source_and_merged |
| 16 | Linear Transformers Are Secretly Fast Weight Programmers | `linear_transformers_...` | ✅ source_and_merged |
| 17 | What Can Transformers Learn In-Context? | `what_can_transformers_...` | ✅ source_and_merged |
| 18 | In-context Learning and Induction Heads | `in_context_learning_...` | ✅ source_and_merged |
| 19 | Transformers learn in-context by GD | `transformers_learn_in_context_...` | ✅ source_and_merged |
| 20 | Transformers learn preconditioned GD | `transformers_learn_to_implement_...` | ✅ source_and_merged |
| 21 | Transformers Learn Second-Order Rates | `transformers_learn_to_achieve_...` | ✅ source_and_merged |
| 22 | Learning to (Learn at Test Time) | `learning_to_learn_at_test_time` | ✅ source_and_merged |
| 23 | Learning to (Learn at Test Time): RNNs with... | `learning_to_learn_at_test_time_rnns_...` | ✅ source_and_merged |
| 24 | Test-Time Training Done Right | `test_time_training_done_right` | ✅ source_and_merged |

## Notes on Non-Complete Entries

### Missing: Optimization as a Model for Few-Shot Learning
- Source: OpenReview paper (ICLR 2017)
- OpenReview does not expose LaTeX source
- PDF available at: https://openreview.net/pdf?id=rJY0-Kcll
- Action: Run `python3 scripts/corpus_pipeline.py --slug optimization_as_a_model_for_few_shot_learning --force-pdf`

### PDF-only: Meta-Learning with Memory-Augmented Neural Networks (Santoro 2016)
- Source: ICML 2016 proceedings paper — LaTeX source not publicly archived
- PDF available in `downloads/meta_learning_with_memory_augmented_neural_networks.pdf`
- Paper is covered by concept proxy: `one_shot_learning_with_memory_augmented_neural_networks` (arXiv source)

## Path Hygiene Notes

- `/home/kazuki/...` paths found in `papers/linear_transformers_are_secretly_fast_weight_programmers/main.tex` — these are **author's commented-out experiment paths in the original paper source**, not our paths. These are acceptable and expected; they are not our repo paths.
- All repo manifest paths are repo-relative. ✅
- `scripts/literature_engineer.py` contains absolute paths — this is the exempted legacy file. ✅
