---
title: "Handling Spaces in File Paths with rsync"
date: 2018-03-24 11:51:10 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /how-to-handle-spaces-in-paths-with-rsync-on-linux/
---

Spaces in file and directory paths are a common source of rsync failures. When paths contain spaces, the shell interprets them as argument separators unless you properly escape or quote them. Here’s how to handle this correctly.

## The core issue

When rsync receives an unquoted path with spaces, the shell splits it at each space. For example:

``` bash
rsync -av /home/user/my documents/ remote:/backup/
```

This gets interpreted as multiple arguments: `/home/user/my`, `documents/`, etc., causing rsync to fail or behave unexpectedly.

## Solution 1: Double quotes

The simplest approach is wrapping paths in double quotes:

``` bash
rsync -av "/home/user/my documents/" remote:/backup/
```

This works for most cases, but be careful with shell variables and special characters. If your path contains `$`, backticks, or backslashes, they may still be interpreted by the shell.

## Solution 2: Single quotes (safer for literal paths)

Single quotes prevent all shell expansion, making them safer when you don’t need variable substitution:

``` bash
rsync -av '/home/user/my documents/' remote:/backup/
```

Use this when paths are hardcoded and contain special characters.

## Solution 3: Escaping with backslash

You can escape individual spaces with backslashes, though this is more verbose:

``` bash
rsync -av /home/user/my\ documents/ remote:/backup/
```

This works but becomes tedious with multiple spaces. Not recommended for complex paths.

## Solution 4: Using `--files-from` (best for batch operations)

When syncing multiple paths with spaces, create a file list instead of passing paths as arguments:

``` bash
cat > /tmp/rsync-list.txt << 'EOF'
/home/user/my documents
/home/user/project files
/var/log/old archives
EOF

rsync -av --files-from=/tmp/rsync-list.txt / remote:/backup/
```

The `--files-from` option reads paths from a file, avoiding shell argument parsing entirely. This is the most reliable approach for scripted backups.

## Solution 5: The `find` approach with NUL separator

For automated scripts processing many files, use find with NUL-terminated output:

``` bash
find /home/user -type f -print0 | rsync -av --files-from=- --from0 / remote:/backup/
```

The `-print0` flag outputs filenames separated by NUL bytes instead of newlines, which rsync handles correctly with `--from0`. This avoids all shell interpretation.

## Practical example: backing up a directory tree

``` bash
rsync -avz --delete "/home/user/my project/" backup.server:/backups/my-project/
```

The trailing slash after the source path is important — it tells rsync to copy the contents, not the directory itself.

## Remote paths with spaces

Remote paths work the same way, but quote them carefully since SSH is involved:

``` bash
rsync -av "/local/path/" "user@remote:/remote/path with spaces/"
```

Wrap both local and remote paths in quotes.

## Common pitfalls

**Don’t forget quotes in scripts** — even in bash scripts, use quotes. Unquoted variables and globs expand before rsync receives them:

``` bash
# Wrong
rsync -av $source_path remote:/backup/

# Right
rsync -av "$source_path" remote:/backup/
```

**Be careful with glob patterns** — if your path contains wildcards, single quotes prevent them from expanding:

``` bash
# This expands the glob before rsync sees it
rsync -av /home/user/my *files/ remote:/backup/

# This passes the literal asterisk to rsync (usually not what you want)
rsync -av '/home/user/my *files/' remote:/backup/
```

**Verify your paths** — test with `rsync --dry-run` first:

``` bash
rsync -avz --dry-run "/home/user/my documents/" remote:/backup/
```

## Summary

For most interactive use, double or single quotes around paths are sufficient. For production scripts and automation, use `--files-from` or `--from0` with find to eliminate shell parsing altogether. Always test with `--dry-run` before running actual syncs, especially when handling many files or complex directory structures.
