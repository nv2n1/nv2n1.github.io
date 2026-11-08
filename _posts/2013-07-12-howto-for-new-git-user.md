---
title: "Getting Started with Git: A Beginner\u2019s Guide"
date: 2013-07-12 16:32:25 +0000
modified: 2026-04-11 16:42:24 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /howto-for-new-git-user/
---

Every user working with Git needs an SSH key pair for authentication. Generate one if you don’t have it:

``` bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

Ed25519 keys are preferred over RSA for better security and performance. The command creates `~/.ssh/id_ed25519` (private key) and `~/.ssh/id_ed25519.pub` (public key). Share the public key with your Git server administrator to set up your account.

Keep your private key secure—never share it or commit it to repositories.

## SSH Configuration for Non-Standard Ports

If your Git server runs SSH on a port other than 22, configure SSH to use it automatically. Add this to `~/.ssh/config`:

    Host example.org
        Port 22111
        User git
        IdentityFile ~/.ssh/id_ed25519

Set proper permissions on the config file:

``` bash
chmod 600 ~/.ssh/config
```

Now `git clone git@example.org:repo1.git` will automatically use port 22111.

## Initial Repository Setup

If you’re creating a new repository from scratch on your local machine before pushing to the server, start here. If you’re working with an existing repository, skip to the next section.

Initialize a local repository:

``` bash
mkdir repo1
cd repo1
git init
```

Create some initial content and commit it:

``` bash
touch README.md
git add README.md
git commit -m "Initial commit"
```

Add the remote server and push:

``` bash
git remote add origin git@example.org:repo1.git
git branch -M main
git push -u origin main
```

The `-u` flag sets up tracking, so future pushes to this branch won’t require specifying the remote and branch.

## Cloning and Working with Existing Repositories

Clone a repository for the first time:

``` bash
git clone git@example.org:repo1.git
cd repo1
```

This creates a local copy with the remote already configured as `origin`.

## Daily Workflow

**Sync with the latest changes:**

``` bash
git pull
```

This fetches and merges updates from the remote repository. Use `git pull --rebase` if you prefer rebasing over merging for a cleaner history.

**Stage your changes:**

``` bash
git add file1.txt directory/file2.txt
```

You can also use `git add .` to stage all modified files, but it’s safer to be explicit about what you’re committing.

**Commit with a descriptive message:**

``` bash
git commit -m "Fix authentication bug in login handler"
```

Write clear commit messages—future you will thank you. Keep the first line under 50 characters and add details below if needed.

**Push to the server:**

``` bash
git push
```

Since you cloned the repository and have tracking configured, this pushes your current branch to its upstream.

## Useful Commands

View your commit history:

``` bash
git log --oneline -10
```

Shows the last 10 commits in a compact format.

Check the status of your working directory:

``` bash
git status
```

Always run this before committing to ensure you’re staging what you intend.

See what changed in a specific commit:

``` bash
git show <commit-hash>
```

Compare your working directory to the last commit:

``` bash
git diff
```

Undo unstaged changes in a file:

``` bash
git checkout -- filename.txt
```

View which branch you’re on and create new ones:

``` bash
git branch
git branch feature-branch
git checkout feature-branch
```

Or create and switch in one command:

``` bash
git switch -c feature-branch
```

## Common Issues

**Permission denied error:** Verify your SSH key is added to your server account and that `ssh-agent` has it loaded:

``` bash
ssh-add ~/.ssh/id_ed25519
ssh-add -l
```

**Connection timeout:** Check that the port is correct in `~/.ssh/config` and that the server’s firewall allows connections.

**Changes rejected on push:** You may have diverged from the remote. Run `git pull` first, resolve any conflicts, then push again.

**Accidentally committed to the wrong branch:** Create a new branch from your current position, reset the old branch, and push:

``` bash
git branch feature-branch
git reset --hard origin/main
git checkout feature-branch
```

Refer to the Git documentation and `git help <command>` for detailed information on any command.
