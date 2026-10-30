# MemN2N : Multiple Memory Hops



## 1. What is a memory hop?

A **memory hop** is one round of attention and memory retrieval.

- **1-hop:** Retrieve information once, then predict the answer.
- **Multi-hop:** Revisit memory, updating the internal question state after each retrieval.


## 2. Multi-hop equations

Initial question state:

$$
u^1 = Bq
$$

At hop $k$, compute attention and retrieve information:

$$
p_i^k = \frac{\exp\!\left((u^k)^\top m_i^k\right)}{\sum_j \exp\!\left((u^k)^\top m_j^k\right)}
$$

$$
o^k = \sum_i p_i^k c_i^k
$$

Update the internal question state:

$$
\boxed{u^{k+1} = u^k + o^k}
$$

- $u^k$: Question state before hop $k$.
- $p_i^k$: Attention weight for memory $i$ at hop $k$.
- $c_i^k$: Output memory vector.
- $o^k$: Retrieved information.
- $u^{k+1}$: Updated state for the next hop.

After $K$ hops, predict the answer:

$$
\hat a = \operatorname{softmax}\!\left(Wu^{K+1}\right)
$$

## 3. Workflow

**Question embedding → Hop 1 (attention + retrieval) → Update state → Hop 2 → … → Hop K → Answer prediction**

**Important:** Hops are learned computation steps, not guaranteed human-like logical steps. More hops do **not** automatically mean better reasoning. The original paper also considers parameter sharing across hops.

## 4. Connection to our experiment

- Compare **1-hop vs. 3-hop** MemN2N.
- Add **0, 5, 10, 20 distracting sentences**.
- Measure **answer accuracy** and inspect **attention distributions**.
- Test whether repeated retrieval improves robustness; do not assume it does.
