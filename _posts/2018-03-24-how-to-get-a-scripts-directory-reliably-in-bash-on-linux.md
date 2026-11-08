---
title: "Finding a Bash Script\u2019s Directory Reliably"
date: 2018-03-24 11:49:30 +0000
layout: post
canonical: https://www.systutorials.com/how-to-get-a-scripts-directory-reliably-in-bash-on-linux/
---

Getting the directory path of a running script is a common requirement in bash, whether you’re sourcing files, building paths to config directories, or navigating relative to the script itself. The naive approach often fails with symbolic links or when the script is sourced rather than executed directly.

## The Problem

Using `$0` alone is unreliable. If your script is a symlink, `dirname $0` returns the symlink’s directory, not the actual script location. If the script is sourced, `$0` refers to the shell itself. These edge cases break path resolution in production scripts.

## The Solution

Use `readlink -f` to resolve the absolute path, then pass it to `dirname`:

``` bash
script_dir=$(dirname "$(readlink -f "$0")")
```

Breaking this down:

- `readlink -f "$0"` — resolves all symlinks and returns the absolute path to the actual script file
- `dirname ...` — extracts the directory portion of that path
- `script_dir=...` — stores the result in a variable

## Handling Sourced Scripts

When a script is sourced (rather than executed), `$0` points to the parent shell, not the sourced file. Use `${BASH_SOURCE[0]}` instead:

``` bash
script_dir=$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")
```

`${BASH_SOURCE[0]}` always references the currently executing file in the stack, so it works correctly whether the script is executed or sourced.

## Practical Example

Here’s a complete script that sets up directories reliably:

``` bash
#!/bin/bash

script_dir=$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")
config_dir="$script_dir/config"
data_dir="$script_dir/data"

echo "Script location: $script_dir"
echo "Config directory: $config_dir"
echo "Data directory: $data_dir"

if [[ ! -d "$config_dir" ]]; then
    mkdir -p "$config_dir"
fi
```

## Edge Cases to Consider

**Symlinked script:** If `/usr/bin/myscript` is a symlink to `/opt/app/myscript.sh`, `readlink -f` returns `/opt/app/myscript.sh` and `script_dir` becomes `/opt/app/`. This is the correct behavior for finding supporting files.

**Script in PATH:** If you run a script from `PATH` (e.g., just typing `myscript`), the absolute path resolution still works correctly.

**Relative symlinks:** Even complex chains of relative symlinks are resolved completely by `readlink -f`, unlike older `-e` flag implementations.

**No readlink available:** On some minimal systems, `readlink -f` may not be available. As a fallback:

``` bash
script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
```

This uses `cd` and `pwd` to normalize the path, though it doesn’t resolve symlinks. For most scripts, this is acceptable.

## Best Practice

Use this as your standard:

``` bash
script_dir=$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")
```

It handles symlinks, sourcing, relative paths, and works across different invocation methods. Store it near the top of your script before any file operations that depend on the script’s location.

## Practical Tips and Common Gotchas

When working with programming languages on Linux, environment management is crucial. Use version managers like asdf, pyenv, or sdkman to handle multiple language versions without system-wide conflicts. Always pin dependency versions in production to prevent unexpected breakage from upstream changes.

For build automation, modern alternatives often outperform traditional tools. Consider using just or task instead of Make for simpler task definitions. Use containerized build environments to ensure reproducibility across different development machines.

## Debugging Strategies

Start with the simplest debugging approach and escalate as needed. Print statements and logging often reveal the issue faster than attaching a debugger. For complex issues, use language-specific debuggers like gdb for C and C++, jdb for Java, or dlv for Go. Always check error messages carefully before diving into code.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
