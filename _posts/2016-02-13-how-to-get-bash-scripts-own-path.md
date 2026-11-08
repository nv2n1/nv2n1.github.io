---
title: "Finding Your Bash Script\u2019s Location: $0 vs ${BASH_SOURCE[0]}"
date: 2016-02-13 17:49:58 +0000
layout: post
canonical: https://www.systutorials.com/how-to-get-bash-scripts-own-path/
---

When a Bash script needs to reference its own location — for sourcing additional files, logging, or managing relative paths — `$0` seems like the obvious choice. But it’s a trap: `$0` behaves differently depending on whether your script is executed directly or sourced.

## The Problem with \$0

When you execute a script directly:

``` bash
./script.sh
```

`$0` contains the script’s path. But when you source it:

``` bash
source script.sh
# or
. script.sh
```

`$0` no longer contains the sourced script’s path — it contains the path of the *calling* shell or parent script instead. This breaks any logic that relies on knowing the script’s actual location.

## The Solution: \${BASH_SOURCE\[0\]}

Use `${BASH_SOURCE[0]}` instead. It reliably returns the path of the current script regardless of whether it’s sourced or executed directly.

``` bash
#!/bin/bash

SCRIPT_PATH="${BASH_SOURCE[0]}"
SCRIPT_DIR="$(cd "$(dirname "${SCRIPT_PATH}")" && pwd)"

echo "Script is at: ${SCRIPT_PATH}"
echo "Script directory: ${SCRIPT_DIR}"
```

## Why \${BASH_SOURCE\[0\]} Works

`BASH_SOURCE` is an array variable where each element contains the filename of a sourced script or the main script. The index tracks the call stack:

- `${BASH_SOURCE[0]}` = current script file
- `${BASH_SOURCE[1]}` = script that sourced the current one
- `${BASH_SOURCE[2]}` = script that sourced that one, and so on

This works inside functions too. When a function is defined in a sourced script, `${BASH_SOURCE[0]}` still points to the file where the function was defined, not where it was called from.

## Practical Example

Consider two scripts where `b.sh` is sourced by `a.sh`:

**a.sh:**

``` bash
#!/bin/bash
echo "a.sh path: ${BASH_SOURCE[0]}"
source ./b.sh
```

**b.sh:**

``` bash
#!/bin/bash
echo "b.sh path: ${BASH_SOURCE[0]}"

get_config() {
    local config_dir="$(dirname "${BASH_SOURCE[0]}")/config"
    echo "Config location: ${config_dir}"
}

get_config
```

Running `./a.sh` produces:

    a.sh path: ./a.sh
    b.sh path: ./b.sh
    Config location: ./config

Sourcing it with `. a.sh` produces the same output. With `$0`, you’d get different results depending on how the script was invoked.

## Getting the Absolute Path

For scripts that might be called from different directories, get the absolute path:

``` bash
SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/$(basename "${BASH_SOURCE[0]}")"
```

Or use readlink if symlink resolution matters:

``` bash
SCRIPT_PATH="$(readlink -f "${BASH_SOURCE[0]}")"
```

## When to Use Each Variable

- **`${BASH_SOURCE[0]}`**: You want the path of the currently executing script file
- **`$0`**: You’re documenting program invocation, or you need the command the user actually typed
- **`${BASH_SOURCE[@]}`**: Debugging — prints the entire call stack of sourced files

The bottom line: for any script logic that depends on the script’s own location, reach for `${BASH_SOURCE[0]}` and avoid the pitfalls of `$0`.

## Practical Tips and Common Gotchas

When working with programming languages on Linux, environment management is crucial. Use version managers like asdf, pyenv, or sdkman to handle multiple language versions without system-wide conflicts. Always pin dependency versions in production to prevent unexpected breakage from upstream changes.

For build automation, modern alternatives often outperform traditional tools. Consider using just or task instead of Make for simpler task definitions. Use containerized build environments to ensure reproducibility across different development machines.

## Debugging Strategies

Start with the simplest debugging approach and escalate as needed. Print statements and logging often reveal the issue faster than attaching a debugger. For complex issues, use language-specific debuggers like gdb for C and C++, jdb for Java, or dlv for Go. Always check error messages carefully before diving into code.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
