# Setup — Windows / PowerShell (local RTX 3060 and RTX 3050)

## Prerequisites
- Git, VS Code (Python/Jupyter extensions), Python 3.11, `uv` (recommended).
- Install uv from the [official documentation](https://docs.astral.sh/uv/getting-started/installation/). Alternative: Python `venv` + pip.
- Do **not** run the terminal as Administrator to work on this repository.

## Bootstrap (PowerShell)

```powershell
cd .\neural-memory-research
uv sync --extra dev
uv run python -m memn2n doctor
uv run python -m memn2n inspect-fixture
uv run pytest -q
```

`uv` generates a lockfile on the first sync; **commit `uv.lock` only after the team verifies the same intended Python/dependency setup**. This archive does not pretend a lockfile was created offline.

## Alternative: standard Python virtual environment

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m memn2n doctor
python -m memn2n inspect-fixture
pytest -q
```

## Notebook environment (later)

```powershell
uv sync --extra dev --extra notebook
uv run python -m ipykernel install --user --name neural-memory-research --display-name "Neural Memory Research"
```

## PyTorch + CUDA (at model milestone)
- Check your driver/GPU first: `nvidia-smi`.
- Choose the supported Windows CUDA wheel from the [official PyTorch selector](https://pytorch.org/get-started/locally/). Do not assume that an ordinary `torch` install automatically provides CUDA on Windows.
- Install the matching PyTorch build **inside the same project environment**; document exact commands and versions in `PROGRESS_LOG.md`.
- Verify with: `python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"` (use `uv run python` if uv-managed).
- Training will begin only after GPU detection is verified; CPU operation remains possible for smoke tests.

## Where data and PDFs go
- Downloaded dataset files: `data/raw/`.
- Processed question-level data: `data/processed/`.
- Paper PDFs: `research/papers/` (not committed); links and your notes live in `research/PAPERS.md`.
- Training runs: `outputs/` (not committed).

## Cloud
Colab or Azure for Students can run the same code after cloning the repository and installing compatible dependencies. GPU availability/quotas are not guaranteed; avoid placing tokens or personal cloud keys inside notebooks.
