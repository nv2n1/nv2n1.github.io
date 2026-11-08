---
title: "How to List Functions in a Linux Static Library"
date: 2018-03-24 08:18:25 +0000
layout: post
canonical: https://www.systutorials.com/how-to-list-the-functions-in-a-a-library-on-linux/
---

The `nm` command displays symbolic information from object files, libraries, and executables. It’s the standard tool for inspecting what functions and variables are defined or referenced in a static library (`.a` file).

### Basic usage

List all symbols in a library:

``` bash
nm lib.a
```

This outputs symbol names, but the default format can be hard to parse. You’ll see output like:

    archive.a:file.o:
    0000000000000000 T function_name
                     U external_function
    0000000000001234 D global_variable

The letters indicate the symbol type:

- `T` — function or data in the text (code) section
- `D` — initialized global data
- B\` — uninitialized global data (BSS section)
- `U` — undefined symbol (external reference)
- `a` — absolute symbol
- `R` — read-only data

### More useful formats

Display symbols with cleaner output:

``` bash
nm -D lib.a
```

However, `-D` works better with shared objects. For static libraries, use:

``` bash
nm --defined-only lib.a
```

This shows only defined symbols, filtering out external references.

For a more readable format with symbol types clearly labeled:

``` bash
nm -B lib.a
```

The `-B` flag uses BSD-style output (equivalent to `--format=bsd`).

### Filtering symbols

Show only functions (text symbols):

``` bash
nm lib.a | grep ' T '
```

Show only undefined symbols (external dependencies):

``` bash
nm lib.a | grep ' U '
```

Show symbols sorted by size:

``` bash
nm -S lib.a | sort -k2 -n
```

### Extracting function names only

If you just need clean function names without addresses or metadata:

``` bash
nm lib.a | grep ' T ' | awk '{print $3}'
```

Or using a more modern approach with `nm`‘s output formats:

``` bash
nm --format=posix lib.a | grep ' T ' | cut -d' ' -f1
```

### Checking multiple libraries

Inspect all `.a` files in a directory:

``` bash
for lib in *.a; do
    echo "=== $lib ==="
    nm "$lib" | grep ' T '
done
```

### Integration with build systems

When debugging linking issues, check what symbols are exported:

``` bash
nm -g lib.a
```

The `-g` flag shows only global symbols, which is useful when a library has many static (file-scope) symbols you don’t care about.

For detailed information on symbol versions or relocations, use:

``` bash
nm -l lib.a
```

This includes source filenames and line numbers where available.

### Related tools

For shared objects (`.so` files), `nm` still works but `objdump` provides more detail:

``` bash
objdump -t lib.so
```

For a tree view of dependencies between object files in a library:

``` bash
ar t lib.a
```

This lists the object files contained in the archive, which you can then inspect individually with `nm`.

## Troubleshooting Common Issues

When encountering problems on Linux systems, follow a systematic approach. Check system logs first using journalctl for systemd-based distributions. Verify service status with systemctl before attempting restarts. For network issues, use ip addr and ss -tulpn to diagnose connectivity problems.

Package management issues often stem from stale caches. Run dnf clean all on Fedora or apt clean on Ubuntu before retrying failed installations. If a package has unmet dependencies, try resolving them with dnf autoremove or apt autoremove.

## Related System Commands

These commands are frequently used alongside the tools discussed in this article:

- systemctl status service-name – Check if a service is running
- journalctl -u service-name -f – Follow service logs in real time
- rpm -qi package-name – Query installed package information
- dnf history – View package transaction history
- top or htop – Monitor system resource usage

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
