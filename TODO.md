# Neural Memory Research — Full Labs Roadmap

Project: When Does Neural Memory Fail? Investigating Distractors in Multi-Hop Reasoning

Objective: Implement MemN2N from scratch using PyTorch, reproduce its core behavior on bAbI, and investigate how distractors affect multi-hop reasoning.

We'll use Jupyter Notebooks for learning and experimentation, and `src/memn2n/` for reusable Python code.

## Phase 1 — Data Preparation

Lab 01

bAbI Dataset Exploration

Covered

Dataset loading, QA1/QA2/QA3, raw and structured records, supporting facts, statistics, vocabulary exploration, data splits and visualizations.

Notebook: `01_dataset_exploration.ipynb`

Lab 02

Preprocessing & Vocabulary Construction

Word-level tokenization, normalization, vocabulary, token IDs, answer labels, padding, masks, PyTorch `Dataset` and `DataLoader`.

Notebook: `02_preprocessing_vocabulary.ipynb`

## Phase 2 — MemN2N Implementation

| Lab | Topic                              | Main deliverable                                                           |
| --- | ---------------------------------- | -------------------------------------------------------------------------- |
| 03  | Embeddings & Memory Representation | Implement matrices \\(A,B,C\\), sentence embeddings and position encoding  |
| 04  | Attention & Memory Retrieval       | Dot-product scores, Softmax, weighted sum and attention visualization      |
| 05  | Multiple Memory Hops               | Implement 1-hop and 3-hop MemN2N                                           |
| 06  | Training Pipeline                  | Cross-entropy, backpropagation, optimizer, checkpoints and training curves |

## Phase 3 — Baselines & Evaluation

| Lab | Topic                       | Main deliverable                                                      |
| --- | --------------------------- | --------------------------------------------------------------------- |
| 07  | Baseline & Clean Evaluation | Bag-of-Words baseline, QA1/QA2/QA3 accuracy and model comparisons     |
| 08  | Distractor Generation       | Generate 0, 5, 10 and 20 distractors without changing correct answers |

## Phase 4 — Research Experiments

| Lab | Topic                      | Main deliverable                                                                |
| --- | -------------------------- | ------------------------------------------------------------------------------- |
| 09  | Controlled Experiments     | Compare 1-hop vs. 3-hop under different distractor levels, using multiple seeds |
| 10  | Attention & Error Analysis | Attention heatmaps, failure cases, per-task degradation and interpretation      |

## Phase 5 — Research Deliverables

| Lab | Topic                            | Main deliverable                                                   |
| --- | -------------------------------- | ------------------------------------------------------------------ |
| 11  | Results & Statistical Analysis   | Tables, plots, mean/std across seeds and reproducibility summary   |
| 12  | Scientific Report & Presentation | Research report, limitations, conclusions and presentation figures |

## Progress

Research implementation roadmap

1 / 12 labs covered

Lab 01 covered; Lab 02 is next. Full experimental validation is still ahead.

## Final project structure

```
neural-memory-reasoning/
├── notebooks/
│   ├── 01_dataset_exploration.ipynb
│   ├── 02_preprocessing_vocabulary.ipynb
│   ├── 03_memory_embeddings.ipynb
│   ├── 04_attention_retrieval.ipynb
│   ├── 05_multiple_memory_hops.ipynb
│   ├── 06_training_pipeline.ipynb
│   ├── 07_baseline_evaluation.ipynb
│   ├── 08_distractor_generation.ipynb
│   ├── 09_controlled_experiments.ipynb
│   ├── 10_attention_error_analysis.ipynb
│   ├── 11_results_analysis.ipynb
│   └── 12_research_report.ipynb
├── src/memn2n/
│   ├── data.py
│   ├── model.py
│   ├── train.py
│   ├── evaluate.py
│   └── distractors.py
├── configs/
├── outputs/
├── research/
└── reports/
```

The notebook filenames above are the proposed final organization; they are not all existing files yet.

Our next task is Lab 02 — Preprocessing & Vocabulary Construction. The goal is to produce the numerical tensors that our MemN2N architecture will consume.

We'll continue with the same approach: simple code, clear scientific objectives, and no unnecessary verification cells.