---
title: "Getting the Full Path of a Makefile"
date: 2018-03-24 11:50:34 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-get-the-full-path-and-directory-of-a-makefile-itself/
---

When you’re working in a Makefile, you often need to reference files relative to where the Makefile itself is located. This is especially useful for multi-directory projects or when your build system needs to know its own location.

## The Solution

Make provides the `MAKEFILE_LIST` variable, which contains the names of all makefiles that have been read. You can use this to determine the Makefile’s directory:

``` makefile
MAKEFILE_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

target:
    @echo "Makefile is in: $(MAKEFILE_DIR)"
```

Breaking this down:

- `$(lastword $(MAKEFILE_LIST))` — gets the last makefile in the list (your current Makefile)
- `$(abspath ...)` — converts it to an absolute path
- `$(dir ...)` — extracts just the directory portion

## Practical Examples

### Using the Directory in Your Build

``` makefile
MAKEFILE_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
PROJECT_ROOT := $(MAKEFILE_DIR)

# Reference source and output directories relative to Makefile location
SRC_DIR := $(PROJECT_ROOT)src
BUILD_DIR := $(PROJECT_ROOT)build
INCLUDE_DIR := $(PROJECT_ROOT)include

compile:
    gcc -I$(INCLUDE_DIR) -c $(SRC_DIR)/*.c -o $(BUILD_DIR)/
```

### Getting Just the Full Path

If you want the full path to the Makefile itself (not just its directory):

``` makefile
MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))

show-path:
    @echo "Full path: $(MAKEFILE_PATH)"
```

### Working with Included Makefiles

When you include other makefiles, `MAKEFILE_LIST` tracks all of them:

``` makefile
CURRENT_MAKEFILE := $(lastword $(MAKEFILE_LIST))
include subdir/sub.mk

# In sub.mk, you can access CURRENT_MAKEFILE from the parent
```

This is useful if you have a modular build system and need to know which makefile is currently being processed.

## Common Use Cases

**1. Source tree alongside build artifacts:**

``` makefile
MAKEFILE_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
DIST_DIR := $(MAKEFILE_DIR)dist
SCRIPTS_DIR := $(MAKEFILE_DIR)scripts

install:
    mkdir -p $(DIST_DIR)
    cp -r $(SCRIPTS_DIR)/* $(DIST_DIR)/
```

**2. Referencing configuration files:**

``` makefile
MAKEFILE_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
CONFIG := $(MAKEFILE_DIR)config.mk

include $(CONFIG)
```

**3. Docker or containerized builds:**

``` makefile
MAKEFILE_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

docker-build:
    docker build -f $(MAKEFILE_DIR)Dockerfile \
        --build-arg BUILD_DIR=$(MAKEFILE_DIR)build \
        -t myapp:latest .
```

## Important Notes

- This approach works consistently across different invocation methods (`make`, `make -f path/to/Makefile`, symlinked makefiles, etc.)
- The `abspath` function is the most reliable way to handle relative paths and ensures compatibility across different systems
- If your Makefile calls sub-makefiles recursively, each level will need its own definition if it needs to reference its own location
- Assignment happens at parse time, so the values are available throughout your entire Makefile

Store the result in a variable early in your Makefile to avoid recomputing it repeatedly.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
