# MemN2N : End-to-End Training & Backpropagation


## 1. End-to-End Learning

- **Goal:** Learn to answer questions using story memories.
- **Supervision:** Train with the correct answers, without requiring labels identifying supporting sentences.
- Embeddings, attention-based retrieval, and answer prediction are optimized jointly.

## 2. Training Workflow

Story + Question → Embeddings → Attention → Memory Hops → Answer Logits → Cross-Entropy Loss → Backpropagation → Parameter Update

## 3. Cross-Entropy Loss

For one training example with correct answer $y$:

$$
\mathcal{L} = -\log P(y\mid\text{story},\text{question})
$$

- If the correct answer receives probability $0.20$: $\mathcal{L}=-\ln(0.20)\approx1.61$.
- If it receives probability $0.90$: $\mathcal{L}=-\ln(0.90)\approx0.105$.
- **Higher probability for the correct answer → lower loss.**

## 4. Backpropagation & Optimization

Backpropagation calculates the gradients of the loss with respect to trainable parameters.

A basic gradient descent update is:

$$
\theta_{\mathrm{new}} = \theta_{\mathrm{old}} - \eta\nabla_\theta\mathcal{L}
$$

- $\theta$: Trainable parameters (including embedding matrices and output projection).
- $\eta$: Learning rate.
- $\nabla_\theta\mathcal{L}$: Gradient of the loss.

## 5. Why Attention Can Be Learned

Attention weights depend on trainable memory and question embeddings:

$$
p_i = \frac{\exp(u^\top m_i)}{\sum_j\exp(u^\top m_j)}
$$

Gradients flow from **answer loss → prediction → retrieval → attention → embeddings**.

- The network can learn useful attention patterns from answer supervision alone.
- Attention weights do **not** necessarily identify human-defined supporting facts perfectly.

## 6. PyTorch Training Loop — Preview

```python
optimizer.zero_grad()
logits = model(story, question)
loss = criterion(logits, correct_answer)
loss.backward()
optimizer.step()
```

- `criterion` can be `torch.nn.CrossEntropyLoss()`.
- Pass **raw logits**, not softmax probabilities, to `CrossEntropyLoss`.
