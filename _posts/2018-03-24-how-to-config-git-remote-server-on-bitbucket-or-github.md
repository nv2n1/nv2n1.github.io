---
title: "Setting Up Git Remote Repositories on GitHub and Bitbucket"
date: 2018-03-24 11:50:02 +0000
author: "Weiwei Jia"
layout: post
categories: [testing-devops]
canonical: /how-to-config-git-remote-server-on-bitbucket-or-github/
---

When you initialize a new repository locally and try to push to GitHub or Bitbucket for the first time, you’ll likely encounter errors like:

    No refs in common and none specified; doing nothing.
    Perhaps you should specify a branch such as 'master'.
    fatal: The remote end hung up unexpectedly

This happens because your local repository has no upstream tracking branch configured. Git doesn’t know which remote branch to push to.

## Configure Your Remote

First, add your remote repository if you haven’t already:

``` bash
git remote add origin https://github.com/username/repo.git
```

For SSH (recommended for frequent pushes):

``` bash
git remote add origin git@github.com:username/repo.git
```

Verify the remote is set correctly:

``` bash
git remote -v
```

## Push and Set Upstream

For your first push, use `--set-upstream` to track the remote branch:

``` bash
git push --set-upstream origin master
```

Or use the shorter syntax:

``` bash
git push -u origin master
```

If you’re using `main` instead of `master` (the current GitHub default):

``` bash
git push -u origin main
```

After this initial push with `-u`, future pushes from that branch will work with just `git push` since the upstream is now configured.

## Check Your Configuration

View your current remote configuration:

``` bash
git remote show origin
```

This displays the fetch and push URLs, along with tracking branches.

## Change Existing Remote

If you need to update your remote URL (switching from HTTPS to SSH, for example):

``` bash
git remote set-url origin git@github.com:username/repo.git
```

Remove a remote entirely:

``` bash
git remote remove origin
```

## Multiple Remotes

You can push to multiple repositories. Add additional remotes:

``` bash
git remote add backup https://bitbucket.org/username/repo.git
git push backup main
```

## Push All Branches

If you want to push all branches and tags at once during initial setup:

``` bash
git push -u origin --all
git push -u origin --tags
```

## SSH Key Setup (Recommended)

For Bitbucket and GitHub, SSH is more convenient than HTTPS after initial setup. Ensure your SSH key is added to your account:

1.  Generate a key if needed: `ssh-keygen -t ed25519 -C "your_email@example.com"`
2.  Add the public key to your GitHub/Bitbucket account settings
3.  Test the connection: `ssh -T git@github.com`

Once SSH is configured, cloning with `git clone git@github.com:username/repo.git` and pushing requires no password authentication.

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
