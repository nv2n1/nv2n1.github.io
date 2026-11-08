---
title: "Extracting Substrings by Delimiter in Bash"
date: 2018-03-24 08:20:44 +0000
layout: post
canonical: https://www.systutorials.com/cut-using-a-string-as-the-delimiter/
---

The `cut` command is designed for simple field splitting, but it has a hard limitation: the delimiter must be a single character.

``` bash
cut --delimiter="delim" -f 1,3
# Error: cut: the delimiter must be a single character
```

This is a deliberate design choice. `cut` prioritizes speed and simplicity for common use cases like splitting on tabs, spaces, or colons. If you need multi-character delimiters, you need a different tool.

## Solution: Use awk for Multi-Character Delimiters

The most practical solution is `awk`, which treats the `-F` option as a full delimiter pattern rather than a single character.

``` bash
awk -F 'delim' '{print $1, $3}' input.txt
```

This splits each line on the string `delim` and prints fields 1 and 3.

### More Realistic Example

If you’re parsing a file with `::|::` as a delimiter:

``` bash
awk -F '::\|::' '{print $1; print $3}' data.txt
```

Note the escaped pipe character — awk’s `-F` interprets the argument as an extended regular expression, so special regex characters need escaping.

### Using FPAT for Complex Patterns

For more sophisticated field matching, use the `FPAT` variable to define what fields *are* rather than what separates them. This is cleaner when dealing with quoted fields or nested delimiters:

``` bash
awk 'BEGIN {FPAT = "[a-zA-Z0-9_]+"} {print $1, $3}' input.txt
```

This extracts contiguous alphanumeric sequences as fields, ignoring any delimiter structure entirely.

FPAT is especially useful for CSV-like data with quoted fields:

``` bash
awk 'BEGIN {FPAT = "([^,]+)|(\"[^\"]+\")"} {print $1, $3}' data.csv
```

## sed as an Alternative

For simpler cases, `sed` can work too:

``` bash
sed 's/delim/\n/g' input.txt | head -n 3 | tail -n 1
```

This converts the delimiter to newlines and extracts specific lines, but it’s less elegant for multiple fields.

## perl for Maximum Flexibility

If you’re already using perl in your scripts, it handles multi-character delimiters natively:

``` bash
perl -lane 'print $F[0], " ", $F[2]' -F 'delim' input.txt
```

The `-a` flag autosplits on the delimiter specified with `-F`, and `@F` contains the resulting fields.

## Practical Comparison

| Tool   | Multi-char Delimiter | Speed | Complexity  |
|--------|----------------------|-------|-------------|
| `cut`  | No                   | Fast  | Low         |
| `awk`  | Yes (regex)          | Good  | Low-Medium  |
| `sed`  | Yes (via regex)      | Good  | Medium      |
| `perl` | Yes                  | Good  | Medium-High |

For most cases, `awk` is the right choice: it’s universally available, handles complex delimiters, and the syntax is straightforward for field extraction.

## Practical Tips and Common Gotchas

When working with programming languages on Linux, environment management is crucial. Use version managers like asdf, pyenv, or sdkman to handle multiple language versions without system-wide conflicts. Always pin dependency versions in production to prevent unexpected breakage from upstream changes.

For build automation, modern alternatives often outperform traditional tools. Consider using just or task instead of Make for simpler task definitions. Use containerized build environments to ensure reproducibility across different development machines.

## Debugging Strategies

Start with the simplest debugging approach and escalate as needed. Print statements and logging often reveal the issue faster than attaching a debugger. For complex issues, use language-specific debuggers like gdb for C and C++, jdb for Java, or dlv for Go. Always check error messages carefully before diving into code.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
