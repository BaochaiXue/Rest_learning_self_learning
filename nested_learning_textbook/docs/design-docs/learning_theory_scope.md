# Why We Skip Traditional Learning Theory
**Canonical location for learning_theory_scope.md content**

## The Question
Why does this textbook skip PAC learning, VC dimension, and Rademacher complexity?

## The Answer

### 1. Wrong Framing for Test-Time Learning
Classical SLT analyzes training-time sample complexity.
This book is about inference-time adaptation — a fundamentally different question that SLT does not directly address.

### 2. Our Math is Online/Adaptive, Not Batch/Statistical
The relevant theory is online learning (regret, adversarial bounds) and
bilevel optimization (inner/outer loop convergence), not PAC generalization bounds.

### 3. Pedagogical Efficiency
Adding PAC theory would require 2-3 extra chapters with diminishing returns
for the target reader (junior CS undergrads with PyTorch experience).

## What We Use Instead
- Online learning: regret bounds (brief intuition in Appendix A)
- Bilevel optimization: inner/outer loop convergence (Chapter 3)
- Matrix analysis: outer product, Sherman-Morrison (Appendix A)
