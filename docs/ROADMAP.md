# Four-week research roadmap

| Milestone | Outcome | Exit check |
|---|---|---|
| **M0 — Workstation** | Shared reproducible local setup | Two machines run smoke tests |
| **M1 — Research + Data** | Paper notes, bAbI parsing and dataset report | Questions extracted with supporting IDs only as metadata |
| **M2 — Baseline + Model** | Bag-of-words QA baseline, one-hop MemN2N | Baseline measured; model learns on a tiny sanity dataset |
| **M3 — Comparative training** | Train one-hop and three-hop with controlled settings | Validation results captured with configs/seeds |
| **M4 — Distractor study** | 0/5/10/20 distractor tests and attention analysis | Correct answers preserved; no truncation of supporting facts |
| **M5 — Reporting** | Figures, limitations, demo and report | Every reported result traceable to a saved run |

### Priority order
1. Correct input parsing, reproducible splits, clean baseline.
2. Training stability and verified architecture.
3. Controlled distractors and reproducible evaluation.
4. Optional extras (entity-overlap distractors, interactive demo) only if the core works.

### Fallback
If implementation runs late: QA1 + QA2, one-hop vs two-hop, fewer distractor conditions. Retain at least one baseline, one controlled experiment and manual error analysis.
