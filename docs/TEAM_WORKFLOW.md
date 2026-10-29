# Team collaboration — practical rules

## One repository, two collaborators
Create a **private** GitHub repository manually when ready; invite both members. This archive does not create or connect any remote repository.

```powershell
# After extracting the archive:
git init
git add .
git commit -m "chore: initialize CS351 research workstation"
# Create an empty private GitHub repository in the browser, then:
git branch -M main
git remote add origin https://github.com/YOUR-ACCOUNT/neural-memory-research.git
git push -u origin main
```

## Team routine
1. Pick one task from `PROJECT_BOARD.md` and claim it.
2. Create a topic branch, e.g. `feature/babi-preprocessing`.
3. Commit small, reviewable changes; run local checks before merging.
4. Update `PROGRESS_LOG.md` when a result, decision or blocker matters.
5. Keep `STATUS.md` concise and current, and link completed work to task IDs.

## Never commit
Data downloads, training checkpoints, local environments, `.env` secrets, large run outputs, cloud access tokens. Use scripts/manifests and run IDs to reproduce them.

## Review checklist
- Does the change preserve train/validation/test separation?
- Does it include a test or reproducible evidence?
- Does documentation reflect what actually works?
- Do figures and metrics correspond to real recorded experiments?
