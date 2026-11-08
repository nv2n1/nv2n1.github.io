---
title: "Print Text Files with Line Numbers: nl, cat, and More"
date: 2018-03-24 08:21:12 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-print-out-text-with-line-numbers-in-linux/
---

The `nl` command is purpose-built for adding line numbers to text files:

``` bash
nl text-file
```

By default, `nl` numbers all non-empty lines and skips blank lines. This behavior is controlled by the body section style, which defaults to `t` (text only).

## Common nl options

**Number all lines including blanks:**

``` bash
nl -ba text-file
```

**Start numbering at a specific value:**

``` bash
nl -v 100 text-file
```

**Control number formatting:**

``` bash
# Right-aligned with leading zeros (width 6)
nl -nrz text-file

# Left-aligned
nl -nln text-file

# Left-aligned, no leading zeros
nl -nln text-file
```

**Change the separator between number and content:**

``` bash
# Use colon and space instead of default tab
nl -s ': ' text-file

# Use pipe separator
nl -s ' | ' text-file
```

**Set line number field width:**

``` bash
# Narrow field (4 characters)
nl -w 4 text-file

# Wide field (8 characters)
nl -w 8 text-file
```

**Number only lines matching a pattern:**

``` bash
# Only number lines starting with uppercase letter
nl -bp'^[A-Z]' text-file

# Number lines containing "error"
nl -bp'error' text-file
```

## Quick alternatives

**cat -n for simple numbering:**

``` bash
cat -n text-file
```

This numbers all lines without blank-line distinction. It’s simpler but less flexible than `nl`. Good for quick one-offs.

**grep -n to number while filtering:**

``` bash
grep -n "pattern" text-file
```

Restricts output to matching lines only. Useful when you need both filtering and line numbers in a single pass.

**less -N for interactive viewing:**

``` bash
less -N /path/to/largefile
```

Displays line numbers within the pager. Press `&` in less to toggle line numbers on/off without exiting. Essential for navigating large log files.

**awk for custom formatting:**

``` bash
awk '{print NR": "$0}' text-file

# With custom separators
awk '{printf "%5d | %s\n", NR, $0}' text-file

# Number only non-empty lines
awk 'NF {printf "%d: %s\n", NR, $0}' text-file
```

The `awk` approach gives you full control over output formatting and filtering logic.

**sed for in-place numbering:**

``` bash
sed = text-file | paste -d ' ' - -
```

This uses `sed` to insert line numbers, then `paste` to align them. Less common but useful for scripting.

## Practical examples

**Number a log file and save output:**

``` bash
nl /var/log/syslog > syslog-numbered.txt
```

**View a configuration file with line numbers, skipping blanks:**

``` bash
nl -s ': ' /etc/nginx/nginx.conf | less
```

**Find error lines with context and line numbers:**

``` bash
nl -ba /var/log/app.log | grep -i error
```

**Number a Python script with narrow field width:**

``` bash
nl -w 3 -s ' | ' script.py
```

**Number specific line ranges:**

``` bash
# Lines 10-50 with numbers
sed -n '10,50p' file.txt | nl -v 10
```

**Combine with head/tail for partial numbering:**

``` bash
# Number only the first 20 lines
head -20 file.txt | nl

# Number the last 30 lines
tail -30 file.txt | nl -v $(wc -l < file.txt | awk '{print $1-29}')
```

**Compare files side-by-side with line numbers:**

``` bash
diff <(nl file1.txt) <(nl file2.txt)
```

## Choosing the right tool

- Use `nl` when you need control over blank lines, formatting, and numbering patterns
- Use `cat -n` for quick numbering of entire files
- Use `grep -n` when you’re already filtering output
- Use `less -N` when viewing files interactively
- Use `awk` when you need complex custom formatting or conditional numbering
