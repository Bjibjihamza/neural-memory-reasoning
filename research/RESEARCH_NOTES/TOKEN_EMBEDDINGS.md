# MemN2N — Step A: Text to Memory Vectors

## 1. Input representations

$$
m_i = Ax_i \qquad u = Bq
$$

- **Tokenization:** The bAbI setup uses **word-level tokens**, not character- or subword-level tokenization. The paper does not prescribe a particular tokenizer library.
- **Vocabulary size:** $V$ = number of distinct words.
- **Embedding dimension:** $d$ = size of each learned dense vector.
- **Trainable embedding matrices:** $A, B, C \in \mathbb{R}^{d \times V}$.

## 2. Input memory — Matrix A

$$
m_i = Ax_i
$$

- $x_i$: sentence $i$ represented as a **Bag-of-Words (BoW)** vector of size $V$.
- $A$: input memory embedding matrix.
- $m_i$: dense memory vector of size $d$.

## 3. Question representation — Matrix B

$$
u = Bq
$$

- $q$: numerical question representation (size $V$).
- $B$: trainable question embedding matrix.
- $u$: embedded question vector (size $d$).

## 4. Output memory — Matrix C

$$
c_i = Cx_i
$$

- $C$: trainable output memory embedding matrix.
- $c_i$: output memory vector used when retrieving information.

**Intuition:** $A$ represents memories for **matching**; $B$ represents the **question**; $C$ represents the information **retrieved**.

## 5. Similarity score — Before softmax

$$
s_i = u^\top m_i
$$

- Compares the question vector with each input memory vector.
- Produces **one scalar score per memory slot**.
- Attention weights are calculated from these scores in the next step.

## 6. Matrix dimensions

| Component | Shape |
|---|---|
| $x_i$, $q$ | $V \times 1$ |
| $A$, $B$, $C$ | $d \times V$ |
| $m_i$, $u$, $c_i$ | $d \times 1$ |
| $s_i$ | Scalar |
