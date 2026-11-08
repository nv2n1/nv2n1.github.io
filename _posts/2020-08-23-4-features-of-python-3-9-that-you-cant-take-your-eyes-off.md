---
title: "Python 3.9\u2019s Most Impactful New Features"
date: 2020-08-23 03:19:25 +0000
modified: 2026-04-11 17:11:39 +0000
author: "Aaronjacobson"
layout: post
categories: [languages-frameworks]
canonical: /4-features-of-python-3-9-that-you-cant-take-your-eyes-off/
---

Python 3.9 brought several substantial improvements over earlier versions. While it’s now past EOL as of October 2025, understanding its features provides context for migration planning and why the Python ecosystem shifted toward 3.10+. That said, if you’re maintaining legacy 3.9 code, these features remain relevant to your codebase.

## Dictionary Merge and Update Operators

The merge operator (`|`) and update operator (`|=`) simplified working with multiple dictionaries. Before 3.9, merging dictionaries required either `.update()` calls or unpacking syntax that felt clunky:

``` python
# Pre-3.9
x = {'zero': 0, 'one': 1}
y = {'nine': 9, 'ten': 10}
z = {**x, **y}

# Python 3.9+
z = x | y
```

The update operator modifies the original dictionary:

``` python
x = {'zero': 0, 'one': 1}
y = {'nine': 9, 'ten': 10}
x |= y
# x is now {'zero': 0, 'one': 1, 'nine': 9, 'ten': 10}
```

If keys overlap, the rightmost dictionary wins:

``` python
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = x | y
# z is {'a': 1, 'b': 3, 'c': 4}
```

This operator became particularly useful in configuration management, where merging default settings with environment-specific overrides happens frequently.

## Flexible Function and Variable Annotations

Type hints in Python 3.9 became more flexible. You could now use built-in collection types directly in annotations instead of importing from `typing`:

``` python
# Pre-3.9 required typing imports
from typing import List, Dict

def process(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}

# Python 3.9+
def process(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}
```

This change reduced boilerplate significantly. You could annotate with `list`, `dict`, `tuple`, and `set` directly without importing alternatives from the `typing` module. For complex scenarios, `typing` still offered `Generic`, `Protocol`, and other advanced constructs.

## String Methods: removeprefix() and removesuffix()

Python 3.9 added two straightforward string methods that eliminated the need for manual slicing or regex:

``` python
"Hello World".removeprefix("Hello ")
# Returns: "World"

"filename.tar.gz".removesuffix(".gz")
# Returns: "filename.tar"

# These methods return the original string if prefix/suffix doesn't match
"test.txt".removeprefix("data_")
# Returns: "test.txt"
```

While seemingly minor, these methods prevented off-by-one errors in string manipulation and improved code readability compared to regex-based approaches:

``` python
# Old approach with regex
import re
filename = "archive.tar.gz"
filename = re.sub(r'\.gz$', '', filename)

# 3.9 approach
filename = "archive.tar.gz"
filename = filename.removesuffix(".gz")
```

## New PEG Parser

Python 3.9 introduced an experimental PEG (Parsing Expression Grammar) parser as a replacement for the LL(1) parser used since Python’s inception. The LL(1) parser had fundamental limitations that prevented certain language improvements.

The PEG parser:

- Handles more complex grammar patterns
- Resolved ambiguities in the language grammar
- Enabled future syntax improvements (like match statements in 3.10)
- Improved error messages in some cases

While users rarely interacted with this change directly, it was foundational for Python’s evolution. The new parser became the default in 3.10, allowing features like structural pattern matching that wouldn’t have been possible under LL(1) constraints.

## IPv6 Scoping

Python 3.9 improved IPv6 address handling with scoping support:

``` python
from ipaddress import IPv6Address

# IPv6 addresses with zone IDs (scope)
addr = IPv6Address('fe80::1%eth0')
print(addr)
```

This mattered for applications handling link-local IPv6 addresses, which require zone identification to function correctly.

## Other Notable Additions

**GraphQL-related improvements:** Better support for deferred evaluation in annotations, useful for forward references without strings.

**Relaxed decorator grammar:** You could use any expression as a decorator, not just names and attribute accesses:

``` python
# Now valid
decorators = [log_calls, validate_args]
@decorators[0]
def my_function():
    pass
```

**Zoneinfo module:** New standard library support for IANA time zone database, replacing reliance on system tzdata.

By 3.10 and beyond, these features became standard practice. If you’re maintaining 3.9 codebases, knowing these features helps explain design choices. For new projects, move to 3.11+ for better performance, type narrowing, and exception groups.
