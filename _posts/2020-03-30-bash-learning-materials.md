---
title: "Bash: From Basics to Production-Ready Scripts"
date: 2020-03-30 06:13:57 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /bash-learning-materials/
---

Start with the official Bash manual—it’s comprehensive and essential before writing production scripts. Access it locally with:

``` bash
man bash
```

Or online at the <a href="https://www.gnu.org/software/bash/manual/" rel="nofollow noopener" target="_blank">GNU Bash Manual</a>. The density rewards careful reading; spend time on these sections:

- **INVOCATION**: How the shell starts and behaves
- **Quoting**: When to quote and when not to
- **Parameter Expansion**: Variable manipulation, defaults, substring removal
- **Command Substitution**: Always use `$(...)` instead of backticks
- **Arithmetic Expansion**: `$((...))` for math operations
- **Conditional Constructs**: `if`, `case`, and `[[ ]]` vs `[ ]`

Most bugs hide in quoting, parameter expansion, and command substitution. Understanding these sections cuts debugging time significantly.

## Defensive Scripting Template

Every production script should start with this foundation:

``` bash
#!/bin/bash
set -euo pipefail

trap 'echo "Error on line $LINENO"; exit 1' ERR

# Your script code here
```

Breaking this down:

- `-e`: Exit immediately on any error
- `-u`: Fail if you reference undefined variables
- `-o pipefail`: Propagate errors through pipes (if command1 \| command2 fails, the script exits)
- `trap 'echo "Error on line $LINENO"'`: Catch errors for debugging or cleanup

This catches most common failures before they become production incidents.

## Style: Google Shell Style Guide

The <a href="https://google.github.io/styleguide/shellguide.html" rel="nofollow noopener" target="_blank">Google Shell Style Guide</a> applies specifically to Bash and reduces bugs through consistency:

- Quote all variables: `"$var"` not `$var`
- Use `[[ ... ]]` for conditionals, not `[ ... ]`
- Declare variables `local` in functions
- Apply `set -euo pipefail` at script start
- Comment non-obvious logic

Adapt these to your team’s needs rather than following dogmatically—the core rules (quoting, `set -euo pipefail`, using `local`) matter everywhere.

## ShellCheck: Your Static Analyzer

Before advancing further, integrate <a href="https://www.shellcheck.net/" rel="nofollow noopener" target="_blank">ShellCheck</a> into your workflow. It catches mistakes that take hours to debug:

``` bash
shellcheck myscript.sh
```

Most distributions package it. Install it in your editor for real-time feedback:

- **Vim/Neovim**: Use `ale` or `nvim-lint` with ShellCheck
- **VS Code**: Install the <a href="https://marketplace.visualstudio.com/items?itemName=timonwong.shellcheck" rel="nofollow noopener" target="_blank">ShellCheck extension</a>
- **Emacs**: Use `flycheck` with the ShellCheck checker

ShellCheck catches unquoted variables, unused variables, incorrect quoting in conditionals, and logic errors. The online version includes explanations for each warning code.

## Debugging Techniques

When scripts fail, use these tools:

``` bash
# Run entire script with debug output
bash -x script.sh

# Enable debugging within the script
set -x

# Improve debug output formatting
export PS4='+ ${BASH_SOURCE}:${LINENO} ${FUNCNAME[0]}(): '

# Trace without execution (useful for parsing errors)
bash -n script.sh

# Redirect verbose output to a file for review
bash -x script.sh 2> debug.log
```

For a single function, wrap it in a subshell with debugging enabled:

``` bash
debug_function() {
  (set -x; some_command "$@")
}
```

Check exit codes individually with `$?` or structure conditionals carefully:

``` bash
if command; then
  echo "Success"
else
  echo "Failed with exit code $?"
fi
```

## Common Pitfalls You’ll Encounter

**Word splitting**: Unquoted variables split on whitespace and glob. Always quote:

