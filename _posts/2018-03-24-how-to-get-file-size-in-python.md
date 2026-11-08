---
title: "Get File Size in Python"
date: 2018-03-24 11:48:39 +0000
modified: 2026-04-12 16:05:09 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-get-file-size-in-python/
---

Getting a file’s size is a common task in Python. There are several ways to do it, depending on what you need and how much detail you want about the file.

## Using os.path.getsize()

The simplest approach is `os.path.getsize()`:

``` python
import os

file_path = '/path/to/your/file.txt'
size_bytes = os.path.getsize(file_path)
print(f"File size: {size_bytes} bytes")
```

This returns the size in bytes. It raises `OSError` if the file doesn’t exist or isn’t accessible.

## Using pathlib (Recommended)

For modern Python 3 code, `pathlib.Path` is cleaner and more flexible:

``` python
from pathlib import Path

file_path = Path('/path/to/your/file.txt')
size_bytes = file_path.stat().st_size
print(f"File size: {size_bytes} bytes")
```

This also raises `OSError` if the file is inaccessible, but gives you access to other file metadata through the `stat()` object.

## Handling Errors

Always handle the case where a file doesn’t exist:

``` python
from pathlib import Path

file_path = Path('/path/to/your/file.txt')
try:
    size_bytes = file_path.stat().st_size
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
```

Or check before accessing:

``` python
from pathlib import Path

file_path = Path('/path/to/your/file.txt')
if file_path.exists():
    size_bytes = file_path.stat().st_size
    print(f"File size: {size_bytes} bytes")
```

## Human-Readable Sizes

Converting bytes to a readable format is useful for logging and reporting:

``` python
from pathlib import Path

def format_bytes(bytes_size):
    """Convert bytes to human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024
    return f"{bytes_size:.2f} PB"

file_path = Path('/path/to/your/file.txt')
size_bytes = file_path.stat().st_size
print(f"File size: {format_bytes(size_bytes)}")
```

## Getting Sizes Recursively

If you need the total size of a directory:

``` python
from pathlib import Path

def dir_size(path):
    """Calculate total size of all files in a directory."""
    total = 0
    for item in Path(path).rglob('*'):
        if item.is_file():
            total += item.stat().st_size
    return total

size_bytes = dir_size('/path/to/directory')
print(f"Directory size: {size_bytes} bytes")
```

## Performance Notes

- `pathlib.Path.stat()` is efficient for a single file and provides comprehensive metadata.
- For directories with many files, recursive traversal can be slow. Consider using `os.walk()` if you need to filter by file type or pattern.
- Use generators when processing large directory trees to avoid loading everything into memory.

## Comparing Methods

| Method | Pros | Cons |
|----|----|----|
| `os.path.getsize()` | Simple, widely compatible | Returns only size, no other metadata |
| `pathlib.Path.stat()` | Modern, provides full metadata, cleaner API | Requires Python 3.4+ |
| `os.stat()` | Access to more metadata | Slightly lower-level API |

For new code, use `pathlib` unless you have specific compatibility requirements with older Python versions.

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
