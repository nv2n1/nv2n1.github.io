---
title: "Git Patches: Create, Apply, and Debug Issues"
date: 2018-03-24 11:41:06 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/patching-with-git/
---

The standard way to generate patches from git commits is `git format-patch`. This creates email-ready patch files that include commit messages, author information, and metadata.

``` bash
# Create a patch from the last commit
git format-patch -1

# Create patches for the last N commits
git format-patch -3

# Create patches from a specific commit onwards
git format-patch abc1234..HEAD

# Create patches from a range of commits
git format-patch abc1234..def5678

# Output patches to a directory
git format-patch -o /tmp/patches -1
```

The `-1` flag tells git how many commits back to start from. Each commit generates a separate numbered patch file like `0001-commit-message.patch`.

For a single logical change across multiple commits, use `--stdout` to combine them:

``` bash
git format-patch -3 --stdout > my-feature.patch
```

## Customizing patch output

Control what gets included in your patches:

``` bash
# Include a cover letter (useful for series)
git format-patch -3 --cover-letter

# Use a custom prefix instead of "PATCH"
git format-patch -3 --subject-prefix="RFC"

# Number patches even if there's only one
git format-patch -1 -N

# Include diffstat
git format-patch -1 --stat

# Sign patches with GPG
git format-patch -1 -S

# Create patches with a custom subject line format
git format-patch -1 --pretty=format:"%h %s"
```

## Applying patches

Use `git apply` for simple patches or `git am` (apply mail) for patches created with `git format-patch`. The key difference: `git am` preserves commits and metadata, while `git apply` just applies the diff without creating new commits.

### With git am (preferred for format-patch)

`git am` handles email headers, author info, and commit metadata properly:

``` bash
# Apply a single patch
git am 0001-fix-bug.patch

# Apply all patches in a directory
git am /tmp/patches/*.patch

# Continue after resolving conflicts
git am --continue

# Skip a problematic patch
git am --skip

# Abort the entire operation
git am --abort

# Apply without verifying GPG signatures
git am --no-verify

# Apply and sign commits with your GPG key
git am -S
```

### With git apply

`git apply` just applies the diff without creating commits. Useful for non-git projects, testing changes before committing, or applying partial diffs:

``` bash
# Apply a patch
git apply my-patch.patch

# Check if a patch applies cleanly (dry run)
git apply --check my-patch.patch

# Apply with whitespace fixes (tabs/spaces)
git apply --whitespace=fix my-patch.patch

# Reverse a patch
git apply -R my-patch.patch

# Apply with strict whitespace checking
git apply --whitespace=error my-patch.patch
```

## Handling patch conflicts

When patches don’t apply cleanly due to conflicting changes, resolve them manually:

``` bash
# After resolving conflicts in your editor
git add .
git am --continue

# Or to edit the commit message during apply
git am --allow-empty

# Abort if things get messy
git am --abort
```

For complex scenarios, use `git apply --reject` to generate `.rej` files for manual inspection:

``` bash
git apply --reject my-patch.patch

# Review the .rej files
cat file.rej

# Manually fix the changes, then add and commit
git add .
git commit
```

If you’re applying a series of patches and one fails, you have options:

``` bash
# Skip just that one patch and continue with the rest
git am --skip

# Reset and try a different approach (e.g., cherry-pick instead)
git am --abort
git cherry-pick abc1234..def5678
```

## Patch workflow example

A typical workflow for receiving and testing patches:

``` bash
# Create a feature branch for testing
git checkout -b test-patch

# Apply patches with am (preserves commits)
git am /path/to/patches/*.patch

# Review changes
git log --oneline -5
git diff main..HEAD

# If everything looks good, merge to main
git checkout main
git merge test-patch

# If there are issues, abort and try again
git am --abort
git checkout test-patch
```

## Creating patches from uncommitted changes

To create a patch from your working directory without committing:

``` bash
# Patch of all unstaged changes
git diff > local-changes.patch

# Patch of staged changes only
git diff --cached > staged.patch

# Patch including both staged and unstaged
git diff HEAD > all-changes.patch

# Apply uncommitted patches with git apply
git apply local-changes.patch
```

This approach works well for sharing work-in-progress changes or applying changes across branches without creating intermediate commits.

## Combining patches and stashing

For temporary work, stashes can be cleaner than patches:

``` bash
# Save uncommitted changes to a stash
git stash

# Later, apply the stash
git stash pop

# Export a stash as a patch
git stash show -p stash@{0} > my-stash.patch
```

## Verifying patches before applying

Before applying patches from untrusted sources:

``` bash
# Preview a patch without applying it
git apply --check my-patch.patch

# Review the actual diff content
git diff < my-patch.patch

# Check patch statistics
git apply --stat my-patch.patch
```

If `git apply --check` reports errors, the patch won’t apply cleanly and you’ll need to manually adjust it or resolve conflicts during `git am`.
