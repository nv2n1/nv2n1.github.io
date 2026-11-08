---
title: "Renaming Git Branches Locally and Remotely"
date: 2018-11-15 08:47:45 +0000
modified: 2026-04-11 17:11:56 +0000
author: "Q A"
layout: post
categories: [testing-devops]
canonical: /how-to-rename-a-branch-name-in-the-remote-git-server/
---

Renaming a Git branch involves three steps: rename locally, push the new branch, and delete the old remote branch. How you do this depends on whether you’re working from the command line or your Git hosting platform’s UI.

## Rename the branch locally

The simplest command renames a branch in your local repository:

``` bash
git branch -m old-name new-name
```

If you’re currently on the branch you want to rename, you can omit the old name:

``` bash
git branch -m new-name
```

## Push the new branch and delete the old one

Once renamed locally, push the new branch to the remote and set upstream tracking:

``` bash
git push origin -u new-name
```

The `-u` flag sets the upstream branch, so future `git push` and `git pull` commands work without additional arguments.

Then delete the old branch from the remote:

``` bash
git push origin --delete old-name
```

## Quick combined workflow

Execute these in order:

``` bash
git branch -m old-name new-name
git push origin -u new-name
git push origin --delete old-name
```

The delete happens last since the new branch is already pushed. This sequence works whether you’re on the branch being renamed or elsewhere.

## Using the web UI

Most Git hosting platforms provide a direct rename option in their UI, which is useful if you have branch protection rules:

**GitHub:** Settings → Branches → click the pencil icon next to the branch name → enter the new name.

**GitLab:** Repository → Branches → click the pencil icon next to the branch name → enter the new name.

**Gitea:** Branches → click the three-dot menu → Rename → enter the new name.

**Gitea (older versions):** If the menu option isn’t available, use the command-line approach instead.

The UI approach handles all Git operations automatically and updates related CI/CD pipeline references, which is especially useful for protected branches.

## Renaming the default branch

If the branch is your repository’s default branch (typically `main` or `master`), change the default branch setting first. Most platforms prevent deletion of the default branch to avoid breaking clones and CI/CD workflows.

**GitHub:** Settings → Default branch → select a different branch, then proceed with the rename steps.

**GitLab:** Settings → Repository → Default branch → select a different branch, then proceed with the rename steps.

After changing the default, follow the standard rename workflow.

## Syncing after a remote rename

If a teammate renamed a remote branch or you need to update your local state, sync your local tracking branch:

``` bash
git fetch origin
git branch -m old-name new-name
git branch -u origin/new-name new-name
```

To also clean up stale local tracking branches:

``` bash
git fetch origin --prune
git branch -m old-name new-name
git branch -u origin/new-name new-name
```

The `--prune` flag removes local tracking branches for remote branches that no longer exist, keeping your local refs clean.

If you need to reset upstream tracking entirely:

``` bash
git branch --unset-upstream new-name
git branch -u origin/new-name new-name
```

## Handling branch protection rules

If your repository has branch protection rules that prevent force pushes or require pull request reviews, branch renames may be restricted at the repository level. Check your repository settings to see if branch rename operations are allowed for your role.

If you can’t rename via the command line due to protection rules, use the web UI — most platforms allow administrators and maintainers to rename protected branches through the settings panel.

## Renaming across multiple remotes

If you push to multiple remotes (e.g., `origin` and `upstream`), rename locally once, then push and delete on each remote separately:

``` bash
git branch -m old-name new-name
git push origin -u new-name
git push upstream -u new-name
git push origin --delete old-name
git push upstream --delete old-name
```

Verify the rename succeeded:

``` bash
git branch -a
```

This shows all local and remote-tracking branches.

## Troubleshooting

**Upstream not set after push:** If you pushed without the `-u` flag, set upstream manually:

``` bash
git branch -u origin/new-name
```

**Stale refs lingering locally:** After deleting the old remote branch, run `git fetch origin --prune` to clean up stale tracking references.

**Accidental push to wrong remote:** If you pushed the new branch to the wrong remote, delete it and push again:

``` bash
git push wrong-remote --delete new-name
git push correct-remote -u new-name
```
