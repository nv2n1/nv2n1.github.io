---
title: "Git Branches and Remote Repositories: A Practical Guide"
date: 2014-07-24 05:36:22 +0000
layout: post
canonical: https://www.systutorials.com/cheatsheet-git-branching-with-a-git-server/
---

``` bash
git clone https://example.com/your/repo.git
git clone git@github.com:user/repo.git
```

Use HTTPS for better firewall compatibility, or SSH if you have keys configured. HTTPS requires authentication via personal access tokens or git credentials; SSH uses key-based auth.

## List branches

``` bash
# Local branches only
git branch

# All branches (local and remote)
git branch -a

# Show branch tracking information
git branch -vv

# Show last commit on each branch
git branch -v
```

Use `git branch -vv` to see which remote branches your locals are tracking. This is especially useful when working across multiple remotes.

## Fetch and update

``` bash
# Fetch changes without merging
git fetch origin

# Fetch and merge into current branch
git pull origin

# Fetch all remotes
git fetch --all

# Remove stale remote tracking branches
git fetch origin --prune
```

Always fetch before pulling to review changes. If you need to sync multiple remotes, use `git fetch --all` to update all tracked remotes at once.

## Switch branches

``` bash
# Preferred modern syntax (Git 2.23+)
git switch rc

# Create and switch in one command
git switch -c dev-b1

# Switch to tracking a remote branch
git switch --track origin/dev-b1
```

`git switch` is clearer than `git checkout` for branch operations. Reserve `checkout` for file restoration (`git checkout -- file`).

## Create a new branch

``` bash
# Create locally
git branch dev-b1

# Create and switch immediately
git switch -c dev-b1

# Create from a specific commit
git branch dev-b1 abc1234

# Create from a remote branch
git switch --track origin/dev-b1
```

Creating from a remote branch with `--track` automatically sets up upstream tracking, so future pulls work without specifying the remote.

## Push branches

``` bash
# Push specific branch and set upstream
git push -u origin dev-b1

# Push all branches
git push origin --all

# Push all branches and tags
git push origin --all --tags

# Delete a remote branch
git push origin --delete dev-b1
```

Always use `-u` on the first push to establish upstream tracking. This makes future `git pull` commands work without arguments.

## Merge branches

``` bash
# Switch to target branch first
git switch rc

# Merge another branch into current branch
git merge dev-b1

# Merge with explicit commit message
git merge dev-b1 -m "Merge dev-b1 into rc"

# Create merge commit even if fast-forward is possible
git merge --no-ff dev-b1

# Fast-forward only (fail if not possible)
git merge --ff-only dev-b1

# Abort if conflicts are complex
git merge --abort
```

Use `--no-ff` for feature branches to preserve history. Use `--ff-only` when merging into main to ensure linear history. Always push after merging: `git push origin rc`.

## Cherry-pick specific commits

``` bash
# Apply a single commit
git cherry-pick abc1234

# Apply multiple commits
git cherry-pick abc1234 def5678

# Apply a range (inclusive)
git cherry-pick abc1234^..def5678

# Continue after resolving conflicts
git cherry-pick --continue

# Abort if unresolvable
git cherry-pick --abort
```

Cherry-picking is useful for backporting critical fixes or applying specific changes to multiple branches. However, avoid it in team workflows—it duplicates commits and creates confusion. Prefer rebasing or merging for shared work.

## Rebase for linear history

``` bash
# Rebase current branch onto main
git rebase main

# Interactive rebase to squash or reorder commits
git rebase -i HEAD~3

# Continue after resolving conflicts
git rebase --continue

# Abort a rebase
git rebase --abort
```

Rebasing creates linear history but rewrites commits, changing their SHAs. **Never rebase shared or public branches.** Only rebase feature branches before merging to main. After rebasing, you must force-push: `git push origin feature-branch --force-with-lease` (safer than `--force`).

## Inspect branch state

``` bash
# Show branches merged into current branch
git branch --merged

# Show branches not yet merged
git branch --no-merged

# Show detailed tracking status
git branch -vv
```

Run `git branch --merged` before cleanup to identify which branches are safe to delete. Use `git branch --no-merged` to see active development branches.

## Clean up local branches

``` bash
# Delete a local branch
git branch -d dev-b1

# Force delete (even if unmerged)
git branch -D dev-b1

# Delete all merged branches
git branch --merged | grep -v "^\*\|main\|master" | xargs git branch -d

# Prune stale remote tracking branches
git fetch origin --prune
```

Always verify with `git branch --merged` before bulk deletion. The grep filter above excludes current branch (`^\*`) and main branches to prevent accidents. Run `git fetch --prune` regularly to clean up remote-deleted branches from your local tracking.
