---
title: "Finding Files Larger Than a Specific Size"
date: 2018-03-24 08:20:28 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-find-files-in-a-directory-that-are-larger-than-certain-size/
---

Finding large files is something you end up doing a lot — disk fills up, you need to track down what’s eating space, or you’re auditing a directory before archiving. The `find` command handles this cleanly.

## Basic usage

Find all files larger than 500MB under the current directory:

``` bash
find . -type f -size +500M
```

The `-type f` limits results to files only (skips directories). Without it, `find` might match directories that contain a lot of data but aren’t themselves large.

## Show file sizes

To see human-readable sizes alongside the filenames:

``` bash
find . -type f -size +500M -ls
```

The `-ls` action outputs in a format similar to `ls -l`, which is cleaner than piping through `ls` separately. If you prefer the output of `ls -lh`, you can use:

``` bash
find . -type f -size +500M -exec ls -lh {} \;
```

## Sort results by size

If you’re hunting for the biggest offenders, sort by size descending:

``` bash
find . -type f -size +100M -exec ls -lh {} \; | sort -rh
```

The `-h` flag in `sort` handles human-readable sizes (MB, GB) correctly. Without it, alphabetical sorting would put 9M above 100M.

## Get a directory-level overview first

If you’re not sure what threshold to use, `du` gives you a directory-level breakdown:

``` bash
du -sh */ | sort -rh | head -20
```

This shows the top 20 directories by size, which narrows down where to look before running `find`. For a full tree view including hidden directories:

``` bash
du -sh ./* ./.* 2>/dev/null | sort -rh | head -20
```

Alternatively, modern tools like `ncdu` provide interactive directory size exploration:

``` bash
ncdu -q /path/to/directory
```

## Size units

`find` supports these size suffixes:

- `c` — bytes
- `k` — kilobytes (1024 bytes)
- `M` — megabytes
- `G` — gigabytes
- `T` — terabytes

To find files between 100MB and 1GB:

``` bash
find . -type f -size +100M -size -1G
```

To find files exactly 500MB:

``` bash
find . -type f -size 500M
```

## Exclude certain directories

To skip directories like `.git` or `node_modules`:

``` bash
find . -type f -size +100M -not -path './.git/*' -not -path './node_modules/*'
```

You can also use `-prune` for more efficient exclusion, which prevents `find` from descending into those directories entirely:

``` bash
find . -path './.git' -prune -o -path './node_modules' -prune -o -type f -size +100M -print
```

For multiple exclusions, this approach scales better on large directory trees.

## Search a specific directory tree

To limit your search to a particular location:

``` bash
find /var/log -type f -size +1G -ls
```

## Find files modified within a timeframe

Combine size with recency to find recently created large files:

``` bash
find . -type f -size +500M -mtime -7
```

This finds files larger than 500MB modified in the last 7 days. Use `-mmin -60` for the last 60 minutes.

## Bulk operations with xargs

If you want to do something with the results — like delete, move, or compress them — pipe into `xargs`:

``` bash
find . -type f -size +500M -print0 | xargs -0 ls -lh
```

Using `-print0` and `-0` handles filenames with spaces or special characters safely. To delete large files interactively:

``` bash
find . -type f -size +500M -print0 | xargs -0 -p rm
```

The `-p` flag prompts before deletion. For non-interactive deletion, be careful with the options:

``` bash
find . -type f -size +500M -delete
```

The built-in `-delete` action is faster than piping to `xargs rm`, but use it only when you’re certain about the results.

## Practical example: clean up old logs

Find and remove log files larger than 100MB not modified in 30 days:

``` bash
find /var/log -type f -name '*.log' -size +100M -mtime +30 -delete
```

Always test the command with `-ls` first to verify what will be deleted:

``` bash
find /var/log -type f -name '*.log' -size +100M -mtime +30 -ls
```
