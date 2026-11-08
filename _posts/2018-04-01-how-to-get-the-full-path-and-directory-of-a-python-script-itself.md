---
title: "Getting the Full Path of a Python Script"
date: 2018-04-01 14:41:12 +0000
layout: post
canonical: https://www.systutorials.com/how-to-get-the-full-path-and-directory-of-a-python-script-itself/
---

When you need to load configuration files, data files, or assets relative to your script’s location, the current working directory won’t work — it depends entirely on where you called the script from, not where the script actually lives.

Use `pathlib.Path`:

``` python
from pathlib import Path

# The directory where the script lives
script_dir = Path(__file__).resolve().parent
print(script_dir)

# Full path to the script itself
script_path = Path(__file__).resolve()
print(script_path)
```

The `.resolve()` call is critical — it follows symlinks and normalizes the path, giving you the true canonical location. This matters in production when scripts are symlinked or deployed through containers.

## Practical Examples

Loading a config file relative to your script:

``` python
from pathlib import Path

script_dir = Path(__file__).resolve().parent
config_file = script_dir / "config.yaml"

if config_file.exists():
    with open(config_file) as f:
        config = yaml.safe_load(f)
else:
    print(f"Config not found at {config_file}")
```

Working with assets in a subdirectory:

``` python
from pathlib import Path

script_dir = Path(__file__).resolve().parent
assets_dir = script_dir / "assets"
logo = assets_dir / "logo.png"

# Safe to use even if directory doesn't exist yet
assets_dir.mkdir(parents=True, exist_ok=True)
```

## When `__file__` Doesn’t Work

In some situations, `__file__` isn’t available:

- **Interactive Python shells** — `__file__` doesn’t exist in REPL or Jupyter
- **Frozen executables** — PyInstaller, cx_Freeze, and similar tools may not set `__file__`
- **Entry points** — Some package installations don’t preserve `__file__` reliably

For these cases, use alternatives:

``` python
import sys
from pathlib import Path

# Fallback chain
try:
    script_path = Path(__file__).resolve()
except NameError:
    # __file__ not available, try sys.argv[0]
    script_path = Path(sys.argv[0]).resolve()

script_dir = script_path.parent
```

For **PyInstaller** executables specifically, use:

``` python
import sys

if getattr(sys, 'frozen', False):
    # Running as compiled executable
    script_dir = Path(sys.executable).parent
else:
    # Running as normal Python script
    script_dir = Path(__file__).resolve().parent
```

## With Modern Project Structures

If you’re using a package with `pyproject.toml` and installing via `pip install -e .` (editable mode), you have better options. Use `importlib.resources` for bundled data files:

``` python
from importlib.resources import files

# Access bundled resources relative to a package
package_files = files('my_package')
config = package_files / 'config.yaml'

with files('my_package').joinpath('data.json').open() as f:
    data = json.load(f)
```

This approach works correctly whether your package is installed normally, in editable mode, or packaged as a wheel. It’s the recommended pattern for distributable Python packages.

For simple scripts that aren’t part of a package, the `pathlib` approach works fine. For anything being distributed or installed, prefer `importlib.resources`.

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
