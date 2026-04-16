# Nested Learning Claim Audit

| Claim / Proof Unit | Status | Anchor | Audit Note |
|---|---|---|---|
| Linear attention recurrence = one-step optimization on dot-product objective | exact | `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Methods.tex:77-88` | Local algebraic equivalence is solid. |
| Softmax attention = non-parametric weighted regression solution | exact | `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Methods.tex:593-602` | Standard Nadaraya-Watson style reformulation. |
| Delta-rule memory = SGD on `L2` regression + retention | exact | `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Methods.tex:611-615` | Clean recurrence-level equivalence. |
| Backprop / GD = associative-memory proximal rewrite | reformulation | `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Methods.tex:303-316` | Rewrite is correct, but it is a view, not a new theorem about learning itself. |
| Momentum = associative-memory module | reformulation | `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Methods.tex:328-353` | Acceptable as a constructed internal objective. |
| Adam is the optimal associative memory | too strong | `papers/nested_learning_the_illusion_of_deep_learning_architectures/merged_paper.tex:1648-1670` | Only true relative to the paper's bespoke element-wise objective; derivation is approximate and omits standard Adam details. |
| DGD closed form | mostly right, proof sloppy | `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Methods.tex:534-543`; `.../merged_paper.tex:1689-1717` | Main update is plausible under normalized inputs; appendix algebra is inconsistent as written. |
| Muon recovered by one-step GD on written objective | incorrect as written | `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Methods.tex:383-392` | The shown gradient step contains a term absent from the displayed objective. |
| All model components are associative-memory systems | interpretive overreach | `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Methods.tex:17-30` | Useful worldview, not mechanism-level consensus. |
| Pre-training is in-context learning | interpretive overreach | `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Methods.tex:723-727` | Follows only after broadening the meaning of context. |
| ICL is not emergent | interpretive overreach | `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Methods.tex:703-705` | Not proved against the original empirical emergence question. |
| Modern architectures are an illusion / uniform feedforward layers | interpretive overreach | `papers/nested_learning_the_illusion_of_deep_learning_architectures/MainText/Intro.tex:87-92`; `.../Methods.tex:651-668` | This is the paper's research agenda, not a settled theorem. |
