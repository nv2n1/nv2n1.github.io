---
title: "Iterating Over Files and Directories in Python"
date: 2018-03-24 11:48:34 +0000
layout: post
canonical: https://www.systutorials.com/how-to-iterate-all-files-and-directories-under-a-directory-in-python/
---

When you need to traverse a directory tree in Python, you have several options. The choice depends on whether you want recursive traversal, how you want to handle the results, and your Python version.

## Using os.walk()

The `os.walk()` function is the classic approach for recursively iterating through directories. It yields tuples of `(dirpath, dirnames, filenames)` for each directory in the tree:

``` python
import os

for root, dirs, files in os.walk('/mnt/data/'):
    print(f"Directory: {root}")
    for dir_name in dirs:
        print(f"  Subdirectory: {dir_name}")
    for file_name in files:
        print(f"  File: {file_name}")
```

This will output:

    Directory: /mnt/data/
      File: file.txt
      Subdirectory: great

To get the full paths:

``` python
import os

for root, dirs, files in os.walk('/mnt/data/'):
    for file_name in files:
        full_path = os.path.join(root, file_name)
        print(full_path)
```

## Using pathlib (Modern Approach)

`pathlib.Path` is the modern, object-oriented way to handle paths in Python 3.4+. It’s more readable and handles cross-platform path differences automatically.

For non-recursive iteration:

``` python
from pathlib import Path

path = Path('/mnt/data/')
for item in path.iterdir():
    if item.is_file():
        print(f"File: {item}")
    elif item.is_dir():
        print(f"Directory: {item}")
```

For recursive iteration:

``` python
from pathlib import Path

path = Path('/mnt/data/')
for item in path.rglob('*'):
    if item.is_file():
        print(f"File: {item}")
    elif item.is_dir():
        print(f"Directory: {item}")
```

Use `glob()` for pattern matching:

``` python
from pathlib import Path

path = Path('/mnt/data/')
for file in path.rglob('*.txt'):
    print(file)
```

## Controlling Recursion Depth with os.walk()

To limit how deep you traverse:

``` python
import os

max_depth = 2
for root, dirs, files in os.walk('/mnt/data/'):
    depth = root.replace('/mnt/data/', '').count(os.sep)
    if depth >= max_depth:
        dirs.clear()  # Prevents walking deeper
    for file_name in files:
        print(os.path.join(root, file_name))
```

Modifying the `dirs` list in-place affects which subdirectories `os.walk()` visits next.

## Filtering During Iteration

Skip hidden files:

``` python
from pathlib import Path

path = Path('/mnt/data/')
for item in path.rglob('*'):
    if item.name.startswith('.'):
        continue
    print(item)
```

## Performance Considerations

For large directory trees:

- `pathlib` is generally faster and more memory-efficient
- `os.walk()` is still reliable and widely compatible
- Both use generators, so memory usage is minimal

For extremely large directories with millions of files, consider using `os.scandir()` directly:

``` python
import os

for entry in os.scandir('/mnt/data/'):
    if entry.is_file():
        print(entry.path)
    elif entry.is_dir():
        print(entry.path)
```

## Key Differences

| Method | Recursive | Cross-platform | Modern | Best For |
|----|----|----|----|----|
| `os.walk()` | Yes | Yes | No | Legacy code, compatibility |
| `pathlib.rglob()` | Yes | Yes | Yes | General use, pattern matching |
| `pathlib.iterdir()` | No | Yes | Yes | Single directory, clean code |
| `os.scandir()` | No | Yes | Yes | Performance-critical code |

For new Python projects, `pathlib` is the recommended approach. Use `os.walk()` when maintaining legacy code or when you need fine-grained control over recursion behavior.

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
