---
title: "Piping stderr to less: Redirect and view error streams"
date: 2018-03-24 08:18:30 +0000
modified: 2026-04-12 16:11:07 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-pipe-the-stderr-to-less/
---

When you need to page through error output from a command, you’ll run into the issue that `less` only receives stdout by default. Error messages go to stderr (file descriptor 2), so they’ll still scroll past on your terminal while stdout gets paged.

### Basic approach: combine stderr with stdout

``` bash
make 2>&1 | less
```

The `2>&1` redirects stderr (fd 2) to stdout (fd 1), merging both streams. This is the most common use case — you want to see everything in one pageable view.

### View only stderr

If you need to examine only the error output:

``` bash
make 2>&1 >/dev/null | less
```

This redirects stdout to `/dev/null` while sending stderr (now combined with stdout via `2>&1`) to `less`.

### Modern alternative: use bash process substitution

For cleaner separation, you can use process substitution to handle streams independently:

``` bash
make 2> >(less)
```

Here stderr goes directly to `less` in a subshell. Stdout still goes to the terminal. This is useful when you want to page errors without losing other output:

``` bash
make 2> >(less) | head -20
```

### Preserve the exit status

Piping masks the original command’s exit status. If you need both pagination and the correct exit code:

``` bash
make 2>&1 | tee >(less) > /dev/null
```

The `tee` command writes to both `less` (via process substitution) and `/dev/null`, while the original exit status is preserved.

Or use the `pipefail` option with bash:

``` bash
set -o pipefail
make 2>&1 | less
echo $?  # now reflects make's exit status, not less's
```

### Real-world examples

Reviewing compiler warnings across a large build:

``` bash
gcc -Wall *.c 2>&1 | less
```

Checking systemd journal errors:

``` bash
journalctl -p err -n 500 2>&1 | less
```

Debugging a shell script’s stderr output:

``` bash
bash -x script.sh 2>&1 | less
```

### Tips for less

When viewing error output in `less`, use `/pattern` to search forward and `?pattern` to search backward. Press `G` to jump to the end, `g` for the beginning. Hit `q` to quit.

For color-coded output (like from `gcc` with colors enabled), use `less -R` to preserve ANSI escape sequences:

``` bash
make 2>&1 | less -R
```

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
