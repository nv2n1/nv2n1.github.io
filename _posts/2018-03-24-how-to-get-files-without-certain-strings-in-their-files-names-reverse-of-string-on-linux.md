---
title: "Find Files Without a Specific String in Their Name on Linux"
date: 2018-03-24 11:45:26 +0000
modified: 2026-04-12 16:05:11 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-get-files-without-certain-strings-in-their-files-names-reverse-of-string-on-linux/
---

Finding files that match a pattern is straightforward with `ls *string*` or `find . -name '*string*'`. But excluding files with a certain string in their filename requires a different approach.

## Using find with negation

The most reliable method is `find` with the `!` (or `-not`) operator:

``` bash
find . -type f ! -name '*string*'
```

This finds all regular files in the current directory and subdirectories that do NOT match the pattern. The `-type f` flag ensures you only get files, not directories. Without it, you’ll get both.

If you only want to search the current directory (not subdirectories):

``` bash
find . -maxdepth 1 -type f ! -name '*string*'
```

To search a specific directory:

``` bash
find /path/to/dir -type f ! -name '*string*'
```

## Using ls with grep

For a quick listing in the current directory only:

``` bash
ls -1 | grep -v string
```

The `-1` flag ensures one file per line. The `-v` flag inverts the match, showing only lines that don’t contain the pattern.

**Caveat:** This approach breaks with special characters in filenames (spaces, newlines, globbing characters). Use `find` when you need reliable handling of arbitrary filenames.

## Combining with other operations

To delete all files except those matching a pattern:

``` bash
find . -type f ! -name '*string*' -delete
```

To count matching files:

``` bash
find . -type f ! -name '*string*' | wc -l
```

To perform an action on each matching file (e.g., move to another directory):

``` bash
find . -type f ! -name '*string*' -exec mv {} /destination/ \;
```

Or with `xargs` for better performance on large file counts:

``` bash
find . -type f ! -name '*string*' -print0 | xargs -0 rm
```

The `-print0` and `-0` flags handle filenames with spaces and special characters safely.

## Multiple exclusions

To exclude multiple patterns, chain negation operators:

``` bash
find . -type f ! -name '*string1*' ! -name '*string2*' ! -name '*.tmp'
```

Or use extended regex with `find -regex`:

``` bash
find . -type f ! -regex '.*\(string1\|string2\|\.tmp\).*'
```

## Gotchas to avoid

- **Missing `-type f`:** Without it, directories matching your negation are also returned
- **Unquoted wildcards:** Use quotes around patterns to prevent shell expansion: `find . ! -name '*string*'` not `find . ! -name *string*`
- **ls limitations:** `ls` can truncate long filenames and doesn’t reliably handle special characters — prefer `find` for scripting

## Troubleshooting Common Issues

When encountering problems on Linux systems, follow a systematic approach. Check system logs first using journalctl for systemd-based distributions. Verify service status with systemctl before attempting restarts. For network issues, use ip addr and ss -tulpn to diagnose connectivity problems.

Package management issues often stem from stale caches. Run dnf clean all on Fedora or apt clean on Ubuntu before retrying failed installations. If a package has unmet dependencies, try resolving them with dnf autoremove or apt autoremove.

## Related System Commands

These commands are frequently used alongside the tools discussed in this article:

- systemctl status service-name – Check if a service is running
- journalctl -u service-name -f – Follow service logs in real time
- rpm -qi package-name – Query installed package information
- dnf history – View package transaction history
- top or htop – Monitor system resource usage

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
