---
title: "Getting Epoch Timestamps in Python"
date: 2018-03-24 11:52:13 +0000
author: "Q A"
layout: post
categories: [languages-frameworks]
canonical: /how-to-get-the-epoch-timestamp-in-python/
---

Python offers several ways to get the current epoch timestamp, each suited to different use cases. The choice depends on your precision requirements and whether you’re working with timezone-aware operations.

## Using time.time()

The simplest approach is `time.time()`, which returns the current time as a float representing seconds since the Unix epoch (January 1, 1970, 00:00:00 UTC):

``` python
import time

epoch_seconds = time.time()
print(epoch_seconds)  # Output: 1735689600.123456
```

If you need an integer, cast it:

``` python
epoch_seconds_int = int(time.time())
```

This works across all platforms and is the standard for compatibility. However, it has microsecond precision at best and the float representation can accumulate rounding errors in long-running processes.

## Using datetime with UTC Timezone

For timezone-aware operations and clearer intent, use the `datetime` module:

``` python
from datetime import datetime, timezone

epoch_seconds = int(datetime.now(timezone.utc).timestamp())
```

This is more explicit about handling UTC and integrates better with code that manipulates dates and times. The `timezone.utc` ensures you’re always working in UTC regardless of your system’s local timezone.

## High-Precision Timestamps with Nanoseconds

For performance monitoring, distributed tracing, and high-frequency logging, use `time.time_ns()` to get nanosecond precision:

``` python
import time

epoch_nanoseconds = time.time_ns()
epoch_milliseconds = epoch_nanoseconds // 1_000_000
epoch_microseconds = epoch_nanoseconds // 1_000
```

This avoids floating-point precision issues entirely and is essential when correlating events across microsservices or measuring sub-millisecond latencies.

## Comparison

| Method | Precision | Returns | Use Case |
|----|----|----|----|
| `time.time()` | Microseconds | Float | General purpose, compatibility |
| `datetime.now(timezone.utc).timestamp()` | Microseconds | Float | Timezone-aware, date/time manipulation |
| `time.time_ns()` | Nanoseconds | Integer | Performance monitoring, tracing |

## Practical Examples

**Logging with millisecond precision:**

``` python
import time
import logging

logging.basicConfig(
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

timestamp_ms = int(time.time() * 1000)
logging.info(f"Event at {timestamp_ms}")
```

**Measuring elapsed time:**

``` python
import time

start = time.time_ns()
# ... do work ...
elapsed_ns = time.time_ns() - start
elapsed_ms = elapsed_ns / 1_000_000
print(f"Took {elapsed_ms:.2f}ms")
```

**Converting to datetime for readability:**

``` python
from datetime import datetime, timezone
import time

timestamp = time.time()
readable = datetime.fromtimestamp(timestamp, tz=timezone.utc)
print(readable)  # Output: 2026-01-01 12:30:45.123456+00:00
```

For most applications, `time.time()` remains the default choice. Use `datetime` methods when you need timezone awareness or plan to perform date arithmetic. Reserve `time.time_ns()` for scenarios where microsecond precision is insufficient—typically observability infrastructure, performance testing, or systems programming where you’re measuring very short durations.

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