``` bash
# Wrong
for file in $list; do ...

# Right
for file in $list; do ... 
# Better: use an array
for file in "${list[@]}"; do ...
```

**Globbing in conditionals**: `[ ]` expands globs; `[[ ]]` doesn’t:

``` bash
# Dangerous—expands *.txt
if [ "$file" = *.txt ]; then ...

# Safe
if [[ "$file" == *.txt ]]; then ...
```

**Subshell scope**: Variables assigned in `(...)` don’t affect the parent:

``` bash
# Wrong—var is unset after the subshell
(var="value")
echo "$var"  # empty

# Right—use { ... ; } for grouping without a subshell
{ var="value"; }
echo "$var"  # prints "value"
```

**Pipe subshells**: The rightmost command in a pipe runs in a subshell:

``` bash
# Wrong—count is lost
cat file | grep pattern | wc -l
count=$?  # $? is 0 (wc succeeded), not the line count

# Right—use command substitution
count=$(grep pattern file | wc -l)
```

**Undefined variables**: `set -u` fails fast, so catch typos early:

``` bash
# With set -u, this exits immediately
echo "$undefind_variable"  # typo caught
```

## Process Substitution for Efficient I/O

Use process substitution to avoid temporary files and subshell scope issues:

``` bash
# Compare sorted files
diff <(sort file1.txt) <(sort file2.txt)

# Read from multiple sources
paste <(cut -f1 data1.txt) <(cut -f1 data2.txt)

# Write to multiple outputs simultaneously
tee >(gzip > file.gz) >(bzip2 > file.bz2) < input.txt > file.txt
```

Process substitution creates named pipes internally, avoiding the overhead of temporary files.

## Arrays and Complex Data

Handle collections properly:

``` bash
# Indexed arrays
declare -a items=("file1.txt" "file2.txt" "file3.txt")
for item in "${items[@]}"; do
  echo "$item"
done

# Associative arrays (Bash 4+)
declare -A config=([host]="localhost" [port]="5432")
for key in "${!config[@]}"; do
  echo "$key=${config[$key]}"
done

# Append to arrays
items+=("file4.txt")
```

Always use `"${array[@]}"` to expand all elements properly quoted.

## Regular Expressions with \[\[ \]\]

The `=~` operator in `[[ ]]` supports extended regular expressions:

``` bash
if [[ "$filename" =~ \.(sh|bash)$ ]]; then
  echo "Bash script"
fi

# Capture groups
if [[ "$input" =~ ^([a-z]+)_([0-9]+)$ ]]; then
  echo "Prefix: ${BASH_REMATCH[1]}"
  echo "Number: ${BASH_REMATCH[2]}"
fi
```

The matched groups are available in the `BASH_REMATCH` array.

## When to Stop Using Bash

Bash excels at gluing Unix tools together and system automation, but has limits:

**Use Bash for:**

- Orchestrating existing commands and pipelines
- System startup, deployment, or maintenance scripts
- Quick automation under 100 lines
- One-off admin tasks

**Switch to Python 3, Go, or Rust when:**

- Script exceeds a few hundred lines
- You need complex data structures or algorithms
- Testing is required
- Your team standardizes on a compiled or typed language
- Performance matters

A 500-line Bash script is harder to maintain and debug than a 500-line Python script.

## Practical Next Steps

1.  Read the Bash manual sections on quoting and expansions (1–2 hours)
2.  Set up ShellCheck in your editor and fix all warnings on existing scripts
3.  Write new scripts with `set -euo pipefail` and proper quoting
4.  Build a small function library for logging, error handling, and argument parsing
5.  Test scripts locally before deploying
6.  Study the <a href="https://www.tldp.org/LDP/abs/html/" rel="nofollow noopener" target="_blank">Advanced Bash-Scripting Guide</a> selectively once fundamentals are solid—focus on sections relevant to your work

The time invested in learning Bash properly pays off in more reliable automation and faster debugging when things break.
