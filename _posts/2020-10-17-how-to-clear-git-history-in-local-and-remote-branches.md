---
title: "Clearing Git History: Local and Remote Branches"
date: 2020-10-17 13:06:25 +0000
layout: post
canonical: https://www.systutorials.com/how-to-clear-git-history-in-local-and-remote-branches/
---

Git tracks every commit, allowing you to inspect the full change history of a repository. However, this history accumulates storage overhead—especially problematic when large files were accidentally committed. If you need to discard all history and keep only the current code state, you can rebuild a branch with a single commit.

This approach works by creating an orphaned branch, committing current files to it, and replacing the original branch. It’s commonly needed for accidentally-versioned large binaries, credentials, or when migrating a repository to a fresh state.

## Clear the Master (or Main) Branch

Start in your cloned repository. First, identify which branch you want to clear—most modern repos use `main` instead of `master`.

``` bash
git checkout --orphan tmp-clean
```

The `--orphan` flag creates a branch with no parent commits, giving you a clean slate. Your working directory files remain intact, but git history is disconnected.

``` bash
git add -A
git commit -m "Initial commit"
```

Add all current files and make your first commit on this temporary branch.

``` bash
git branch -D master  # or 'main' if that's your primary branch
git branch -m master  # rename tmp-clean to master
```

Delete the old branch and rename the temporary branch to take its place.

``` bash
git push -f origin master
```

Force push to the remote. The `-f` flag is required because you’ve rewritten history. Coordinate with your team before doing this on shared repos.

**Alternative for `main` branches:**

If your repository uses `main` instead of `master`, adjust accordingly:

``` bash
git checkout --orphan tmp-clean
git add -A
git commit -m "Initial commit"
git branch -D main
git branch -m main
git push -f origin main
```

## Clean Up Your Working Repository

After the force push, your local clone still references old commits. Clean it up:

``` bash
git branch -u origin/master master  # set tracking branch
git gc --aggressive --prune=now
```

The `git gc` command performs garbage collection, removing unreachable objects and reclaiming disk space. `--prune=now` immediately deletes dangling commits instead of waiting 2 weeks.

## Update Other Repository Clones

Any other cloned copies still have the old history. Force them to match the remote:

``` bash
git fetch --all
git reset --hard origin/master
```

Run these commands in each affected clone. The `reset --hard` discards local changes and aligns with the remote state.

**For clones tracking `main`:**

``` bash
git fetch --all
git reset --hard origin/main
```

## Important Considerations

- **Backup first**: Force pushing rewrites history permanently. Create a backup clone before proceeding.
- **Notify your team**: Anyone with local clones must run the fetch/reset commands. This causes merge conflicts if anyone has unpushed work.
- **Check for large files**: If your goal is removing accidentally-committed large files, consider `git filter-repo` instead. History rewriting alone doesn’t reduce repository size if large files remain in the new single commit. You’d need to actually remove those files before committing to the orphan branch.
- **Refs and tags**: This process doesn’t remove old tag references. Use `git push origin --delete refs/tags/tagname` if needed.
- **CI/CD pipelines**: Update any deployment scripts or build systems that may reference old commit SHAs.

## Using BFG as an Alternative

For removing specific large files without clearing all history, `bfg` is faster than `filter-repo`:

``` bash
bfg --delete-files large-file.iso repo.git
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

This approach preserves most history while surgically removing problem files.
