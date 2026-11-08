---
title: "Extract Directory and Filename from File Paths in Bash"
date: 2018-03-24 11:46:09 +0000
layout: post
canonical: https://www.systutorials.com/how-to-get-the-directory-path-and-file-name-from-a-absolute-path-in-bash-on-linux/
---

When you have an absolute path like `/foo/bar/baz.txt` and need to split it into its components, Bash provides two essential utilities: `dirname` and `basename`.

## Using dirname and basename

The `dirname` command returns the directory portion of a path, while `basename` returns just the filename:

``` bash
p="/foo/bar/baz.txt"
dirname "$p"    # Output: /foo/bar
basename "$p"   # Output: baz.txt
```

Note the quotes around `$p` — this is important if your paths contain spaces or special characters.

## Practical examples

Extract just the filename without extension:

``` bash
p="/home/user/documents/report.pdf"
basename "$p" .pdf    # Output: report
```

Build a new path using the directory:

``` bash
p="/etc/config/app.conf"
dir=$(dirname "$p")
cp "$p" "$dir/app.conf.backup"
```

Process multiple files in a directory:

``` bash
for file in /var/log/app/*.log; do
    dir=$(dirname "$file")
    name=$(basename "$file")
    echo "Processing $name from $dir"
done
```

## Parameter expansion alternative

Bash parameter expansion offers an alternative to external commands, which is faster in loops:

``` bash
p="/foo/bar/baz.txt"
dir="${p%/*}"           # Remove everything after last /
file="${p##*/}"         # Remove everything up to last /
echo "$dir"             # /foo/bar
echo "$file"            # baz.txt
```

Remove the extension:

``` bash
p="/foo/bar/baz.txt"
noext="${p%.*}"         # Remove from last . to end
echo "$noext"           # /foo/bar/baz
```

## When to use each approach

Use `dirname` and `basename` when:

- Your script prioritizes readability
- Performance isn’t critical
- You’re working with simple, well-formed paths

Use parameter expansion when:

- Processing thousands of paths in loops
- You want to avoid spawning subshells
- The path manipulation is straightforward

Parameter expansion is typically 10-20x faster since it avoids calling external commands, but the difference only matters at scale.

## Edge cases

Both approaches handle relative paths and symlinks consistently:

``` bash
dirname "baz.txt"       # Output: .
basename "./foo/bar"    # Output: bar
```

Be careful with trailing slashes:

``` bash
dirname "/foo/bar/"     # Output: /foo/bar (removes trailing slash)
basename "/foo/bar/"    # Output: bar (removes trailing slash)
```

For paths that might contain spaces or special characters, always quote your variables:

``` bash
p="/home/user/my documents/file (1).txt"
dirname "$p"    # Correctly handles spaces and parentheses
basename "$p"   # Correctly outputs: file (1).txt
```

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Practical Tips and Common Gotchas

When working with programming languages on Linux, environment management is crucial. Use version managers like asdf, pyenv, or sdkman to handle multiple language versions without system-wide conflicts. Always pin dependency versions in production to prevent unexpected breakage from upstream changes.

For build automation, modern alternatives often outperform traditional tools. Consider using just or task instead of Make for simpler task definitions. Use containerized build environments to ensure reproducibility across different development machines.

## Debugging Strategies

Start with the simplest debugging approach and escalate as needed. Print statements and logging often reveal the issue faster than attaching a debugger. For complex issues, use language-specific debuggers like gdb for C and C++, jdb for Java, or dlv for Go. Always check error messages carefully before diving into code.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
