# MemN2N : Answer Prediction


## 1. Inputs

After memory retrieval:

- $u$: embedded question vector.
- $o$: retrieved memory output vector.

Both have embedding dimension $d$.

## 2. Combine question and retrieved information

$$
z = o + u
$$

- $z \in \mathbb{R}^{d}$: combined representation.

## 3. Output projection — Matrix W

$$
y = Wz
$$

- $W \in \mathbb{R}^{K \times d}$: trainable output matrix.
- $K$: number of possible answer classes (answer vocabulary size).
- $y \in \mathbb{R}^{K}$: raw answer scores (**logits**).

## 4. Answer Softmax

$$
\hat{a} = \operatorname{softmax}(y) = \operatorname{softmax}\!\bigl(W(o+u)\bigr)
$$

- $\hat{a}$: probability distribution over possible answers.
- **Prediction:** Answer class with the highest probability.

**Illustrative example:**

| Answer | Predicted probability |
|---|---:|
| Garden | 75% |
| Kitchen | 15% |
| Office | 10% |

**Predicted answer:** Garden.

## 5. Two Different Softmax Operations

| Attention Softmax — Step B | Answer Softmax — Step D |
|---|---|
| Distribution over stored memories | Distribution over possible answers |
| Determines each memory's retrieval weight | Determines answer probabilities |

## 6. One Hop vs. Multiple Hops

- **One-hop MemN2N:** Retrieve memory once, then predict the answer.
- **Multi-hop MemN2N:** Update the question state and repeat retrieval before the final prediction.

$$
u^{k+1} = u^{k} + o^{k}
$$
