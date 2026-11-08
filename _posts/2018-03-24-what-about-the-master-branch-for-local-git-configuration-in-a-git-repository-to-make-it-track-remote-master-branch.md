---
title: "Setting Up Git Branch Tracking for Remote Branches"
date: 2018-03-24 11:46:04 +0000
modified: 2026-04-12 16:09:11 +0000
author: "Eric Ma"
layout: post
categories: [scripting-utilities]
canonical: /what-about-the-master-branch-for-local-git-configuration-in-a-git-repository-to-make-it-track-remote-master-branch/
---

By default, Git doesn’t automatically configure your local branch to track its remote counterpart. You need to explicitly set up this tracking relationship so that `git pull` and `git push` know which remote branch to synchronize with.

## Setting Up Tracking for an Existing Branch

If you already have a local branch and want it to track a remote branch, use:

``` bash
git branch --set-upstream-to=origin/main main
```

Replace `main` with your actual branch name if it’s different. This command configures your local `main` branch to track `origin/main`.

You can verify the tracking relationship with:

``` bash
git branch -vv
```

This shows all branches with their tracking status. Output looks like:

    * main          a1b2c3d [origin/main] Your commit message
      develop       f4e5d6c [origin/develop] Another commit
      feature-x     g7h8i9j no tracking branch

## Setting Up Tracking During Checkout

When switching to a remote branch that doesn’t exist locally, Git can automatically create a local tracking branch:

``` bash
git checkout main
```

If `main` doesn’t exist locally but `origin/main` does, Git creates it and sets up tracking automatically. This is the simplest approach for new work.

## Setting Up Tracking During Push

When pushing a new branch for the first time, use the `-u` flag:

``` bash
git push -u origin feature-branch
```

This pushes your branch and sets up tracking in one step. Without `-u`, the branch gets pushed but `git pull` won’t know where to pull from later.

## Shorthand: git branch -u

You can use `-u` as a shorthand for `--set-upstream-to`:

``` bash
git branch -u origin/main main
```

## Checking Your Current Tracking Configuration

To see what your branch is tracking:

``` bash
git branch -vv
```

Or check the Git config directly:

``` bash
git config branch.main.remote
git config branch.main.merge
```

## Default Branch Names

Most repositories now use `main` as the default branch instead of `master`. When you clone a repository, Git automatically checks out the default branch and sets up tracking for it. If you’re working with an older repository still using `master`, the same commands apply—just substitute `master` for `main`.

## Why This Matters

With tracking set up correctly:

- `git pull` knows which remote branch to fetch and merge from
- `git push` defaults to the correct remote branch
- `git status` shows how many commits you’re ahead or behind the remote
- Tools and scripts can determine the upstream branch automatically

Without tracking, you’d need to explicitly specify the remote and branch name every time: `git pull origin main` instead of just `git pull`.

## Git Workflow Tips

Effective Git usage goes beyond knowing individual commands. Consider adopting a branching strategy that suits your team size. Feature branching works well for small teams, while GitFlow or trunk-based development scales better for larger organizations.

Always write descriptive commit messages. A good commit message explains what changed and why, not just what. Use the imperative mood: “Add feature” not “Added feature”.

## Useful Git Shortcuts

Add these aliases to your Git configuration for faster daily workflows:

```wp-block-code
[alias]
    st = status -sb
    co = checkout
    br = branch -v
    lg = log --oneline --graph --decorate -20
    unstage = reset HEAD --
    amend = commit --amend --no-edit
    last = log -1 HEAD --stat
```

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
