---
title: "Git Branching Strategies: Create, Merge, and Manage Branches"
date: 2018-03-24 11:40:51 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /git-branching-tutorial/
---

Git branching is fundamental to modern development workflows. A branch is a lightweight pointer to a commit that lets you work on multiple features, fixes, or experiments in parallel without affecting the main codebase. Understanding branching well is essential for team collaboration and maintaining a clean project history.

## Creating and Switching Branches

Create a new branch:

``` bash
git branch feature-name
```

Switch to that branch:

``` bash
git checkout feature-name
```

Combine both in one command:

``` bash
git checkout -b feature-name
```

In Git 2.23+, the `switch` command is the preferred approach—it’s cleaner and more explicit than `checkout`, which conflates multiple operations:

``` bash
git switch -c feature-name
```

To switch to an existing branch:

``` bash
git switch feature-name
```

## Listing and Viewing Branches

View all local branches:

``` bash
git branch
```

View all branches including remotes:

``` bash
git branch -a
```

See the current branch name:

``` bash
git branch --show-current
```

Get a visual representation of your branching history:

``` bash
git log --graph --decorate --oneline --all
```

Compare specific branches to see what commits differ:

``` bash
git log main..feature-name
```

This shows commits in `feature-name` that aren’t in `main`.

## Merging Branches

Switch to the target branch (usually `main` or `develop`):

``` bash
git switch main
git merge feature-name
```

By default, Git performs a fast-forward merge if possible. To preserve the branch as a separate line of history, use `--no-ff`:

``` bash
git merge --no-ff feature-name
```

This creates a merge commit even when fast-forward is possible, which is useful in shared repositories where you want explicit record of integration points.

For a cleaner history in fast-moving projects, use squash merge to combine all commits into one:

``` bash
git merge --squash feature-name
git commit -m "Add feature-name"
```

Or use rebase-based merging (if your workflow supports it):

``` bash
git rebase main feature-name
git switch main
git merge feature-name
```

## Handling Merge Conflicts

When changes conflict, Git marks the conflicting sections:

    <<<<<<< HEAD
    your changes
    =======
    incoming changes
    >>>>>>> feature-name

Edit the file to resolve conflicts, keeping the code you want. Then stage and commit:

``` bash
git add conflicted-file.txt
git commit -m "Resolve merge conflicts in conflicted-file.txt"
```

To abort a merge entirely:

``` bash
git merge --abort
```

For complex conflicts, use a merge tool:

``` bash
git mergetool
```

## Managing Remote Branches

Fetch updates from the remote without merging or changing your working directory:

``` bash
git fetch origin
```

List remote branches:

``` bash
git branch -r
```

Track a remote branch locally:

``` bash
git switch feature-name
```

Git automatically creates a local tracking branch if a matching remote branch exists.

Or explicitly set up tracking:

``` bash
git branch --track feature-name origin/feature-name
```

Push a local branch to remote:

``` bash
git push -u origin feature-name
```

The `-u` flag sets upstream tracking automatically.

Push all branches to remote:

``` bash
git push origin --all
```

## Deleting Branches

Delete a local branch (safe—only works if merged):

``` bash
git branch -d feature-name
```

Force delete without checking merge status:

``` bash
git branch -D feature-name
```

Delete a remote branch:

``` bash
git push origin --delete feature-name
```

Or use the shorthand:

``` bash
git push origin :feature-name
```

## Branching Strategies

**Feature Branch Workflow**: Create a new branch for each feature or fix. Merge back to main when complete. Works well for small teams.

``` bash
git switch -c feature/user-authentication
# work and commit
git switch main
git merge feature/user-authentication
```

**Git Flow**: Uses multiple long-lived branches (`main`, `develop`, `release/*`, `hotfix/*`). Suits larger projects with scheduled releases and complex workflows.

**Trunk-Based Development**: Keep a single main branch, merge frequently with short-lived feature branches (1-2 days max). Ideal for continuous deployment pipelines.

**GitHub Flow**: Single main branch, feature branches, pull requests for review, merge to main. Simple and effective for most modern projects.

Choose a strategy based on your team size, release cycle, and CI/CD maturity.

## Best Practices

- **Keep branches focused**: Each branch should address exactly one feature, bugfix, or experiment.
- **Use descriptive names**: Prefix with `feature/`, `bugfix/`, `hotfix/`, or `chore/` followed by a short description. Example: `feature/kafka-consumer-retry-logic`.
- **Delete after merging**: Remove merged branches regularly to reduce noise. Most tools have cleanup options.
- **Fetch before pushing**: Run `git fetch` to sync with remote changes before pushing your work.
- **Use pull requests**: Have teammates review changes before merging to shared branches. This catches bugs, spreads knowledge, and maintains code quality.
- **Keep commits clean**: Squash or rebase before merging to avoid cluttering history with work-in-progress commits.
- **Protect main branch**: Use repository settings to require pull request reviews and passing tests before merging to main.

## Checking Branch Status

See all branches with their upstream tracking status:

``` bash
git branch -vv
```

This shows which remote branch each local branch tracks and whether it’s ahead or behind.

Get a quick overview of unpushed commits:

``` bash
git log origin/main..main
```

This shows commits on your local main that haven’t been pushed yet.
