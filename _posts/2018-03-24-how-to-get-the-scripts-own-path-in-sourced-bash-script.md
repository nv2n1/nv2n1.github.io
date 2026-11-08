---
title: "Getting a Sourced Bash Script\u2019s Own Path"
date: 2018-03-24 11:49:58 +0000
layout: post
canonical: https://www.systutorials.com/how-to-get-the-scripts-own-path-in-sourced-bash-script/
---

When you source a script using `. script.sh` or `source script.sh`, the `$0` variable doesn’t point to the sourced script—it stays as the path of the parent shell or calling script. This creates a problem if you need the sourced script to know its own location.

## The solution: use `${BASH_SOURCE[0]}`

The `${BASH_SOURCE[0]}` variable holds the path of the currently executing script, even when sourced. This is the reliable way to reference a script’s own location from within the script itself.

``` bash
#!/bin/bash

# This works whether the script is sourced or executed directly
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "Script location: $script_dir"
```

## Understanding `${BASH_SOURCE[0]}` vs `$0`

- `$0` — the name or path used to invoke the shell (stays constant from the parent shell)
- `${BASH_SOURCE[0]}` — the name of the currently executing script (changes in each script file)

When you source a script:

``` bash
# In parent.sh
. ./helper.sh
```

Inside `helper.sh`:

- `$0` would be `parent.sh` or whatever invoked the parent
- `${BASH_SOURCE[0]}` would be `helper.sh`

## `${BASH_SOURCE[@]}` — the call stack

For more complex scenarios with multiple levels of sourcing, use the array form `${BASH_SOURCE[@]}`:

``` bash
#!/bin/bash

# Print the entire sourcing call stack
for i in "${!BASH_SOURCE[@]}"; do
    echo "Level $i: ${BASH_SOURCE[$i]}"
done
```

This shows the chain of scripts that led to the current execution.

## Practical example: sourced config loader

``` bash
#!/bin/bash
# config.sh - a sourced configuration file

# Get the directory where this config file lives
config_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Load additional files relative to the config location
source "$config_dir/defaults.conf"
source "$config_dir/local.conf" 2>/dev/null || true

export CONFIG_HOME="$config_dir"
```

The `cd` and `pwd` combination handles relative paths correctly, even if the script is sourced from a different working directory.

## Getting just the filename (not the full path)

If you need only the script’s name without the directory:

``` bash
script_name="${BASH_SOURCE[0]##*/}"
echo "Script name: $script_name"
```

Or for the full path:

``` bash
script_path="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/$(basename "${BASH_SOURCE[0]}")"
```

## Compatibility note

`BASH_SOURCE` is a Bash-specific feature and won’t work in POSIX sh. If you need portability to other shells, you’ll need to pass the script path as a parameter or use other workarounds. For most modern systems where Bash is standard, `${BASH_SOURCE[0]}` is the right choice.

## Practical Tips and Common Gotchas

When working with programming languages on Linux, environment management is crucial. Use version managers like asdf, pyenv, or sdkman to handle multiple language versions without system-wide conflicts. Always pin dependency versions in production to prevent unexpected breakage from upstream changes.

For build automation, modern alternatives often outperform traditional tools. Consider using just or task instead of Make for simpler task definitions. Use containerized build environments to ensure reproducibility across different development machines.

## Debugging Strategies

Start with the simplest debugging approach and escalate as needed. Print statements and logging often reveal the issue faster than attaching a debugger. For complex issues, use language-specific debuggers like gdb for C and C++, jdb for Java, or dlv for Go. Always check error messages carefully before diving into code.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
