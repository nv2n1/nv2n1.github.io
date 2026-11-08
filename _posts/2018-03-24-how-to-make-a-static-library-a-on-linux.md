---
title: "Building Static Libraries on Linux"
date: 2018-03-24 08:18:42 +0000
modified: 2026-04-12 16:38:55 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-make-a-static-library-a-on-linux/
---

Start by compiling your C source files into object files:

``` bash
gcc -c lib1.c lib2.c
```

This produces `lib1.o` and `lib2.o`. You can use any compiler flags here—`-Wall`, `-O2`, `-fPIC`, etc.—that match your build requirements. Position-independent code (`-fPIC`) isn’t strictly required for static libraries but is good practice if you anticipate reusing these objects elsewhere.

## Creating the static library with ar

Use `ar` to archive the object files into a static library:

``` bash
ar -cvq libmy.a lib1.o lib2.o
```

The flags mean:

- `-c` — create the archive (don’t warn if it doesn’t exist yet)
- `-v` — verbose output
- `-q` — quickly append files

After creation, you can inspect the library’s contents:

``` bash
ar -t libmy.a
```

This lists all object files archived inside. For more detail including symbol tables:

``` bash
ar -tv libmy.a
nm libmy.a
```

`nm` is particularly useful for checking which symbols are defined and which are undefined.

## Optimizing the library with ranlib

Modern versions of `ar` handle this automatically, but on older systems you may need to generate a symbol table index:

``` bash
ranlib libmy.a
```

This isn’t required on current Linux distributions (ar does it for you), but it’s harmless to run.

## Linking against the static library

### Direct path

Link directly by specifying the full path to the library:

``` bash
gcc -o p p.c libmy.a
```

### Using -L and -l flags

Or use search paths with the `-L` flag to specify the directory, and `-l` to specify the library name without the `lib` prefix and `.a` extension:

``` bash
gcc -o p p.c -L/path/to/lib/directory -lmy
```

The linker searches for `libmy.a` in the specified directory. You can chain multiple `-L` flags:

``` bash
gcc -o p p.c -L/usr/local/lib -L./lib -lmy -lpthread
```

### Static linking with multiple dependencies

If your library depends on other libraries, link them in order:

``` bash
gcc -o p p.c libmy.a -lpthread -lm
```

Order matters—the linker processes left to right, so dependent libraries should come after the libraries that depend on them.

## Using modern build tools

For production code, consider using `ar` through a build system rather than invoking it directly:

With CMake:

``` cmake
add_library(mylib STATIC lib1.c lib2.c)
target_link_libraries(myprogram mylib)
```

With Make:

``` makefile
libmy.a: lib1.o lib2.o
    ar -cvq $@ $^

lib1.o lib2.o: %.o: %.c
    gcc -c -Wall -O2 $< -o $@
```

This ensures consistent compilation flags and rebuilds only when necessary.

## Examining dependencies

To see what symbols your program needs from the library:

``` bash
nm -u p
```

Shows undefined symbols in your executable. Compare against the library:

``` bash
nm libmy.a
```

Symbols marked with `T` (text section) are defined; those marked `U` are undefined references that must be satisfied by linked libraries.

## 2026 Best Practices and Advanced Techniques

For Building Static Libraries on Linux, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
