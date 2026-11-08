---
title: "Fixing Git Pull on Feature Branches Without Tracking"
date: 2018-03-24 11:44:39 +0000
modified: 2026-04-12 14:25:37 +0000
author: "Eric Ma"
layout: post
categories: [scripting-utilities]
canonical: /how-to-pull-your-git-tree-after-creating-it-on-remote-server/
---

When you create a new branch locally and try to `git pull`, you’ll hit this error if the branch doesn’t have upstream tracking configured:

    You asked me to pull without telling me which branch you
    want to merge with, and 'branch.dev-harry.merge' in
    your configuration file does not tell me, either.

This happens because Git doesn’t automatically know which remote branch to pull from when you’re on a local branch without upstream tracking set. The `rc` branch works fine because it already has this configuration.

## The Problem

When you check your branches:

``` bash
$ git branch
* dev-harry
  master
  rc
```

And try to pull:

``` bash
$ git pull
```

Git needs to know: “Pull from which remote?” and “Which remote branch should I merge?”

The `rc` branch works because its configuration already exists. You can verify this by checking git config:

``` bash
$ git config branch.rc.remote
origin
$ git config branch.rc.merge
refs/heads/rc
```

Your `dev-harry` branch is missing these settings.

## Solutions

**Option 1: Set upstream when pulling (one-time fix)**

``` bash
$ git pull origin dev-harry
```

This pulls from the `origin` remote and the `dev-harry` branch, but doesn’t create permanent tracking.

**Option 2: Set upstream tracking (recommended)**

``` bash
$ git branch --set-upstream-to=origin/dev-harry dev-harry
```

Or the shorter form:

``` bash
$ git branch -u origin/dev-harry
```

After this, `git pull` works without arguments.

**Option 3: Set upstream during checkout**

If you’re checking out a new branch that exists on the remote:

``` bash
$ git checkout --track origin/dev-harry
```

This creates the local branch and sets upstream tracking in one command.

**Option 4: Configure manually in .git/config**

Edit `.git/config` directly and add:

``` ini
[branch "dev-harry"]
    remote = origin
    merge = refs/heads/dev-harry
```

Then save and `git pull` will work.

## Verify Your Configuration

After setting upstream, confirm it’s correct:

``` bash
$ git branch -vv
* dev-harry 1a2b3c4 [origin/dev-harry] your commit message
  master   4d5e6f7 [origin/master] another message
  rc       7g8h9i0 [origin/rc] yet another message
```

The `[origin/branch-name]` part shows tracking is configured.

## Best Practice for New Branches

When creating and pushing a new branch to a remote, use:

``` bash
$ git push -u origin dev-harry
```

The `-u` flag automatically sets upstream tracking as you push. This saves setup work later.

## Git Best Practices

When working with Git, follow these practices for a cleaner history:

- Write clear, descriptive commit messages that explain what changed and why
- Make small, focused commits rather than large sweeping changes
- Use branches for features and experiments, merge or rebase when ready
- Review changes with git diff before committing
- Use .gitignore to exclude build artifacts and environment files

## Useful Git Aliases

Speed up your workflow with these aliases in ~/.gitconfig:

```wp-block-code
[alias]
    st = status
    co = checkout
    br = branch
    ci = commit
    lg = log --oneline --graph --decorate
    last = log -1 HEAD
    unstage = reset HEAD --
    amend = commit --amend --no-edit
```

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.
