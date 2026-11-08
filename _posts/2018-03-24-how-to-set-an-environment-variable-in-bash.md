---
title: "Setting Environment Variables in Bash"
date: 2018-03-24 08:18:35 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-set-an-environment-variable-in-bash/
---

Setting environment variables in Bash is one of the most fundamental skills for working with Linux command lines and shell scripts. Bash provides several ways to define and manage variables.

## Setting a Variable for the Current Shell

```wp-block-code
MY_VAR="hello world"
```

**Important:** No spaces around the `=` sign. `MY_VAR = "value"` will produce an error because Bash interprets it as a command `MY_VAR` with arguments.

Access the variable with `$`:

```wp-block-code
echo $MY_VAR
# Output: hello world
```

## Exporting to Child Processes

Variables set without `export` are only visible to the current shell. To make them available to child processes (scripts, applications launched from this shell):

```wp-block-code
export MY_VAR="hello world"
# Or export an existing variable
MY_VAR="hello world"
export MY_VAR
```

Without `export`, a script called from this shell won’t see the variable:

```wp-block-code
TEST="only here"
bash -c 'echo $TEST'    # Empty - child process doesn't see it

export TEST="everywhere"
bash -c 'echo $TEST'    # "everywhere" - child sees it
```

## Common Patterns

**Add to PATH:**

```wp-block-code
export PATH="/usr/local/bin:$PATH"
export PATH="$PATH:$HOME/.local/bin"  # Append instead of prepend
```

**Set a development variable:**

```wp-block-code
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export GOPATH=$HOME/go
export EDITOR=vim
```

## Making Variables Persistent

Variables set in a terminal only last for that session. To persist them:

**Per-user (most common):** Add to `~/.bashrc`:

```wp-block-code
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**Login shells only:** Use `~/.bash_profile` or `~/.profile` instead. These run once at login, while `~/.bashrc` runs for each new interactive shell.

**System-wide:** Add to `/etc/profile.d/`:

```wp-block-code
echo 'export JAVA_HOME=/usr/lib/jvm/java-17' | sudo tee /etc/profile.d/java.sh
source /etc/profile.d/java.sh
```

## Setting Variables for a Single Command

```wp-block-code
# Variable only for this one command
DEBUG=1 ./my-script.sh

# Multiple variables
NODE_ENV=production PORT=3000 node server.js
```

This is the preferred pattern for passing configuration to scripts and daemons — the variable doesn’t pollute your shell environment.

## Special Variable Syntax

Bash provides several variable expansion features:

```wp-block-code
# Default value if unset
echo ${MY_VAR:-"default"}

# Set default and assign
echo ${MY_VAR:="default"}

# Error if unset
echo ${MY_VAR:?"MY_VAR is not set"}

# Alternative value if SET
echo ${MY_VAR:+"was set to $MY_VAR"}

# String length
echo ${#MY_VAR}

# Substring
echo ${MY_VAR:0:5}      # First 5 characters
echo ${MY_VAR: -3}      # Last 3 characters

# Replace
echo ${MY_VAR/hello/goodbye}   # Replace first match
echo ${MY_VAR//o/0}            # Replace all matches
```

## Unsetting Variables

```wp-block-code
unset MY_VAR
```

This removes the variable entirely from the current shell and its export list.

## Listing Environment Variables

```wp-block-code
# All exported variables
env
printenv

# All variables (including non-exported)
set

# Search for a specific variable
printenv PATH
echo $PATH
```

## Variable Scope and Subshells

Child processes inherit exported variables, but changes in a child don’t affect the parent:

```wp-block-code
export MY_VAR="parent"
bash -c 'MY_VAR="child"; echo "Child: $MY_VAR"'
echo "Parent: $MY_VAR"
# Output:
# Child: child
# Parent: parent
```

This is a common gotcha when trying to set variables from inside a pipeline or subshell — the parent shell won’t see the change.

## Quick Reference

- `VAR=value` — Set for current shell
- `export VAR=value` — Set and export to children
- `VAR=value command` — Set for single command only
- `~/.bashrc` — Persist per-user
- `/etc/profile.d/` — Persist system-wide
- `unset VAR` — Remove variable

## Integer and Array Variables

Bash supports typed variables:

```wp-block-code
# Integer variable (faster arithmetic)
declare -i COUNT=0
((COUNT++))
echo $COUNT  # 1

# Read-only variable
declare -r CONFIG_PATH="/etc/myapp"
CONFIG_PATH="/new/path"  # Error: readonly variable

# Array
FILES=("file1.txt" "file2.txt" "file3.txt")
echo ${FILES[0]}     # file1.txt
echo ${FILES[@]}     # All elements
echo ${#FILES[@]}    # Array length

# Associative array (Bash 4+)
declare -A CONFIG
CONFIG[host]="example.com"
CONFIG[port]="443"
echo ${CONFIG[host]}  # example.com
```

## Environment Variables in Scripts

When writing shell scripts, follow these best practices:

```wp-block-code
#!/bin/bash
# Check if a variable is set
if [ -z "$JAVA_HOME" ]; then
    echo "Error: JAVA_HOME is not set" >&2
    exit 1
fi

# Use with default
DB_HOST=${DB_HOST:-"localhost"}
DB_PORT=${DB_PORT:-"5432"}

# Quote variables to handle spaces and empty values
echo "Connecting to $DB_HOST:$DB_PORT"
```

Always quote variable expansions (`"$VAR"` not `$VAR`) to prevent word splitting and glob expansion issues with values containing spaces or special characters.
