---
title: "View a File at a Specific Git Commit"
date: 2018-03-24 11:41:58 +0000
layout: post
canonical: https://www.systutorials.com/how-to-view-a-file-at-a-specific-commit-in-git/
---

Sometimes you need to view a file as it existed at a specific commit in Git — without checking out that commit or modifying your working directory. Git provides several ways to do this.

## View a File at a Specific Commit

```wp-block-code
# View file content at a specific commit
git show commit_hash:path/to/file

# Example
git show a1b2c3d:src/main.py
```

This outputs the file content to your terminal. You can pipe it to other commands:

```wp-block-code
# Save to a file
git show a1b2c3d:src/main.py > old_main.py

# Search within the old version
git show a1b2c3d:src/main.py | grep "function_name"

# View with syntax highlighting (if you have bat installed)
git show a1b2c3d:src/main.py | bat -l python
```

## Using git show with Branch Names

```wp-block-code
# View file on a different branch
git show feature-branch:src/main.py

# View file at a tag
git show v2.0:src/main.py

# View file relative to HEAD (one commit back)
git show HEAD~1:src/main.py
```

## Browse Files Interactively

Use `git restore` or `git cat-file` for more interactive exploration:

```wp-block-code
# List files in a commit's tree
git ls-tree commit_hash

# List files in a specific directory at that commit
git ls-tree commit_hash src/

# Cat a file by its blob hash
git cat-file -p blob_hash
```

## Compare File Between Commits

```wp-block-code
# Diff a file between two commits
git diff commit1 commit2 -- path/to/file

# Diff between current and previous commit
git diff HEAD~1 HEAD -- src/main.py

# See only changed lines with context
git diff commit1 commit2 --stat -- path/to/file
```

## Checkout a File from a Specific Commit

To actually restore a file from a past commit into your working directory:

```wp-block-code
# Restore file from a specific commit (modern Git)
git restore --source commit_hash path/to/file

# Or the older command
git checkout commit_hash -- path/to/file
```

**Warning:** This overwrites the current version of the file. Make sure you’ve committed or stashed any changes you want to keep.

## Using git blame for Line-Level History

See which commit last modified each line:

```wp-block-code
# Blame with commit info
git blame path/to/file

# Blame a specific line range
git blame -L 10,30 path/to/file

# Follow renames
git blame -C path/to/file
```

## View Deleted Files

If a file was deleted and you want to see its last version:

```wp-block-code
# Find the commit that deleted the file
git log --all --full-history -- path/to/deleted_file

# View the file just before deletion (parent of deletion commit)
git show deletion_commit^:path/to/deleted_file

# Restore the deleted file
git restore --source deletion_commit^ path/to/deleted_file
```

## Using Git GUI Tools

Several GUI tools make browsing historical files easier:

```wp-block-code
# Built-in Git GUI
gitk path/to/file

# Git's web interface
git instaweb --httpd=webrick

# VS Code GitLens extension shows inline blame and file history
```

## Quick Reference

- `git show hash:path` — View file at a commit
- `git show branch:path` — View file on a branch
- `git diff c1 c2 -- path` — Compare file between commits
- `git restore --source hash path` — Restore file from commit
- `git blame path` — Line-level history
- `git log -- path` — Find commits that touched a file

## Bisect to Find When a File Changed

If you know a file content changed but do not know which commit, use git bisect to find it with binary search:

```wp-block-code
git bisect start
git bisect bad HEAD
git bisect good v1.0
# Git checks out a middle commit
git show HEAD:path/to/file
# Tell Git if good or bad
git bisect good
# Repeat until found
git bisect reset
```

Binary search finds the offending commit in log(N) steps instead of checking every commit manually.

## Using git log for File History

Find all commits that modified a specific file:

```wp-block-code
# Full history
git log --follow -- path/to/file

# One-line with dates
git log --oneline --follow --date=short -- path/to/file

# Show changes at each commit
git log -p -- path/to/file

# Find when a string was added/removed
git log -S "function_name" -- path/to/file
```

The -S flag (pickaxe) finds when a specific function, variable, or string was introduced or removed from a file.
