---
title: "Static Linking C and C++ Programs with GCC on Linux"
date: 2014-01-01 03:50:47 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-statically-link-c-and-c-programs-on-linux-with-gcc/
---

Static linking embeds all library code directly into your binary. On Linux, this sounds straightforward but glibc introduces complications that pure static binaries don’t truly exist — the C library still loads dynamic features at runtime like NSS (Name Service Switch), locale data, and character set converters. Understanding these constraints is essential before committing to static linking.

## When Static Linking Makes Sense

Static linking solves real problems in specific scenarios:

- **Reproducible builds** — binaries work identically across Linux distributions without worrying about glibc version differences
- **Simplified deployment** — no need to manage shared library dependencies on target systems
- **Embedded systems** — reduced attack surface and predictable memory layout
- **Legacy environment support** — systems where installing dev libraries isn’t an option

For most modern applications, better alternatives exist:

- **musl libc** — designed from scratch for static linking; produces smaller, truly portable binaries
- **Containers** (Docker, Podman) — manage dependencies consistently without static compilation overhead
- **AppImage or similar formats** — portable execution with runtime dependency bundling
- **Cross-compilation toolchains** — musl-based cross-compilers for embedded targets

## The glibc Static Linking Reality

If you choose glibc static linking anyway, be aware of these gotchas:

**DNS resolution breaks easily** — NSS loads shared libraries at runtime for hostname lookups. Without proper `/etc/nsswitch.conf` on the target system or alternative DNS solutions, your binary won’t resolve hostnames. Solutions include hardcoding IPs, using `getaddrinfo()` with careful fallbacks, or linking against `musl-libc` instead.

**Binary size explodes** — glibc static linking produces 5-10MB binaries even for simple programs. musl produces 200KB for equivalent functionality.

**dlopen() and plugins don’t work** — you can’t dynamically load shared libraries from a statically-linked binary.

**Character encoding issues** — missing GCONV_PATH environment variable can break locale conversion on systems with different glibc installations.

**Licensing complications** — glibc is LGPL; static linking may trigger license obligations if you redistribute binaries.

## Static Linking C Programs

Install static C library headers and archives:

``` bash
# Fedora/RHEL/CentOS
sudo dnf install glibc-static

# Debian/Ubuntu
sudo apt-get install libc6-static
```

Compile with `-static`:

``` bash
gcc -static program.c -o program
```

Verify the binary is statically linked:

``` bash
ldd program
```

Expected output:

    not a dynamic executable

When using standard library functions that depend on other libraries (like `pthread_create()`), specify them on the command line:

``` bash
# Correct: libraries before the program works too, but conventional placement
gcc -static program.c -lpthread -lm -o program
```

**Library link order matters.** The linker processes libraries in command order; if a later object file needs symbols from an earlier library, they won’t resolve. When in doubt, test both orders:

``` bash
# Safe: list libraries at the end
gcc -static program.c -o program -lpthread -lm

# Also safe with explicit ordering
gcc -static -Wl,--start-group program.c -lpthread -lm -Wl,--end-group -o program
```

For external libraries, ensure static `.a` files exist on your system. Most package managers install dynamic libraries by default:

``` bash
gcc -static program.c -o program -L/usr/lib -lz -lpthread
```

## Static Linking C++ Programs

Install C++ standard library static packages:

``` bash
# Fedora/RHEL/CentOS
sudo dnf install glibc-static libstdc++-static

# Debian/Ubuntu
sudo apt-get install libc6-static libstdc++6-static
```

Compile with GCC flags for static runtime libraries:

``` bash
g++ -static -static-libstdc++ -static-libgcc program.cpp -o program
```

Flag meanings:

- `-static` — attempt to link all libraries statically (glibc exceptions apply)
- `-static-libstdc++` — link libstdc++ statically instead of dynamically
- `-static-libgcc` — link libgcc statically

Verify with `ldd`:

``` bash
ldd program
# Output: not a dynamic executable
```

With external C++ libraries like OpenSSL or Boost, ensure static `.a` files are available and explicitly link them:

``` bash
g++ -static -static-libstdc++ -static-libgcc program.cpp \
  -o program \
  -L/usr/lib/x86_64-linux-gnu \
  -lssl -lcrypto -lpthread
```

For Boost libraries:

``` bash
g++ -static -static-libstdc++ -static-libgcc program.cpp \
  -o program \
  -L/usr/lib/x86_64-linux-gnu \
  -lboost_system -lboost_filesystem -lpthread
```

## CMake Configuration for Static Linking

Force CMake to find and use static library variants:

``` cmake
set(CMAKE_FIND_LIBRARY_SUFFIXES ".a")
set(CMAKE_EXE_LINKER_FLAGS "-static-libgcc -static-libstdc++")

find_package(OpenSSL REQUIRED)
find_package(ZLIB REQUIRED)

target_link_libraries(my_target OpenSSL::Crypto OpenSSL::SSL ZLIB::ZLIB)
```

This tells CMake to prefer `.a` files over `.so` when searching for libraries. The `find_package()` calls handle the complexity of locating static variants automatically.

For projects with complex dependencies, consider using a dedicated build environment or container to ensure all static library variants are available.

## Inspecting Statically-Linked Binaries

Verify what’s actually compiled in:

``` bash
# Check for unexpected dynamic references
ldd program

# List all symbols (far too many to read, but useful for grep)
nm program | wc -l

# Search for embedded library names (should find none or very few)
strings program | grep -E "\.so\.|lib.*\.a"
```

Check actual runtime behavior:

``` bash
# Monitor libraries loaded at runtime
strace -e open,openat ./program 2>&1 | grep "\.so"

# Inspect memory map of running process
cat /proc/<pid>/maps
```

Even with `-static`, glibc may attempt to load NSS modules, locale data, or timezone information from `/etc` or `/usr/share`. This is expected and not a sign of failure — only if those files don’t exist and hostname lookups fail is there a real problem.

## Testing Across Distributions

Always test your statically-linked binary on the actual target systems. Binary compatibility isn’t guaranteed between:

- Different major glibc versions (CentOS 7 vs. Ubuntu 22.04)
- Different CPU architectures (even if both are x86-64)
- Systems with significantly different `/etc` configurations

Create a test matrix with at least three target distributions before deploying statically-linked binaries in production. Consider containers as a safer alternative for multi-distribution scenarios.
