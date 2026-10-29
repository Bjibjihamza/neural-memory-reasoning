# When Does Neural Memory Fail?

**CS 351 — Natural Language Processing | Research workstation**  
**Team:** Bjibji Hamza · Elbouk Abderrahimane  
**Status:** Proposal approved; workstation scaffold created; model training not started.

> **Research question:** How does the number of memory hops affect multi-fact question answering as distracting facts are added?

## Start here

1. **[Current status](docs/STATUS.md)** — what is completed, what is next.
2. **[Task board](docs/PROJECT_BOARD.md)** — bite-size tasks and acceptance criteria.
3. **[Windows setup](docs/SETUP_WINDOWS.md)** — Git, Python, VS Code, uv, PyTorch and CUDA checks.
4. **[Literature](research/PAPERS.md)** — primary paper, benchmark, reading plan.
5. **[Experiment protocol](docs/EXPERIMENT_PROTOCOL.md)** — how to compare models without leakage.

## Quick start (once Python, uv, Git are installed)

```powershell
cd neural-memory-research
uv sync --extra dev
uv run python -m memn2n doctor
uv run python -m memn2n inspect-fixture
uv run pytest -q
```

A real GPU-enabled PyTorch installation is **not** part of the lightweight workstation bootstrap. Follow the [CUDA notes](docs/SETUP_WINDOWS.md) when starting the modeling phase. If `uv` is unavailable, use Python venv/pip as documented.

## Repository layout

| Directory | Purpose |
|---|---|
| `proposal/` | Approved YAML and submitted thumbnail |
| `research/` | Papers, literature notes and architecture notes |
| `docs/` | Roadmap, status, project board, decisions, reproducibility protocol |
| `data/` | Downloaded/prepared bAbI data (ignored by Git) |
| `notebooks/` | Exploration and research notebooks |
| `src/memn2n/` | Small reusable Python utilities; future neural architecture |
| `configs/` | Planned experimental settings |
| `tests/` | Offline fixture and unit tests |
| `outputs/` | Checkpoints, metrics and figures (ignored by Git) |
| `reports/` | Report and presentation work products |

## Boundaries of this starter

- **Included now:** usable local project, source tracking layout, status/tasks/docs, paper references, proposal/image, offline data parser + smoke test, starter notebook, checks.
- **Not completed yet:** bAbI download/EDA, bag-of-words baseline, MemN2N implementation, model training, distractor generation and experimental results.
- **Not created remotely:** GitHub repository or GitHub Project board. Both can be set up manually using [team workflow](docs/TEAM_WORKFLOW.md).

The bAbI benchmark is publicly available under CC BY 3.0: <https://huggingface.co/datasets/facebook/babi_qa>. Cite the dataset and original paper in all reports. Generated files and downloaded literature should stay outside the normal Git commit history.
