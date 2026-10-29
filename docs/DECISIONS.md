# Research decision log

| ID | Decision | Rationale | Revisit if |
|---|---|---|---|
| ADR-001 | Use MemN2N from the 2015 paper, no pretrained weights | Learn architecture and attention from scratch | Implementation cannot train within deadline |
| ADR-002 | bAbI English QA1–QA3 (`en-valid-10k-*`) | One/two/three supporting-fact tasks with official splits | Data format/access differs from documentation |
| ADR-003 | Compare 1 vs 3 memory hops with 0/5/10/20 distractors | Controlled architecture × robustness experiment | Training budget requires reduced grid |
| ADR-004 | Git + Markdown + notebooks + reusable Python modules | Lightweight shared research system | Tooling becomes a blocker |
| ADR-005 | No full datasets/model checkpoints in Git | Keep repository compact and avoid accidental data leakage | A reproducible artifact store is later selected |
| ADR-006 | No custom dashboard or MLflow initially | Preserve time for model implementation | Manual run tracking becomes unmanageable |

Add an entry whenever a research or engineering choice materially changes.
