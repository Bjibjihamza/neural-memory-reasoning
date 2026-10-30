# MemN2N — Steps H & I: bAbI Dataset, Evaluation & Experimental Design

**Project:** *When Does Neural Memory Fail? Investigating Distractors in Multi-Hop Reasoning*  
**Reference architecture:** Sukhbaatar et al., *End-To-End Memory Networks* (NeurIPS 2015)  
**Status:** Research protocol / planned experiments — **no results reported yet**

---

## H. Dataset — bAbI Question Answering

**Source:** [facebook/babi_qa (Hugging Face)](https://huggingface.co/datasets/facebook/babi_qa)  
**Original task generator:** [facebookarchive/bAbI-tasks (GitHub)](https://github.com/facebookarchive/bAbI-tasks)  
**Language / version:** English, **10k training-example configurations** (`en-10k-qa1`, `en-10k-qa2`, `en-10k-qa3`)  
**License (dataset card):** CC BY 3.0  
**Nature:** Synthetic stories with questions, answers, and supporting-fact annotations.

| Task | Original task | Reasoning requirement |
|---|---|---|
| **QA1** | Single Supporting Fact | Retrieve one relevant fact |
| **QA2** | Two Supporting Facts | Combine two facts |
| **QA3** | Three Supporting Facts | Follow a longer chain of facts |

### Sample structure

```text
Story:
  Mary picked up the milk.
  Mary traveled to the garden.
  John went to the kitchen.
  Mary dropped the milk.
Question: Where is the milk?
Answer: garden
Supporting facts: IDs of the relevant story sentences
```

*Illustrative example, not a verbatim dataset row.*

**Important:** Supporting-fact IDs may be used for *analysis*, but **not as supervision for training MemN2N**. The training target is the final answer.

### Data processing

- Parse stories, questions, answers, supporting-fact IDs, and original sentence order.
- Use a consistent **word-level tokenizer** and a vocabulary built **only from training data**; reserve an unknown-token ID.
- Transform sentences/questions into token IDs, then embeddings (Steps A–G).
- Preserve event chronology; use position and temporal encoding as specified in model configuration.
- Build a separate answer vocabulary; do not expose held-out answers during vocabulary fitting without documenting the evaluation convention.
- Record dataset revision, configuration, sample counts, and preprocessing parameters.

---

## I. Experimental Design

### 1. Research question and hypothesis

**Research question:** How does the number of memory hops affect MemN2N question-answering accuracy when irrelevant sentences compete for attention?

**Hypothesis (to test):** Additional hops **may** improve multi-fact QA and robustness to distractors, particularly QA2/QA3. More hops are **not guaranteed** to help.

### 2. Independent and dependent variables

| Category | Variables |
|---|---|
| **Independent** | Task: QA1 / QA2 / QA3 |
| **Independent** | Model: BoW baseline / 1-hop MemN2N / 3-hop MemN2N |
| **Independent** | Added distractors: **0, 5, 10, 20** sentences |
| **Extension (optional)** | Distractor type: random vs. entity-overlapping |
| **Dependent** | Answer accuracy; accuracy drop vs. clean input |
| **Diagnostic** | Attention on supporting facts; per-task errors |
| **Controlled** | Training split, tokenizer, embedding size, memory capacity, optimizer, evaluation examples, seed schedule |

**Main grid:** 3 tasks × 3 model configurations × 4 distractor levels = **36 evaluation conditions per seed**. Training is performed per model/task/seed; the distractor levels can be evaluated on the same trained checkpoint in the primary protocol.

### 3. Baseline and model configurations

- **BoW baseline:** Simple supervised question/story representation without multi-hop retrieval; define exact features and classifier before implementation.
- **1-hop MemN2N:** One attention → retrieval operation, then answer prediction.
- **3-hop MemN2N:** Three repeated attention → retrieval operations, then answer prediction.
- Implement in **PyTorch from scratch**; no pretrained language model.
- Use comparable vocabulary, embedding dimensions, training budget, and answer space when fair comparison permits.
- **Default architectural controls:** Position encoding, temporal encoding, weight sharing and memory size must be explicitly documented and held constant across hop comparisons where applicable.

### 4. Distractor injection protocol

1. Select an existing (story, question, answer) example.
2. Add **N = 0 / 5 / 10 / 20** irrelevant, grammatically valid bAbI-style sentences.
3. Insert them at **controlled/randomized positions** while maintaining the relative order of original events.
4. **Validate that the gold answer is unchanged** and no distractor changes the queried entity/object's state.
5. Preserve original supporting-fact IDs using an index mapping after insertion.
6. Keep all relevant facts within the configured memory window; otherwise reject or flag the example.
7. Save the generated perturbations and random seed for exact replay.

**Default distractors:** Prefer facts about unrelated entities that cannot alter the answer.  
**Optional harder setting:** Entity-overlapping distractors, only if their semantics can be verified as non-answer-changing. Do **not** assume a sentence is irrelevant merely because it has a different answer.

### 5. Train / validation / test protocol

- Use the dataset's supplied training and test partitions; create a **deterministic, disjoint validation split from training** if none is provided by the selected loader/configuration.
- Fit vocabulary, choose hyperparameters, and select checkpoints using **training/validation only**.
- **Primary experiment — clean-trained robustness:** Train models on clean stories; evaluate each **same checkpoint** on clean and distractor-augmented held-out examples.
- Reuse identical evaluation examples and, where feasible, the **same generated distractor sets** for all compared models.
- Run **at least 3 random seeds**; report mean and standard deviation.
- **Optional secondary experiment:** Train with distractor augmentation and compare against clean-trained models; keep separate from the primary results.
- Freeze the test protocol before final reporting; do not tune to test-set outcomes.

### 6. Evaluation metrics

**Primary metric — Answer Accuracy**

$$
\operatorname{Accuracy}=\frac{\text{Correct predictions}}{\text{Total questions}}
$$

**Robustness — Accuracy drop from clean condition**

$$
\Delta\operatorname{Acc}(N)=\operatorname{Acc}(0)-\operatorname{Acc}(N)
$$

Report **per-task** accuracy, **per-level** accuracy, and mean ± standard deviation across seeds. Use percentage points for accuracy drop when accuracy is expressed as a percentage.

**Diagnostics (not equivalent to explanation/causality):**
- Attention heatmaps per hop and per sentence.
- Attention mass assigned to annotated supporting facts (with adjusted indices).
- Examples of correct → incorrect predictions after adding distractors.
- Error patterns by QA task, hop count and distractor number.

### 7. Planned figures and tables

| Output | Content |
|---|---|
| **Accuracy vs. distractors** | Lines: 1-hop vs. 3-hop; separate QA1/QA2/QA3 |
| **Robustness table** | Clean accuracy and accuracy drop at 5/10/20 distractors |
| **Attention heatmaps** | Per-hop attention over original and inserted sentences |
| **Error analysis** | Representative failures, with story/question/answer |
| **Baseline comparison** | BoW vs. 1-hop vs. 3-hop under identical evaluation conditions |

### 8. Validity checks and risks

- **Answer preservation:** Distractors must not introduce an alternative correct answer.
- **Memory truncation:** Never silently remove required supporting facts.
- **Temporal confounds:** Inserting sentences changes memory positions; record insertion location and distinguish this from semantic distraction.
- **Leakage:** No overlap of training and held-out examples; no use of test data for tuning.
- **Fairness:** Keep preprocessing, memory capacity and training budgets comparable across models.
- **Attention interpretation:** High attention does not prove logical reasoning or causal importance.
- **Scope:** Results on synthetic bAbI tasks do **not** establish performance on real-world QA or modern LLMs.

### 9. Reproducibility & deliverables

**Record for every run:** `dataset_config`, dataset revision, task, model, hop count, embedding size, positional/temporal encoding, training setup, seed, checkpoint, distractor count/type, injection seed, metrics, and code commit.

**Expected outputs:**

```text
configs/       # model and experiment settings
src/memn2n/    # model, preprocessing, distractors, training, evaluation
notebooks/     # dataset exploration and attention visualization
outputs/       # metrics, figures, checkpoints (large files untracked)
reports/       # final report and experimental findings
research/      # paper notes and protocol
```

**Research workflow:** Dataset inspection → preprocessing checks → baseline → 1-hop → 3-hop → clean evaluation → distractor evaluation → error analysis → report.

---

## Research Status Checklist

- [ ] Verify downloaded task configurations, splits, and sample counts.
- [ ] Inspect QA1/QA2/QA3 story formats and supporting-fact IDs.
- [ ] Define and test answer-preserving distractor generation.
- [ ] Freeze model settings and evaluation protocol.
- [ ] Implement and validate BoW baseline.
- [ ] Train and evaluate 1-hop and 3-hop MemN2N.
- [ ] Run all distractor levels with multiple seeds.
- [ ] Generate figures, tables and failure examples.
- [ ] Report limitations and reproducibility details.

**Key takeaway:** Our contribution is a **controlled experimental study** of how added irrelevant facts affect attention-based retrieval and answer accuracy, and whether **one vs. three memory hops** changes robustness.

## References

1. Sukhbaatar et al. (2015), [*End-To-End Memory Networks*](https://arxiv.org/abs/1503.08895).
2. Weston et al. (2015), [*Towards AI-Complete Question Answering: A Set of Prerequisite Toy Tasks*](https://arxiv.org/abs/1502.05698).
3. [facebook/babi_qa dataset card](https://huggingface.co/datasets/facebook/babi_qa) — configuration names and CC BY 3.0 licensing.
4. [Original bAbI task generator](https://github.com/facebookarchive/bAbI-tasks) — definitions of QA1/QA2/QA3 and synthetic-world generation.
