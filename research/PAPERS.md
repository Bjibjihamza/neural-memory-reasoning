# Literature library / reading queue

## Primary paper — read first
**Sukhbaatar, Szlam, Weston & Fergus (2015). End-To-End Memory Networks. NeurIPS 2015.**  
[Paper (arXiv PDF)](https://arxiv.org/pdf/1503.08895) · [Abstract](https://arxiv.org/abs/1503.08895)

Focus: memory slots and embeddings; softmax attention; output vectors; iterative updates; answer prediction; training settings; bAbI results; limitations.

## Benchmark
**Weston et al. (2015). Towards AI-Complete Question Answering: A Set of Prerequisite Toy Tasks.**  
[Paper](https://arxiv.org/abs/1502.05698) · [Dataset card](https://huggingface.co/datasets/facebook/babi_qa)

Focus: QA1/QA2/QA3 distinction; story/question/answer format; supporting fact annotations; synthetic-data limitations; CC BY 3.0 usage.

## Optional background
- [Gated End-to-End Memory Networks (2017)](https://aclanthology.org/E17-1055/): later variants and difficulties.
- [Attention Is All You Need (2017)](https://arxiv.org/abs/1706.03762): conceptual comparison only; **not** the model implemented here.

## Paper-file organization
Local copies of the PDFs may be placed in `research/papers/` and are ignored by Git. The team should download from source when needed and keep bibliographic links and original notes under version control.

## Reading workflow
Each reader adds a few points to `LITERATURE_NOTES.md`: problem, main mechanism, equations, assumptions, reproducibility questions, relevant figure numbers. Discuss open points together before coding.
