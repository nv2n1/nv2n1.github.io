---
title: "Suppress \u201cEntering/Leaving Directory\u201d Messages in Recursive Make"
date: 2018-03-24 11:44:04 +0000
layout: post
canonical: https://www.systutorials.com/how-to-suppress-entering-leaving-messages-when-invoking-make-recursively/
---

When running `make` recursively with `$(MAKE)` or `make -C`, you’ll see verbose messages like “Entering directory” and “Leaving directory” for each subdirectory. These messages clutter the build output and make it harder to spot actual errors.

## The Quick Fix

Pass `--no-print-directory` to make:

```wp-block-code
make --no-print-directory
```

Or set it in your Makefile:

```wp-block-code
.MAKEFLAGS: --no-print-directory
```

## Suppressing via MAKEFLAGS Environment Variable

Set the flag globally for all make invocations:

```wp-block-code
export MAKEFLAGS="--no-print-directory"
make
```

Add to your `~/.bashrc` for permanent effect:

```wp-block-code
export MAKEFLAGS="--no-print-directory"
```

## How the Messages Are Generated

GNU Make prints these messages automatically when it changes directories during recursive builds. The messages look like:

```wp-block-code
make[1]: Entering directory '/home/user/project/src'
make[2]: Entering directory '/home/user/project/src/lib'
cc -c file.c -o file.o
make[2]: Leaving directory '/home/user/project/src/lib'
make[1]: Leaving directory '/home/user/project/src'
```

Each level of recursion adds a bracketed number (`make[1]`, `make[2]`, etc.) indicating the depth.

## Using –print-directory Selectively

If you want directory messages for some sub-makes but not others, use `--print-directory` to re-enable them:

```wp-block-code
# In top-level Makefile
.MAKEFLAGS: --no-print-directory

# In a specific sub-Makefile where you want messages
.MAKEFLAGS: --print-directory
```

## Clean Build Output

For truly clean build output, combine `--no-print-directory` with other flags:

```wp-block-code
# Suppress directory messages, run in parallel, show only errors
make --no-print-directory -j$(nproc) --quiet
```

Or create a wrapper script:

```wp-block-code
#!/bin/bash
# build.sh - clean build output
make --no-print-directory "$@" 2>&1 | grep -v "^make\[" | grep -v "Entering\|Leaving"
```

## Alternative: Use Recursive Make Sparingly

The “Recursive Make Considered Harmful” paper by Peter Miller argues that recursive make builds are slower and more error-prone than non-recursive builds. Consider restructuring your project to use a single top-level Makefile:

```wp-block-code
# Single Makefile for the entire project
SUBDIRS = src lib tests

.PHONY: all $(SUBDIRS)

all: $(SUBDIRS)

src:
    $(MAKE) -C src

lib:
    $(MAKE) -C lib

tests: src lib
    $(MAKE) -C tests
```

Or use modern build systems like `CMake`, `Meson`, or `Ninja` that handle subdirectory builds cleanly without verbose directory change messages.

## Other Useful Make Flags

- `-j N` — Run N parallel jobs (use `-j$(nproc)` for all cores)
- `-B` — Unconditionally rebuild all targets
- `-n` — Dry run (show commands without executing)
- `-k` — Continue building after errors (for finding all errors at once)
- `--warn-undefined-variables` — Warn when using undefined variables
- `--debug=v` — Show why make decides to rebuild each target

## Quick Reference

- `make --no-print-directory` — Suppress entering/leaving messages
- `MAKEFLAGS=--no-print-directory` — Environment variable approach
- `.MAKEFLAGS: --no-print-directory` — Makefile directive

## Make Parallel Builds

When running parallel builds with `-j`, the entering/leaving directory messages become especially noisy since multiple sub-makes run concurrently. Always suppress them in parallel mode:

```wp-block-code
make -j$(nproc) --no-print-directory
```

## Build Log Filtering

If you can’t modify the Makefile or command line, filter the output after the fact:

```wp-block-code
# Remove entering/leaving messages from build log
make 2>&1 | grep -v "Entering directory\|Leaving directory" | tee build.log

# Show only warnings and errors
make 2>&1 | grep -E "warning:|error:|Error" | tee errors.log

# Colorize errors in real time
make 2>&1 | grep --color=auto -E "^|error:|Error"
```

## Make and CMake Integration

If your project uses CMake as the meta-build system, CMake generates Makefiles that use recursive make. Suppress directory messages in the CMake build:

```wp-block-code
cmake -DCMAKE_VERBOSE_MAKEFILE=ON ..
make --no-print-directory -j$(nproc)
```

Or set the flag in your CMakeLists.txt:

```wp-block-code
set(CMAKE_VERBOSE_MAKEFILE ON)
set(CMAKE_MAKE_PROGRAM "make --no-print-directory")
```
