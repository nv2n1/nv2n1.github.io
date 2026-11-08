---
title: "Printing to STDERR and STDOUT in Bash"
date: 2018-03-24 11:52:57 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-print-a-line-to-stderr-and-stdout-in-bash/
---

Understanding file descriptors is fundamental to shell scripting. By default, your shell has three standard streams:

- **STDOUT (FD 1):** Standard output, where commands print results
- **STDERR (FD 2):** Standard error, where commands print errors and diagnostics
- **STDIN (FD 0):** Standard input, where commands read data

## Basic Output

Print to STDOUT:

``` bash
echo "This goes to stdout"
```

Print to STDERR:

``` bash
echo "This is an error" >&2
```

The `>&2` redirects the output to file descriptor 2 (STDERR). This is the standard approach and works across all POSIX shells.

## Printing Multiple Lines

For multi-line messages to STDERR, use a here-document:

``` bash
cat >&2 <<EOF
Error: Something went wrong
Details:
  - Check the logs
  - Verify permissions
EOF
```

This is cleaner than multiple `echo` statements, especially for larger blocks.

## Capturing and Separating Streams

When running commands, redirect streams explicitly:

``` bash
# Capture only stdout
result=$(command 2>/dev/null)

# Capture only stderr
errors=$(command 2>&1 1>/dev/null)

# Separate both streams
command 2>errors.log 1>output.log

# Send stderr to stdout
command 2>&1 | tee combined.log

# Send both to different places
command > output.log 2> errors.log
```

The order matters with redirects. `2>&1` sends FD 2 to wherever FD 1 currently points. If you do `2>&1 1>/dev/null`, STDERR still goes to the terminal while STDOUT goes nowhere—not what you want.

## Practical Examples

Logging errors in a script:

``` bash
#!/bin/bash

error_exit() {
    echo "ERROR: $1" >&2
    exit 1
}

if [[ ! -f "$config_file" ]]; then
    error_exit "Config file not found: $config_file"
fi
```

Separating diagnostic output from results:

``` bash
#!/bin/bash

debug() {
    [[ "$DEBUG" == "1" ]] && echo "[DEBUG] $*" >&2
}

debug "Starting process"
result=$(some_command)
debug "Process completed"
echo "$result"
```

Run with debugging:

``` bash
DEBUG=1 ./script.sh 2>debug.log
```

Combining streams in a pipeline while keeping them separate:

``` bash
# Process stdout, while errors remain visible
command 2> >(tee errors.log >&2) | process_output
```

## File Descriptor Duplication

Save and restore file descriptors:

``` bash
exec 3>&1  # Save stdout to FD 3
exec 1>output.log  # Redirect stdout to file
echo "This goes to the file"
exec 1>&3  # Restore stdout from FD 3
echo "This goes to the terminal"
```

Useful for complex scripts where you need temporary redirects.

## Conditional Redirection

Print to STDERR only if running interactively:

``` bash
if [[ -t 2 ]]; then
    # stderr is a terminal
    echo "Error: check your input" >&2
fi
```

The `-t` test checks if a file descriptor is connected to a terminal.

## Testing Your Script

Use a shell linter before deployment:

``` bash
shellcheck myscript.sh
```

Test stream separation:

``` bash
./myscript.sh 2>stderr.txt 1>stdout.txt
diff -u expected_stderr.txt stderr.txt
diff -u expected_stdout.txt stdout.txt
```

## Common Mistakes

**Redirecting in the wrong order:**

``` bash
# Wrong: loses stderr when you redirect stdout
command 1>output.log 2>&1

# Right: capture both properly
command 2>&1 | tee output.log
# Or explicitly
command >output.log 2>error.log
```

**Forgetting that `echo` adds a newline:**

``` bash
echo -n "No newline" >&2  # Use -n flag to suppress
```

**Using `>` instead of `>>` when appending:**

``` bash
echo "Line 1" > output.log
echo "Line 2" >> output.log  # >> appends, > overwrites
```

Proper stream handling is critical in production scripts—it determines whether your error messages actually reach the people monitoring your systems.
