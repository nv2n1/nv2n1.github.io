---
title: "Clone a Git Branch with Shallow History"
date: 2018-03-24 11:42:06 +0000
modified: 2026-04-12 16:04:38 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-clone-a-snapshot-of-a-remote-repository-at-a-specific-branch/
---

When you need just the files from a specific branch without downloading the entire repository history, use shallow cloning. This is useful for large repositories where full history takes time to transfer, or when you only care about the current state of a particular branch.

The core command is:

``` bash
git clone -b branch-name <repository-url> --depth 1
```

For example, to clone branch `develop` from a remote repository:

``` bash
git clone -b develop git@github.com:user/repo.git --depth 1
```

The flags work as follows:

- `-b develop` checks out the specified branch immediately after cloning
- `--depth 1` creates a shallow clone with only 1 commit of history (the current HEAD)

## Why shallow cloning matters

**Large repositories with long histories**: Cloning the entire history of a mature project can take significant time and disk space. A shallow clone downloads only what you need.

**CI/CD pipelines**: Build systems often use shallow clones to speed up job startup times.

**Feature branch work**: If you’re only working on a specific branch, you don’t need the history of master or other branches.

## Going deeper: common shallow clone scenarios

Clone with more history depth if you need to see recent commits:

``` bash
git clone -b develop git@github.com:user/repo.git --depth 10
```

Clone without specifying a branch (defaults to the remote’s default branch):

``` bash
git clone git@github.com:user/repo.git --depth 1
```

Convert a shallow clone to a full one:

``` bash
git fetch --unshallow
```

Fetch additional history after shallow cloning:

``` bash
git fetch --depth 20
```

## Alternative: using git archive

If you need just a snapshot of files without any git history at all, `git archive` is cleaner:

``` bash
git archive --remote=git@github.com:user/repo.git -b develop -o snapshot.zip HEAD
```

This creates a zip file of the branch contents without cloning the entire repository. It’s faster for simple file extraction but doesn’t give you a working git repository.

## Performance comparison

For a repository with thousands of commits:

- Full clone: several seconds to minutes, uses several hundred MB
- `--depth 1`: milliseconds to seconds, uses only a few MB
- `git archive`: seconds, uses minimal bandwidth but no git history

Shallow clones are the standard approach in modern CI/CD and for developers working with large projects. If you later need full history, `git fetch --unshallow` converts the shallow repository to a complete one.

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
