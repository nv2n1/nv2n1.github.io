---
title: "Check File Readability and Writability in Python"
date: 2018-03-24 11:51:14 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-detect-whether-a-file-is-readable-and-writable-in-python/
---

The most straightforward approach is `os.access()`, which tests whether the process has the requested access to a file:

``` python
import os

file_path = "example.txt"

# Check if file is readable
if os.access(file_path, os.R_OK):
    print("File is readable")

# Check if file is writable
if os.access(file_path, os.W_OK):
    print("File is writable")

# Check if file exists and is executable
if os.access(file_path, os.X_OK):
    print("File is executable")

# Check multiple permissions at once
if os.access(file_path, os.R_OK | os.W_OK):
    print("File is readable and writable")
```

`os.access()` respects the actual filesystem permissions and the effective user ID, making it reliable for security checks. However, keep in mind that on some filesystems (particularly network-mounted ones), `os.access()` may not behave consistently.

## Using pathlib.Path for modern Python

The `pathlib` module provides a cleaner interface and is the recommended approach in modern Python:

``` python
from pathlib import Path

file_path = Path("example.txt")

# Check if file exists
if file_path.exists():
    print("File exists")

# Check readability and writability
if file_path.stat().st_mode & 0o400:
    print("Owner can read")

if file_path.stat().st_mode & 0o200:
    print("Owner can write")
```

For a more direct approach using `os.access()` with `pathlib`:

``` python
from pathlib import Path
import os

file_path = Path("example.txt")

if os.access(file_path, os.R_OK):
    print("Readable")

if os.access(file_path, os.W_OK):
    print("Writable")
```

## Try-except approach for practical checks

The most robust method in practice is attempting the actual operation and handling exceptions:

``` python
def can_read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            f.read(1)
        return True
    except (IOError, OSError, PermissionError):
        return False

def can_write_file(file_path):
    try:
        with open(file_path, 'a'):
            pass
        return True
    except (IOError, OSError, PermissionError):
        return False

# Usage
if can_read_file("example.txt"):
    print("File is readable")

if can_write_file("example.txt"):
    print("File is writable")
```

This approach catches actual permission errors that might occur, including those on network filesystems where `os.access()` can be unreliable.

## Checking permissions before file operations

When you need to perform actual operations, combine permission checks with error handling:

``` python
from pathlib import Path
import os

def safe_file_operation(file_path):
    path = Path(file_path)

    # Pre-flight checks
    if not path.exists():
        raise FileNotFoundError(f"{file_path} does not exist")

    if not os.access(path, os.R_OK):
        raise PermissionError(f"Cannot read {file_path}")

    # Proceed with operation
    content = path.read_text()
    return content

# Or for write operations
def safe_write_operation(file_path, content):
    path = Path(file_path)

    if not os.access(path, os.W_OK):
        raise PermissionError(f"Cannot write to {file_path}")

    path.write_text(content)
```

## Edge cases and considerations

**Temporary permission changes**: Permissions can change between check and use (race condition). Always wrap actual file operations in try-except blocks regardless of prior checks.

**Network filesystems**: NFS and similar systems may return misleading results from `os.access()`. The try-except approach is more reliable here.

**Virtual filesystems**: Some special filesystems (/proc, /sys on Linux) don’t report permissions accurately. Always verify behavior in your specific environment.

**Effective vs. real permissions**: On Unix systems, `os.access()` checks effective permissions (what the current process can do). Use `stat()` to check actual file mode bits if you need the raw mode information.

**Windows differences**: Windows doesn’t use Unix-style permission bits. File access is determined by ACLs. `os.access()` still works but behaves differently—use the try-except approach for cross-platform code.

## Type-hinted helper function

For larger codebases, wrap permission checks in a type-hinted utility:

``` python
from pathlib import Path
from typing import Literal

def check_file_access(
    file_path: str | Path,
    mode: Literal["r", "w", "x", "a"] = "r"
) -> bool:
    """Check if file is accessible for the given mode."""
    try:
        with open(file_path, mode):
            pass
        return True
    except (IOError, OSError, PermissionError):
        return False

# Usage
if check_file_access("data.txt", "r"):
    print("Ready to read")
```

Use `os.access()` for quick permission checks, but rely on exception handling when performing actual file operations. This combination ensures robust, cross-platform code that handles edge cases correctly.
