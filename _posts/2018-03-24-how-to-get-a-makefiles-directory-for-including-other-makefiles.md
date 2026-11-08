---
title: "Finding the Directory of a Makefile for Includes"
date: 2018-03-24 08:20:32 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-get-a-makefiles-directory-for-including-other-makefiles/
---

When you have shared Makefiles included across multiple projects in different directory structures, relative includes break. If `common.mk` tries to `include release.mk` and both files are in a subdirectory like `external/`, the include fails because Make uses the current working directory, not the location of the including file.

For example, this structure works fine:

    Makefile
    common.mk
    release.mk

But this one fails:

    Makefile
    external/common.mk
    external/release.mk

When `external/common.mk` contains `include release.mk`, Make looks for `release.mk` in the current directory, not in `external/`.

## The solution: Use MAKEFILE_LIST

The key is to get the directory of the currently-executing Makefile using `MAKEFILE_LIST`:

``` makefile
SELF_DIR := $(dir $(lastword $(MAKEFILE_LIST)))
```

This variable is automatically maintained by Make and contains the list of all Makefiles being processed. The `lastword` function gets the most recently included file (the current one), and `dir` extracts its directory path.

Now you can safely include sibling files:

``` makefile
include $(SELF_DIR)/release.mk
```

This works regardless of where the top-level Makefile is located or what the current working directory is.

## Practical example

Given the directory structure:

    Makefile
    external/common.mk
    external/release.mk

**Makefile:**

``` makefile
include external/common.mk

all:
    @echo "Building..."
```

**external/common.mk:**

``` makefile
SELF_DIR := $(dir $(lastword $(MAKEFILE_LIST)))

include $(SELF_DIR)/release.mk

.PHONY: all
```

**external/release.mk:**

``` makefile
RELEASE_VERSION := 1.0.0

release: all
    @echo "Releasing v$(RELEASE_VERSION)"
```

Running `make` from the top directory works correctly — `external/release.mk` is found even though the current directory is the project root.

## Handling nested includes

If you have deeper nesting or multiple levels of includes, the technique scales without modification. Each Makefile gets its own `SELF_DIR`:

``` makefile
# external/common.mk
SELF_DIR := $(dir $(lastword $(MAKEFILE_LIST)))
include $(SELF_DIR)/release.mk
include $(SELF_DIR)/build/targets.mk

# external/build/targets.mk
SELF_DIR := $(dir $(lastword $(MAKEFILE_LIST)))
include $(SELF_DIR)/../release.mk  # Still works
```

Each call to `$(lastword $(MAKEFILE_LIST))` returns the correct file for that context, so redefining `SELF_DIR` in each file is safe and keeps includes self-contained.

## Common pitfall: pwd vs SELF_DIR

Don’t confuse this with using `$(PWD)` or shell commands like `$(shell pwd)`. Those depend on where Make was invoked from, not where the Makefile is located. Using `MAKEFILE_LIST` is the correct, reliable approach that works in any invocation context.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
