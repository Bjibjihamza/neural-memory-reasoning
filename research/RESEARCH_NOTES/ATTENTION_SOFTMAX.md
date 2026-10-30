# MemN2N : Attention Mechanism & Softmax


## 1. Similarity Scores — Recap

Compare the embedded question $u$ with each input memory vector $m_i$:

$$
s_i = u^\top m_i
$$

- $s_i$: raw similarity score for memory $i$ (not a probability).
- Higher scores indicate stronger learned matching.

## 2. Softmax — Scores to Attention Weights

$$
p_i = \frac{e^{s_i}}{\sum_j e^{s_j}}
$$

- $p_i$: attention weight for memory $i$.
- $0 < p_i < 1$ and $\sum_i p_i = 1$ (for a finite, nonempty set of scores).
- Every memory receives a weight; softmax does not select only one sentence.

## 3. Attention Workflow

**Question vector $u$ + input memories $m_i$**  
$\downarrow$ Dot product: $s_i=u^\top m_i$  
$\downarrow$ Softmax: $p_i=\operatorname{softmax}(s)_i$  
**Attention distribution:** $[0.665,\ 0.245,\ 0.090]$

## 4. Memory Retrieval

Apply the attention weights to the **output memory vectors** $c_i=Cx_i$:

$$
o = \sum_i p_i c_i
$$

- $p_i$: attention weight.
- $c_i$: output memory vector.
- $o$: retrieved information (weighted sum).

