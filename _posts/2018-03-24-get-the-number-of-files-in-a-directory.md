---
title: "Counting Files in a Directory: Common Pitfalls and Best Practices"
date: 2018-03-24 08:21:39 +0000
modified: 2026-04-11 17:40:27 +0000
author: "Weiwei Jia"
layout: post
categories: [scripting-utilities]
canonical: /get-the-number-of-files-in-a-directory/
---

The most reliable one-liner to count files in the current directory is:

``` bash
find . -maxdepth 1 -type f | wc -l
```

This counts only regular files (not directories or symlinks) and handles edge cases that trip up simpler approaches.

## Why Not Use `ls | wc -l`?

The common `ls | wc -l` command has several problems:

- **Hidden files excluded by default** — dotfiles won’t be counted unless you use `ls -a`
- **Directory entries counted** — `.` and `..` get included with `-a`, inflating your count by 2
- **Fails on special characters** — filenames with newlines (possible in Unix) break the count
- **Spawns unnecessary processes** — pipes create subprocess overhead, mattering at scale
- **Unsorted output variability** — different shells and systems may behave differently

Use `ls | wc -l` only if you’re counting in a carefully controlled environment and understand its limitations.

## Reliable Approaches

### Using `find` (recommended for scripts)

Count only files, excluding directories:

``` bash
find . -maxdepth 1 -type f | wc -l
```

The `-maxdepth 1` limits to the current directory, `-type f` excludes directories, and `find` handles hidden files by default.

For recursive counting across subdirectories:

``` bash
find . -type f | wc -l
```

### Using `find` with `-printf` (avoids piping overhead)

``` bash
find . -maxdepth 1 -type f -printf '.' | wc -c
```

This outputs one character per file and counts characters instead of lines. Handles edge cases better than line-based counting and slightly faster on very large directories.

### Using bash arrays with globbing (simplest for interactive use)

``` bash
shopt -s nullglob
files=(*)
echo ${#files[@]}
```

This stores matching files in an array and returns the count. The `nullglob` option prevents echoing the glob pattern if no matches exist. Handles spaces and special characters correctly without spawning subprocesses.

For hidden files too:

``` bash
shopt -s nullglob
files=(* .[!.]*)
echo ${#files[@]}
```

The `.[!.]*` pattern matches dotfiles while excluding `.` and `..`.

### Counting by file type

Count only directories:

``` bash
find . -maxdepth 1 -type d | wc -l
```

Subtract 1 if you don’t want to include the current directory itself.

Count only symlinks:

``` bash
find . -maxdepth 1 -type l | wc -l
```

Count a specific file extension:

``` bash
find . -maxdepth 1 -name "*.txt" -type f | wc -l
```

## Performance Considerations

For directories with millions of files, even `find` can be slow. Consider these alternatives:

**Use `ls -U` (unsorted mode)** if you just need a rough count and speed matters:

``` bash
ls -U | wc -l
```

Unsorted listing is faster because it skips the sorting step. Accuracy suffers, but the speed gains are significant.

**Check filesystem metadata** on some systems:

``` bash
stat -c %h .
```

On ext4/btrfs, this returns the link count of the directory, which can indicate file count (though it’s not always exact). Not portable across filesystems.

**Cache the count in application logic** — if you’re checking frequently, maintain a counter in your monitoring or backup system rather than recounting every time.

## Common Pitfalls

**Forgetting `-maxdepth 1` with `find`** — you’ll get a recursive count across all subdirectories, which is usually not what you want.

**Using `-a` with `ls` and forgetting about `.` and `..`** — subtract 2 from the result, or use `ls -A` (capital A) which excludes them:

``` bash
ls -A | wc -l
```

**Globbing with no matches** — without `nullglob` in bash, `echo *.txt | wc -w` echoes the literal `*.txt` if no files match. Always enable `shopt -s nullglob` or check for matches first.

## Summary

For scripts and automation: use `find . -maxdepth 1 -type f | wc -l`

For interactive shells: use the array method with `shopt -s nullglob`

For one-off speed checks: use `ls -U | wc -l` (accepting inaccuracy)

Pick based on your precision requirements and performance constraints.
