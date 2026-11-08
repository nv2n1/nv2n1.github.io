---
title: "Python\u2019s os.makedirs() with mode 0o777 doesn\u2019t grant write permissions to others"
date: 2018-03-24 11:54:30 +0000
layout: post
canonical: https://www.systutorials.com/in-python-os-makedirs-with-0777-mode-does-not-give-others-write-permission/
---

When you call `os.makedirs(path, mode=0o777)` in Python, the resulting directory often won’t have the permissions you expect. The mode argument gets masked by the process’s umask, which removes certain permission bits before applying them to the filesystem.

Your umask acts as a filter. If your umask is `0o022` (common on many systems), it removes write permissions for group and others:

    0o777 & ~0o022 = 0o755

This means `os.makedirs(path, mode=0o777)` creates a directory with `0o755` permissions (rwxr-xr-x), not `0o777` (rwxrwxrwx).

## Checking and Changing Your Umask

View your current umask:

``` bash
umask
```

If you need to temporarily change it before calling `os.makedirs()`:

``` python
import os

# Get current umask (this sets it to 0, then restores the original)
current_umask = os.umask(0)
os.umask(current_umask)

# Create directory with full permissions
os.makedirs('/tmp/test_dir', mode=0o777)

# Restore original umask
os.umask(current_umask)
```

However, changing the umask process-wide is rarely the right solution—it affects all subsequent file creation in your process.

## Better Approaches

**Use `chmod()` after creation** (recommended):

``` python
import os

os.makedirs('/tmp/test_dir', mode=0o777, exist_ok=True)
os.chmod('/tmp/test_dir', 0o777)
```

This is explicit and doesn’t manipulate your umask. Any future calls to `mkdir()` or file creation still respect your original umask.

**Create with restricted permissions, then expand**:

``` python
import os

os.makedirs('/tmp/test_dir', mode=0o700, exist_ok=True)
os.chmod('/tmp/test_dir', 0o777)
```

This is safer—the directory starts private, then gets opened up only when needed.

**Use context manager for temporary umask changes**:

``` python
import os
from contextlib import contextmanager

@contextmanager
def temporary_umask(new_umask):
    old_umask = os.umask(new_umask)
    try:
        yield
    finally:
        os.umask(old_umask)

with temporary_umask(0):
    os.makedirs('/tmp/test_dir', mode=0o777, exist_ok=True)
```

This ensures your umask is restored even if an exception occurs.

## Security Considerations

Before setting 0o777 on directories, consider:

- **Do you actually need world-writable directories?** This is a security risk in production. Anyone can modify files there.
- **Is this a temporary directory?** Use `/tmp` with proper naming conventions and verify ownership.
- **Are you running in a container?** Docker and other containers can restrict capabilities regardless of permissions.
- **What’s the principle of least privilege?** Start restrictive (0o700) and relax only when necessary.

For shared development environments, prefer `0o770` (group-writable) with appropriate group membership, or `0o755` (world-readable but only owner-writable) for most cases.

## Checking Actual Permissions

After creating a directory, verify permissions:

``` python
import os
import stat

os.makedirs('/tmp/test_dir', exist_ok=True)
os.chmod('/tmp/test_dir', 0o777)

mode = os.stat('/tmp/test_dir').st_mode
permissions = oct(stat.S_IMODE(mode))
print(f"Directory permissions: {permissions}")
```

This tells you exactly what permissions the filesystem actually assigned, accounting for umask interference.

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
