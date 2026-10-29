# Literature notes — collaborative working document

## End-To-End Memory Networks (2015)

**Motivating problem:** *To be filled by team after reading paper.*  
**Main components:** word embeddings; input/output memory vectors; softmax attention; iterative hop update; answer prediction.  
**Equation references:** Section 2 of original paper.  
**Implementation decisions to verify:** positional encoding, memory representation, parameter tying, initialization, optimizer, vocabulary/answer encoding.

### Questions for paper-reading session
- What exactly is stored in an input memory versus an output memory?
- Is the same memory read at each hop, or are parameters separate/shared?
- What is the query state `u` and how is it updated?
- How can we validate attention and answer predictions independently?
- What parts of the original training recipe matter most on QA1–QA3?

### Evidence / notes
*Add original notes with page references here. Do not paste the paper verbatim.*
