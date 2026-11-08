---
title: "Reading Environment Variables in Python"
date: 2018-03-24 11:52:10 +0000
modified: 2026-04-12 16:09:24 +0000
author: "Q A"
layout: post
categories: [languages-frameworks]
canonical: /how-to-get-an-environment-variable-in-python-2/
---

Environment variables are essential for configuration management—API keys, database URLs, feature flags, and environment-specific settings should never be hardcoded. Python provides straightforward mechanisms to access them.

## The os Module

The standard way to read environment variables is with the `os` module:

``` python
import os

api_key = os.environ['API_KEY']
```

This raises a `KeyError` if the variable doesn’t exist. For safer handling, use `get()` with a default:

``` python
import os

api_key = os.environ.get('API_KEY', 'default-key')
debug_mode = os.environ.get('DEBUG', 'False').lower() == 'true'
```

## The pathlib.Path Approach

For file paths specifically, combine environment variables with `pathlib`:

``` python
from pathlib import Path
import os

config_dir = Path(os.environ.get('CONFIG_DIR', '/etc/myapp'))
log_file = config_dir / 'app.log'
```

## Type-Safe Access with python-dotenv

For local development, the `python-dotenv` package loads variables from a `.env` file:

``` bash
pip install python-dotenv
```

``` python
from dotenv import load_dotenv
import os

load_dotenv()  # Loads from .env in the current directory
database_url = os.environ.get('DATABASE_URL')
```

This is useful for development but shouldn’t be used in containerized production environments—pass variables directly via Docker environment flags or orchestration tools.

## Handling Type Conversion

Environment variables are always strings. Convert them explicitly:

``` python
import os

port = int(os.environ.get('PORT', '8000'))
timeout = float(os.environ.get('TIMEOUT', '30.0'))
enable_cache = os.environ.get('ENABLE_CACHE', 'false').lower() in ('true', '1', 'yes')
```

## Using Pydantic for Validation

For larger applications, use Pydantic to validate and type-check environment variables:

``` python
from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    api_key: str
    debug: bool = False
    port: int = 8000
    database_url: Optional[str] = None

    class Config:
        env_file = '.env'

settings = Settings()
```

Pydantic automatically raises validation errors if required variables are missing or have incorrect types.

## Best Practices

- **Never commit secrets**: Use `.env` locally but add it to `.gitignore`. In CI/CD pipelines, inject secrets via your platform’s native secret management (GitHub Secrets, GitLab CI/CD variables, etc.).
- **Fail fast**: For required configuration, let the application crash on startup rather than silently using defaults. This makes misconfiguration obvious immediately.
- **Use containers consistently**: When using Docker, define variables in your `docker-compose.yml` or pass them at runtime. This ensures local development matches production.
- **Document required variables**: Maintain a `.env.example` file showing all required variables without sensitive values.

## Checking If a Variable Exists

``` python
import os

if 'API_KEY' in os.environ:
    api_key = os.environ['API_KEY']
else:
    api_key = None  # or raise an error
```

## Listing All Environment Variables

``` python
import os

for key, value in os.environ.items():
    print(f"{key}={value}")
```

For debugging, this can be useful—but be careful not to log or expose sensitive values in production.

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
