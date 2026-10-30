# MemN2N — Step G: Position & Temporal Encoding

**Paper:** *End-To-End Memory Networks* — Sukhbaatar et al. (2015)  
**Purpose:** Represent word order within sentences and sentence order within memory.

## 1. Why encoding order matters

A basic **Bag-of-Words (BoW)** sentence representation ignores word order:

- “Mary pushed John.”
- “John pushed Mary.”

Both contain the same words, but have different meanings.

Story chronology also matters:

1. Mary went to the kitchen.
2. Mary traveled to the garden.

**Question:** Where is Mary? → **Garden**, the more recent location.

## 2. Position Encoding — Word order

Without position encoding:

$$
m_i = \sum_{j=1}^{J} A x_{ij}
$$

With position encoding:

$$
m_i = \sum_{j=1}^{J} l_j \odot A x_{ij}
$$

- $x_{ij}$: One-hot vector for word $j$ in sentence $i$.
- $A$: Trainable input embedding matrix.
- $l_j$: Position-dependent vector.
- $\odot$: Element-wise multiplication.
- $J$: Number of words in the sentence.

**Purpose:** Make the sentence representation sensitive to word positions.

## 3. Temporal Encoding — Sentence order

MemN2N adds learned temporal vectors to memory slots:

$$
m_i = A x_i + T_A(i)
$$

$$
c_i = C x_i + T_C(i)
$$

- $T_A(i)$: Input-memory temporal embedding at memory position $i$.
- $T_C(i)$: Output-memory temporal embedding at memory position $i$.
- $i$: Sentence position in the memory sequence.

**Purpose:** Help distinguish earlier from later events.

**Note:** These expressions show temporal encoding with basic sentence embeddings. Position encoding can also be incorporated into the sentence embeddings before adding temporal vectors.

## 4. Position vs. Temporal Encoding

| Mechanism | Captures | Level |
|---|---|---|
| **Position encoding** | Word order | Within a sentence |
| **Temporal encoding** | Sentence/event order | Across memory slots |

## 5. Connection to our research

- Word order can change sentence meaning.
- Event order can determine the answer.
- Added distractors may change relevant sentences' memory positions.
- Preserve the meaningful event sequence and correct answers when generating distractors.

**Key takeaway:** Position encoding models **where words appear** within a sentence; temporal encoding models **where sentences appear** in memory.

**Next:** Step H — bAbI Dataset & Evaluation.
