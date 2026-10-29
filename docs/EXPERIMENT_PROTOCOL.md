# Experimental protocol — preliminary / no results yet

## Goal
Measure the effect of memory hop count on multi-fact QA accuracy under varying distractor counts.

## Dataset and leakage prevention
- Tasks: English QA1, QA2, QA3, configurations `en-valid-10k-qa1/2/3`.
- Use dataset-provided train/validation/test partitions; test is never used for model selection.
- Each source record may contain **multiple questions**. Flatten each question with **preceding** story context only. Preserve source-story ID, source split, answer and supporting sentence IDs.
- Build vocab/label space from training data only (including an `<unk>` policy). Ensure no overlap due to accidental re-splitting or copy leakage.
- Supporting IDs are diagnostic metadata, **never** model inputs during training or inference.

## Models
- Baseline: story+question bag-of-words classifier.
- MemN2N: 1-hop and 3-hop configurations; common dimensions, optimizer, training examples, and stopping policy.
- Plan: embedding dimension 32 or 64; baseline and training implementation belong to later milestones.

## Distractor injection
- Evaluation conditions: 0, 5, 10, 20 **added** sentences (random/unrelated in core study).
- Inject only into a *copy* of the held-out story for each question, preserving causal story semantics and gold answer.
- Ensure model's memory capacity fits all original plus added facts; **never silently truncate supporting facts**.
- Hold distractor generation seeds and positions consistent across model comparisons.
- Optional extension: entity-overlap distractors (separate experimental variable; do not conflate with count).

## Evaluation
- Exact-match answer accuracy by task, hop count and distractor condition.
- Compare performance to baseline and to the same model on clean test examples (accuracy delta).
- Record configurations, random seed, code commit, input digest, epochs and hardware for each run.
- Inspect representative successes/failures and attention maps; attention weights **do not prove** a logical reasoning chain.
- If resources permit, use repeated seeds and report mean/variability; don't hide unstable runs.

## Study limitations
bAbI is synthetic. Results should not be generalized to real-world language understanding without additional evaluation.
