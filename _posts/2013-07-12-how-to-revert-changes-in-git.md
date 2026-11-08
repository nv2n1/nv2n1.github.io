---
title: "How to Undo Git Commits and Changes"
date: 2013-07-12 16:32:21 +0000
modified: 2026-04-12 04:41:22 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-revert-changes-in-git/
---

Mistakes happen during development. Git provides several commands to undo changes at different stages—before committing, after committing, or in specific files. Understanding which tool to use depends on where you are in the workflow.

## Revert the entire working tree before committing

If you’ve made changes to multiple files and want to discard everything back to the last commit:

``` bash
git reset --hard HEAD
```

This restores all tracked files to their committed state. Untracked files remain untouched—use `git clean -f` if you want to remove those too.

**Warning:** `--hard` is destructive. Once executed, unsaved changes are gone. If there’s any chance you’ll need the changes later, use `git stash` instead:

``` bash
git stash
```

Then retrieve them later with `git stash pop`.

## Revert changes to a particular file before committing

If you’ve modified a file but haven’t staged it yet:

``` bash
git checkout HEAD -- working_file
```

Or the shorter form (though less explicit):

``` bash
git restore working_file
```

`git restore` is the modern approach introduced in Git 2.23 and is preferred for clarity—it’s explicit about restoring files rather than switching branches.

## Remove a file from the staging area

If you’ve accidentally staged a file with `git add`:

``` bash
git reset working_file
```

The file remains in your working tree with changes intact. Then delete it if needed:

``` bash
rm working_file
```

Alternatively, use the modern command:

``` bash
git restore --staged working_file
```

## Revert changes to a specific file after committing

To restore a single file to its state in a previous commit:

``` bash
git checkout <commit> -- working_file
git restore --source=<commit> working_file
```

Replace `<commit>` with a commit hash, tag, or reference:

``` bash
git checkout HEAD^ -- working_file      # previous commit
git checkout HEAD~3 -- working_file     # three commits back
git checkout v1.2.0 -- working_file     # specific tag
git checkout main -- working_file       # from another branch
```

The `--source` syntax is the newer `restore` equivalent and is clearer about intent.

## Undo a commit entirely

To remove a commit and rewrite history (only use on unpushed commits):

``` bash
git reset --hard HEAD~1
```

This deletes the last commit. Use `HEAD~N` to go back N commits.

## Undo a commit but keep its changes

If you want to uncommit work without losing it:

``` bash
git reset --soft HEAD~1
```

Changes return to the staging area, allowing you to re-commit with corrections.

## Revert a commit with a new commit (safe for shared branches)

If the commit is already pushed, create a new commit that undoes it:

``` bash
git revert <commit-hash>
```

This opens an editor for the revert commit message. For public branches, this is safer than `reset` since it preserves history. Example:

``` bash
git log --oneline  # find the commit
git revert abc1234
```

## Recover a deleted file

If you deleted a file but haven’t committed the deletion:

``` bash
git restore deleted_file
```

Or the older syntax:

``` bash
git checkout deleted_file
```

If you’ve already committed the deletion, restore it from a specific commit:

``` bash
git restore --source=HEAD~1 deleted_file
```

Then stage and commit it back.

## Clean up untracked files

Untracked files (new files never added to git) can accumulate. Preview what will be removed:

``` bash
git clean -n
```

Then remove them:

``` bash
git clean -f
```

Use `-d` to also remove untracked directories:

``` bash
git clean -fd
```

Be careful—untracked files can’t be recovered this way.

## View and checkout older versions

To see commit history:

``` bash
git log --oneline
```

To inspect a specific older version (enters detached HEAD state):

``` bash
git checkout <commit-hash>
```

Create a branch from this point if you want to keep working:

``` bash
git checkout -b recovery-branch
```

To return to your main branch:

``` bash
git checkout main
```

## Quick reference

| Goal                          | Command                                |
|-------------------------------|----------------------------------------|
| Discard unstaged file changes | `git restore <file>`                   |
| Unstage a file                | `git restore --staged <file>`          |
| Undo last commit (unpushed)   | `git reset --soft HEAD~1`              |
| Delete last commit entirely   | `git reset --hard HEAD~1`              |
| Undo pushed commit safely     | `git revert <hash>`                    |
| Restore file from old commit  | `git restore --source=<commit> <file>` |
| Remove untracked files        | `git clean -fd`                        |
| Discard all unstaged changes  | `git restore .`                        |

Always use `git status` and `git diff` before destructive operations to confirm what you’re about to change. When in doubt, `git stash` buys you time to think.
