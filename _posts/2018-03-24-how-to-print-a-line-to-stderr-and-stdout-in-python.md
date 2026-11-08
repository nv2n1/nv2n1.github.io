---
title: "How to Print to STDOUT and STDERR in Python"
date: 2018-03-24 11:52:57 +0000
layout: post
canonical: https://www.systutorials.com/how-to-print-a-line-to-stderr-and-stdout-in-python/
---

By default, `print()` writes to STDOUT. Both STDOUT and STDERR go to your terminal unless you redirect them. Here’s how to send output to each stream explicitly.

### Printing to STDOUT

The standard `print()` function writes to STDOUT and automatically adds a newline:

``` python
print("your message")
```

### Printing to STDERR

To print to STDERR, pass the `file` parameter:

``` python
import sys
print("your message", file=sys.stderr)
```

### Practical example

Create a test script to verify output goes to the right stream:

``` python
import sys

print("This goes to STDOUT")
print("This goes to STDERR", file=sys.stderr)
print("Back to STDOUT")
```

Run it and redirect only STDERR:

``` bash
python script.py 2>/tmp/stderr
cat /tmp/stderr
```

You’ll see only the STDERR message in `/tmp/stderr`, while the STDOUT messages appear on your terminal.

### Redirecting both streams separately

Capture STDOUT and STDERR to different files:

``` bash
python script.py > /tmp/stdout 2> /tmp/stderr
```

Or merge them together:

``` bash
python script.py 2>&1 | tee output.log
```

### Common patterns

**Suppress STDERR output:**

``` bash
python script.py 2>/dev/null
```

**Suppress STDOUT output:**

``` bash
python script.py 1>/dev/null
```

**Suppress both:**

``` bash
python script.py >/dev/null 2>&1
```

### Writing to STDERR in scripts

When writing tools or CLI scripts, use STDERR for errors, warnings, and diagnostic messages. Reserve STDOUT for actual output:

``` python
import sys

def process_file(filename):
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found", file=sys.stderr)
        sys.exit(1)
```

This way, other programs can safely pipe your STDOUT without capturing error messages.

### Additional print options

The `print()` function accepts other useful parameters:

``` python
import sys

# Suppress newline
print("no newline", end="", file=sys.stderr)

# Use custom separator for multiple arguments
print("error", "details", "here", sep=" | ", file=sys.stderr)

# Flush immediately (useful for real-time output)
print("Progress...", file=sys.stderr, flush=True)
```

The `flush=True` parameter is particularly useful when printing progress indicators or logs that need immediate display, rather than being buffered.

### Python 2 vs Python 3

If you encounter Python 2 code, it uses the older print statement syntax:

``` python
# Python 2 only (deprecated)
print >> sys.stderr, "your message"
```

Python 2 reached end-of-life in 2020. All new code should use Python 3’s `print()` function with the `file` parameter. If you’re maintaining legacy Python 2 code, migrate it to Python 3.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Common Pitfalls and Best Practices

When working with Python on Linux systems, keep these considerations in mind. Always use virtual environments to avoid polluting the system Python installation. Python 2 reached end-of-life in 2020, so ensure you are using Python 3 for all new projects.

For system scripting, prefer the subprocess module over os.system for better control over process execution. Use pathlib instead of os.path for cleaner file path handling in modern Python.

## Related Commands and Tools

These complementary Python tools and commands are useful for daily development workflows:

- python3 -m venv myenv – Create an isolated virtual environment
- pip list –outdated – Check which packages need updating
- python3 -m py_compile script.py – Check syntax without running
- black script.py – Auto-format code to PEP 8 standards
- mypy script.py – Static type checking for Python code

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
