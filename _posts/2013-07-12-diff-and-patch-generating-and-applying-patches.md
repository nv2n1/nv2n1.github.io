---
title: "Generating and Applying Patches with diff and patch"
date: 2013-07-12 16:32:33 +0000
modified: 2026-04-11 16:41:41 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /diff-and-patch-generating-and-applying-patches/
---

The `diff` utility generates unified diffs that show changes between file versions. Always use the `-u` flag to create unified diffs, which are the standard format for patches.

For a single file:

``` bash
diff -u original.c new.c > fix.patch
```

For an entire directory tree:

``` bash
diff -rupN original/ new/ > patchfile.patch
```

The flags break down as:

- `-r`: recurse into directories
- `-u`: unified diff format (required for patches)
- `-p`: show function names in diff headers
- `-N`: treat absent files as empty

A unified diff includes three lines of context around changes by default. You can adjust this with `-U`:

``` bash
diff -rupN -U5 original/ new/ > detailed.patch
```

### Handling binary files

If your tree includes binary files, `diff` will flag them but won’t generate usable patches. You have two options:

``` bash
# Exclude binary files entirely
diff -rupN --binary original/ new/ > patchfile.patch

# Use git diff for better binary handling
git diff > changes.patch
```

## Applying Patches with patch

The `patch` utility reads a diff file and applies changes to your source tree. The critical parameter is `-p`, which strips leading path components.

Basic application to a file:

``` bash
patch < fix.patch
```

If the patch doesn’t contain the target filename, specify it:

``` bash
patch myfile.c < fix.patch
```

### Understanding the -p level

When applying patches to a directory structure, you need to strip the correct number of path components. If your patch was created with:

``` bash
diff -rupN original/src/mm/page.c new/src/mm/page.c > mm.patch
```

The patch contains paths like `original/src/mm/page.c`. If you’re applying it in a directory where the actual file is at `src/mm/page.c`, use `-p1` to strip the first component (`original/`):

``` bash
patch -p1 < mm.patch
```

If applying from the root of a larger tree, adjust accordingly:

``` bash
# Strip two components: original/ and src/
patch -p2 < mm.patch
```

Use `--dry-run` to preview changes without applying them:

``` bash
patch -p1 --dry-run < mm.patch
```

### Reversing patches

Remove a previously applied patch with the `-R` flag:

``` bash
patch -p1 -R < mm.patch
```

## Modern alternatives

While `diff` and `patch` remain standard, modern workflows often use version control:

### Git-based patching

Generate patches with `git diff` or `git format-patch`:

``` bash
git diff > changes.patch
git format-patch -1 HEAD  # Creates a patch from the last commit
```

Apply with `git apply` or `git am`:

``` bash
git apply changes.patch
git am < formatted-patch
```

The `git am` command (apply mailbox) is preferred for commit history preservation.

### When to use diff/patch vs git

Use traditional `diff`/`patch` for:

- Projects without version control
- Distributing patches to users who don’t use git
- Simple one-file fixes

Use git for:

- Collaborative development
- Maintaining patch history
- Complex multi-commit changes

## Practical example

Create a patch from changes in your working directory:

``` bash
# Make changes to files in original/
cp -r original backup
# ... edit files in original/ ...
diff -rupN backup/ original/ > my-changes.patch
```

Apply to a fresh copy:

``` bash
cp -r original test-apply
cd test-apply
patch -p1 < ../my-changes.patch
```

Test with `--dry-run` first:

``` bash
cd test-apply
patch -p1 --dry-run < ../my-changes.patch
```

If the dry-run succeeds, apply for real. If it reports failures, check that `-p` levels match your directory structure.

## Common issues

**“patch: \*\*** malformed patch”\*\* — The file isn’t a valid diff. Verify it was created with `diff -u` and hasn’t been corrupted.

**“Hunk FAILED”** — The patch doesn’t match the target file. This happens when the file has been modified since the patch was created. Use `--verbose` to see what `patch` is trying to match, or use `fuzz` to be more lenient:

``` bash
patch -p1 --fuzz=2 < file.patch
```

**“patch: \*\*** can’t find file to patch”\*\* — The `-p` level is wrong. Test with `--dry-run` and adjust the number of path components.
