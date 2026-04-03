# Book Scope
**Canonical location for book_plan.md content**  
See root `nested_learning_textbook/book_plan.md` (legacy) for original.

## Title
《推断期学习：从 Test-Time Training 到 Nested Learning》

## Target Audience
CS undergraduates with basic PyTorch experience. No PAC/VC required.

## What This Book Is
A narrative-driven textbook tracing inference-time learning from distribution shift → TTT 2020 → meta-learning → fast weights → linear attention → ICL-as-GD → TTT Layers → Titans → Nested Learning.

## What This Book Is NOT
- Not a Transformer implementation guide
- Not a traditional SLT textbook (no PAC bounds)
- Not a promotion of Nested Learning as a proven framework

## Critical Two-Line Distinction
1. TTT 2020: gradient descent modifies persistent weights at test time (requires .backward())
2. TTT-Layer 2024: hidden state IS the learner; gradient steps are embedded in forward pass

## Narrative Thread
test-time update → bilevel/meta-learning → fast weights/memory → attention/linear-attention →
ICL as learning → Learning to (Learn at Test Time) → TTT layers → Titans → test-time regression → Nested Learning
