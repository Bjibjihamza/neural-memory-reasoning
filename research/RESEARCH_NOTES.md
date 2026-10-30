# Neural Networks & Memory — Research Notes

**Research Paper:** *End-To-End Memory Networks* — Sukhbaatar et al. (2015)  
**Project:** When Does Neural Memory Fail? Investigating Distractors in Multi-Hop Reasoning

---

## 1. Neural Network Families

Neural Networks (NNs) are a broad family of Deep Learning models.

| Architecture | Main application |
|---|---|
| ANN / MLP | General prediction and classification |
| CNN | Computer Vision |
| RNN / LSTM / GRU | Sequential data, NLP, time series |
| Transformers | Attention-based modeling, NLP, generation |
| Memory Networks | Memory retrieval and question answering |

### Important Research Papers

| Architecture | Year | Paper |
|---|---|---|
| MemN2N | 2015 | *End-To-End Memory Networks* — Sukhbaatar et al. |
| Transformer | 2017 | *Attention Is All You Need* — Vaswani et al. |

## 2. Neural Networks & Memory

**Neural memory:** Mechanisms that allow a model to retain, access or reuse information.

### Main Memory Mechanisms

- **Parametric memory:** Knowledge stored in learned weights.
- **Hidden state:** Information carried between sequence steps (RNN).
- **Gated memory:** Selective retention and forgetting (LSTM / GRU).
- **External memory:** Explicit memory slots accessible through retrieval (MemN2N).
- **Attention-based context:** Access to relevant token representations (Transformers).

*These mechanisms can overlap.*

### Evolution of Neural Memory

| Architecture | Memory mechanism |
|---|---|
| Feedforward NN | Learned weights; no persistent sequential state by default |
| RNN | Recurrent hidden state |
| LSTM / GRU | Hidden state + learned gates |
| MemN2N | External memory + attention |
| Transformer | Attention-based contextual representations |

*Conceptual progression, not a strict historical lineage.*

## 3. The Research Problem

**Problem:** Remembering information is not enough; a model must retrieve and combine the right facts.

### Limitations of Recurrent Networks

**RNN**

Sentence 1 → Sentence 2 → … → Sentence N → Final hidden state → Prediction

- Processes information sequentially.
- Compresses previous information into an evolving hidden state.
- Can struggle to preserve and retrieve distant information.

**LSTM / GRU**

- Improve long-range information retention.
- Use gates to manage information.
- Do not automatically provide direct access to every earlier sentence.

### Key Research Question

Can a neural network:

1. Store multiple pieces of information?
2. Retrieve relevant facts based on a question?
3. Combine information from different memories?
4. Learn retrieval using only the final answer as supervision?

**Proposed solution:** External Memory + Attention.

## 4. MemN2N Architecture

**Core principle:** Represent sentences as memory vectors and use attention to retrieve relevant information.

### Step A — Sentence & Question Embeddings

Convert sentence representations into memory vectors:

\[
m_i=Ax_i
\]

- \(x_i\): vector representation of sentence \(i\)
- \(A\): trainable embedding matrix
- \(m_i\): input memory vector

Embed the question:

\[
u=Bq
\]

- \(q\): question representation
- \(B\): question embedding matrix
- \(u\): internal question vector

**Concepts:** Tokenization, embeddings, matrix multiplication.

### Step B — Attention

Compare the question vector with each memory vector:

\[
p_i=\frac{\exp(u^\top m_i)}{\sum_j\exp(u^\top m_j)}
\]

- \(u^\top m_i\): similarity score
- Softmax: normalizes attention weights across memory slots
- \(p_i\): attention weight for memory \(i\)

**Goal:** Assign greater weight to relevant memories.

### Step C — Memory Retrieval

\[
o=\sum_i p_i c_i
\]

- \(c_i=Cx_i\): output memory vector
- \(p_i\): attention weight
- \(o\): weighted memory output

**Concept:** Weighted sum of memory representations.

### Step D — Answer Prediction

For a single-hop model:

\[
\hat a=\operatorname{softmax}(W(o+u))
\]

- \(W\): trainable output projection
- \(\hat a\): probability distribution over possible answers

**Task:** Answer classification (e.g., garden, kitchen, office).

## 5. Multiple Memory Hops

**One hop:** Access memory once.

**Multiple hops:** Access memory repeatedly, updating the internal question state.

\[
u^{k+1}=u^k+o^k
\]

- \(u^k\): state before hop \(k\)
- \(o^k\): retrieved information
- \(u^{k+1}\): updated state

**Important:** More hops provide additional retrieval steps but do not guarantee better reasoning.

## 6. End-to-End Learning

**Main contribution:** Learn memory retrieval without explicit supporting-fact labels.

### Training Workflow

Story + Question  
↓  
Embeddings  
↓  
Attention + Memory Hops  
↓  
Answer Prediction  
↓  
Cross-Entropy Loss  
↓  
Backpropagation → Update Parameters

**Trainable components:** Embeddings, attention-related representations, output projection.

## 7. Additional Concepts to Study

- **Position Encoding:** Preserve word-order information.
- **Temporal Encoding:** Represent the order of events or memory slots.
- **Weight Sharing:** Reuse or link parameters across memory hops.
- **Bag-of-Words:** Sentence representation without explicit word order.

## 8. Experiments & Evaluation

**Dataset:** bAbI Question Answering

| Task | Supporting facts |
|---|---|
| QA1 | 1 fact |
| QA2 | 2 facts |
| QA3 | 3 facts |

### Our Research Experiment

**Question:** How do irrelevant sentences affect memory retrieval and multi-hop reasoning?

- Compare **1-hop vs. 3-hop MemN2N**.
- Introduce **0, 5, 10, 20 distractors**.
- Evaluate **answer accuracy**.
- Analyze **attention distributions**.
- Investigate **retrieval failures**.

**Hypothesis:** Multiple hops may help retrieve and combine supporting facts, but robustness to distractors must be measured experimentally.

---

## 9. Essential Concepts Checklist

- [ ] Word embeddings and matrix dimensions
- [ ] Dot product and Softmax
- [ ] Attention and weighted sum
- [ ] Multi-hop retrieval
- [ ] Cross-entropy and backpropagation
- [ ] Position and temporal encoding
- [ ] bAbI dataset and experiment design

**Key takeaway:** MemN2N learns to retrieve and combine information from external memory using attention, with the entire model trained through the final answer prediction.