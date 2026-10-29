# Architecture notes — implementation plan (not yet implemented)

MemN2N is **not a Transformer**. We will implement repeated memory attention and an answer classifier, using PyTorch tensor operations and autodiff.

## Inputs
- Context story: sentence tokens → trainable memory vectors `m_i` and output vectors `c_i`.
- Question: tokens → query state `u`.

## One hop (simplified conceptual equations)
- Attention weights: `p_i = softmax(u^T m_i)` over all memory slots.
- Readout: `o = sum_i(p_i * c_i)`.
- Updated state: `u_next = u + o` (a basic hop configuration).
- Final prediction: softmax over answer vocabulary after chosen number of hops.

## Engineering checks
- Attention has shape `[batch, memory_slots]` and sums to ~1 over valid slots.
- Padding and memory masks must not receive attention.
- Memory window covers all required facts plus added distractors.
- Test tiny synthetic examples and intentionally overfit a micro-batch before full runs.
- Extract attention for visualization only after model predictions are verified.

The original paper includes more training and embedding variants than this simplified outline. Confirm the chosen implementation recipe before claiming a faithful reproduction.
