---
title: "Git Merge vs. Rebase vs. Cherry-Pick: When to Use Each"
date: 2014-07-28 08:56:17 +0000
layout: post
canonical: https://www.systutorials.com/git-merging-faqs/
---

`git merge` and `git rebase` both integrate changes from one branch into another, but they handle history differently.

**Merge** creates a new commit that ties together the histories of both branches. Your feature branch history remains intact, and the main branch gains a merge commit. This is safer for shared branches because it doesn’t rewrite history.

``` bash
git checkout main
git merge feature-branch
```

**Rebase** replays your commits on top of the target branch, rewriting history. It produces a linear timeline but should only be used on branches you haven’t shared yet.

``` bash
git checkout feature-branch
git rebase main
```

**When to use each:**

- Use `git merge` for shared branches and when merging to main/master
- Use `git rebase` on local branches before creating a pull request to clean up history
- Never rebase commits that others have already pulled

## Fast-Forward Merges

When your main branch hasn’t changed since you created your feature branch, Git can fast-forward — it simply moves the main branch pointer forward without creating a merge commit.

``` bash
git merge feature-branch
```

If main is a direct ancestor of feature-branch, this fast-forwards automatically. To disable this behavior and always create a merge commit:

``` bash
git merge --no-ff feature-branch
```

To only allow fast-forward merges (fails if not possible):

``` bash
git merge --ff-only feature-branch
```

For most teams, using `--no-ff` on main/master ensures every merge is visible in history, making it easier to track what was integrated and when.

## Handling Merge Conflicts

Conflicts occur when both branches modify the same lines. Git marks conflicted sections with these markers:

    <<<<<<< HEAD
    your current branch changes
    =======
    incoming branch changes
    >>>>>>> branch-name

### Manual Resolution

``` bash
# View conflicted files
git status

# Edit the file to resolve conflicts
vim conflicted-file.txt

# Mark as resolved
git add conflicted-file.txt

# Complete the merge
git commit -m "Resolve merge conflict"
```

### Using Merge Tools

For a more visual approach, use your editor’s built-in merge tool:

``` bash
# Use VS Code, Neovim, or your configured merge tool
git mergetool
```

### Examining Both Sides

To see what changed on each side before resolving:

``` bash
git diff --ours      # your branch
git diff --theirs    # incoming branch
git diff --base      # common ancestor
```

## Testing a Merge Before Committing

Preview merge results without immediately committing:

``` bash
# Create a temporary branch to test
git checkout -b test-merge main
git merge feature-branch

# Examine the result
git diff main..test-merge

# If it looks good, clean up and do the real merge
git checkout main
git merge feature-branch
git branch -d test-merge
```

Alternatively, use a dry-run approach:

``` bash
git merge --no-commit --no-ff feature-branch

# Review the changes
git status
git diff --cached

# Abort if unhappy
git merge --abort

# Or complete it if satisfied
git commit
```

## Undoing a Merge

If you’ve already merged but want to undo it, the approach depends on whether it’s been pushed.

**For unpushed merges:**

``` bash
git reset --hard HEAD~1
```

**For already-public merges:**

Create a revert commit instead:

``` bash
# Find the merge commit
git log --oneline | head -20

# Revert it (use -m 1 to specify which parent to keep)
git revert -m 1 <merge-commit-hash>

# Push the revert
git push
```

The `-m 1` flag tells Git to revert to the first parent (your main branch) and discard changes from the second parent (the merged branch).

## Selective Merging with Cherry-Pick

To merge only specific commits from another branch:

``` bash
# List commits you want
git log feature-branch --oneline

# Cherry-pick individual commits
git cherry-pick <commit-hash>
git cherry-pick <commit-hash-2>
```

To cherry-pick a range:

``` bash
git cherry-pick commit1..commit2
```

If conflicts occur during cherry-pick:

``` bash
# After resolving conflicts
git add resolved-file.txt
git cherry-pick --continue

# Or abort the entire operation
git cherry-pick --abort
```

Cherry-pick is useful for backporting bug fixes, but avoid it for large feature branches — use merge instead. Overusing cherry-pick creates duplicate commits and makes history harder to follow.

## Replacing an Entire Branch

To completely rewrite a branch with content from another:

``` bash
# Replace feature-branch with content from main
git checkout feature-branch
git reset --hard main
```

Or without checking out the branch:

``` bash
git branch -f feature-branch main
```

Force-push this change (only if you own the branch):

``` bash
git push origin feature-branch --force-with-lease
```

Always use `--force-with-lease` instead of `--force` — it’s safer because it checks that no one else pushed changes in the meantime.

## Practical Feature Branch Workflow

A typical feature branch workflow that keeps history clean:

``` bash
# Create and work on feature branch
git checkout -b feature/new-api
# ... make commits and push ...

# Before merging, fetch latest and rebase on main
git fetch origin
git rebase origin/main

# Resolve any conflicts that arise
# Test thoroughly with local builds/tests

# Switch to main and merge with a merge commit
git checkout main
git pull origin main
git merge --no-ff feature/new-api

# Push and clean up
git push origin main
git branch -d feature/new-api
```

This approach keeps main’s history clean, makes bisecting easier with `git bisect`, and ensures every feature merge is explicitly documented in the log.

## Rebasing Multiple Commits Interactively

To squash, reorder, or edit multiple commits before merging:

``` bash
# Rebase the last 3 commits
git rebase -i HEAD~3
```

This opens your editor with a list of commits. Common commands:

- `pick` — use commit as-is
- `squash` (or `s`) — merge commit into the previous one
- `reword` (or `r`) — change commit message
- `drop` (or `d`) — discard commit
- `fixup` (or `f`) — like squash, but discard commit message

After editing and saving, Git will reapply the commits in the new order. This is powerful for cleaning up local history before opening a pull request.

## Merge Strategies

By default, Git uses the `recursive` strategy for standard merges. Other strategies are available:

``` bash
# Resolve by preferring "ours" changes in conflicts
git merge -X ours feature-branch

# Or prefer "theirs" changes
git merge -X theirs feature-branch

# Use the resolve strategy (older, simpler algorithm)
git merge -s resolve feature-branch
```

These are rarely needed but useful when merging branches with known conflict patterns.
