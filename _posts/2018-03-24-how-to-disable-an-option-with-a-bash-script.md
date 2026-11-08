---
title: "Disabling Options in Bash Scripts"
date: 2018-03-24 11:50:21 +0000
layout: post
canonical: https://www.systutorials.com/how-to-disable-an-option-with-a-bash-script/
---

Bash maintains a set of built-in options that control script behavior. You disable them using `set +o` followed by the option name, or with short flags like `set +x`.

## The Basic Syntax

``` bash
set +o option-name
```

Or using short flag notation:

``` bash
set +x
```

The `+` sign disables an option; `-` enables it. This works for both long-form (`-o option-name`) and short-form flags.

## Common Options You’ll Disable

**set +e** — Allow commands to fail without exiting the script

By default, `set -e` exits immediately if any command fails. Disabling it lets the script continue even when commands return non-zero status codes. Useful when you expect certain commands might fail:

``` bash
#!/bin/bash
set -e
# ... some commands ...

set +e
# This command might fail, and we don't care
rm /tmp/nonexistent-file.txt
exit_code=$?
set -e

# Rest of script continues with error checking enabled
```

**set +u** — Allow unset variables

`set -u` treats unset variables as errors, preventing typos from silently passing through. Disabling it reverts to lenient behavior where undefined variables expand to empty strings. Generally not recommended for production scripts:

``` bash
#!/bin/bash
set -u

echo "$DEFINED_VAR"  # OK
echo "$UNDEFINED_VAR"  # Error: parameter not set

set +u
echo "$UNDEFINED_VAR"  # Expands to empty string, no error
```

**set +x** — Disable command echo (debugging)

`set -x` prints each command before executing it—invaluable for debugging. Disable it to stop the noise:

``` bash
#!/bin/bash
set -x
echo "This command is printed before execution"

set +x
echo "This command runs silently"

set -x
echo "Debugging is back on"
```

## Checking Current Option Status

List all enabled options:

``` bash
set -o
```

Or check a specific option:

``` bash
if [[ -o option-name ]]; then
    echo "option-name is enabled"
else
    echo "option-name is disabled"
fi
```

## Scoping Options in Functions

Options set in a function remain active after the function returns unless explicitly disabled. For isolated behavior, use subshells:

``` bash
#!/bin/bash
set -e

my_function() {
    (
        set +e
        # Commands here can fail without affecting parent
        false
        echo "Still executing"
    )
    # Back to set -e in parent scope
}

my_function
```

## Production Best Practices

Most production scripts should start with:

``` bash
#!/bin/bash
set -euo pipefail
```

This enables:

- `-e`: Exit on error
- `-u`: Error on unset variables
- `-o pipefail`: Fail if any command in a pipeline fails

Then selectively disable specific options only where necessary. This pattern catches subtle bugs that would otherwise silently propagate.

## Practical Tips and Common Gotchas

When working with programming languages on Linux, environment management is crucial. Use version managers like asdf, pyenv, or sdkman to handle multiple language versions without system-wide conflicts. Always pin dependency versions in production to prevent unexpected breakage from upstream changes.

For build automation, modern alternatives often outperform traditional tools. Consider using just or task instead of Make for simpler task definitions. Use containerized build environments to ensure reproducibility across different development machines.

## Debugging Strategies

Start with the simplest debugging approach and escalate as needed. Print statements and logging often reveal the issue faster than attaching a debugger. For complex issues, use language-specific debuggers like gdb for C and C++, jdb for Java, or dlv for Go. Always check error messages carefully before diving into code.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
