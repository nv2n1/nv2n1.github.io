---
title: "Reading Environment Variables in Python"
date: 2018-03-24 11:51:50 +0000
modified: 2026-04-12 16:07:38 +0000
author: "Q A"
layout: post
categories: [languages-frameworks]
canonical: /how-to-get-an-environment-variable-in-python/
---

The most straightforward way to read an environment variable in Python is with `os.getenv()`:

``` python
import os

api_key = os.getenv('API_KEY')
print(api_key)
```

If the variable doesn’t exist, `getenv()` returns `None`. You can provide a default value as a fallback:

``` python
debug_mode = os.getenv('DEBUG', 'False')
port = os.getenv('PORT', '8000')
```

For variables that must exist, use `os.environ[]` instead. This raises a `KeyError` if the variable isn’t set, which is useful for catching configuration errors early:

``` python
import os

required_token = os.environ['DATABASE_URL']
```

## Type Conversion and Validation

Environment variables are always strings. Convert them to appropriate types:

``` python
import os

port = int(os.getenv('PORT', '8000'))
debug = os.getenv('DEBUG', 'False').lower() == 'true'
timeout = float(os.getenv('TIMEOUT', '30.0'))
```

For more complex validation, consider a dedicated library. `python-dotenv` loads variables from a `.env` file during development:

``` python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')
```

Install it with `pip install python-dotenv`. This is useful for local development but production deployments should source variables directly from your orchestration platform (Kubernetes, systemd, Docker, etc.).

## Using Pydantic for Configuration

Modern Python projects often use Pydantic for structured configuration management:

``` python
from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str
    debug: bool = False
    port: int = 8000
    database_url: str = Field(..., alias='DATABASE_URL')

    class Config:
        env_file = '.env'

settings = Settings()
```

This approach provides validation, type checking, and clear documentation of required variables. Install with `pip install pydantic-settings`.

## Accessing All Variables

To inspect all environment variables:

``` python
import os

for key, value in os.environ.items():
    print(f'{key}={value}')
```

Check if a variable exists without retrieving its value:

``` python
import os

if 'API_KEY' in os.environ:
    api_key = os.environ['API_KEY']
```

## Production Considerations

Never hardcode secrets or rely on defaults for sensitive values. Use environment variables or secret management systems (Kubernetes Secrets, AWS Secrets Manager, HashiCorp Vault) to provide credentials at runtime.

In containerized environments, pass variables through your orchestration layer rather than `.env` files. Docker passes variables with `-e FLAG=value` or `--env-file`, Kubernetes uses ConfigMaps and Secrets, and systemd services use `Environment=` directives in unit files.

For applications that run across multiple environments, validate that required variables are present on startup:

``` python
import os
import sys

required_vars = ['API_KEY', 'DATABASE_URL', 'SERVICE_NAME']
missing = [var for var in required_vars if var not in os.environ]

if missing:
    print(f'Error: Missing required environment variables: {", ".join(missing)}', file=sys.stderr)
    sys.exit(1)
```

This fails fast rather than causing cryptic errors later during execution.

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
