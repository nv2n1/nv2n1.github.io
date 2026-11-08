---
title: "Comparing Linux Hex Viewers: xxd, od, hexdump, and hd"
date: 2018-03-24 11:40:36 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /printing-a-file-in-hexadecimal-format-of-all-content-on-linux/
---

Viewing file contents in hexadecimal is essential for debugging binaries, inspecting file headers, analyzing corrupted data, and understanding file formats. Linux provides several tools for this, each with different strengths.

## xxd

`xxd` is the most commonly used hex viewer. By default, it displays hex on the left and ASCII representation on the right:

``` bash
xxd file.txt
```

Output:

    00000000: 4865 6c6c 6f20 576f 726c 6421 0a          Hello World!.

For plain hex without ASCII or addresses, use `-p`:

``` bash
xxd -p file.txt
```

This outputs continuous hex—useful for piping to other tools or processing:

``` bash
xxd -p file.bin | tr -d '\n'  # Remove newlines for one long hex string
```

Limit output to specific byte ranges:

``` bash
xxd -l 256 file.txt          # First 256 bytes
xxd -s 0x100 file.txt        # Start at offset 0x100
xxd -s 0x100 -l 256 file.txt # From 0x100 for 256 bytes
```

View only specific columns:

``` bash
xxd -c 32 file.txt  # Show 32 bytes per line instead of 16
```

Reverse hex dump back to binary:

``` bash
xxd -r -p hexfile.txt > binary.bin  # Convert plain hex to binary
xxd -r hexfile.txt > binary.bin     # Convert formatted hex to binary
```

## od (Octal Dump)

`od` is a POSIX standard utility available on all Unix systems. For hexadecimal output, use `-A x` for hex addresses and `-t x1` for single-byte hex values:

``` bash
od -A x -t x1 file.txt
```

Add `-v` to show all lines (without it, repeated patterns compress):

``` bash
od -A x -t x1 -v file.txt
```

Show 32-bit values in hex:

``` bash
od -A x -t x4 file.txt
```

## hexdump

`hexdump` offers clean, canonical formatting:

``` bash
hexdump -C file.txt
```

The `-C` flag provides hex+ASCII output similar to `xxd`. For custom output formats:

``` bash
hexdump -e '16/1 "%02x " "\n"' file.txt  # 16 bytes per line
hexdump -e '8/1 "%02x " "  "' -e '8/1 "%_p" "\n"' file.txt  # Two columns
```

## hd (Hexdump Alias)

On most systems, `hd` is an alias for `hexdump -C`:

``` bash
hd file.txt
```

It’s the quickest option if you want the default behavior.

## Practical Examples

Compare changes in a binary file:

``` bash
xxd old.bin > old.hex
xxd new.bin > new.hex
diff -u old.hex new.hex
```

View the first 512 bytes of a device (e.g., disk boot sector):

``` bash
xxd -l 512 /dev/sda
```

View the first 4KB of a large file without loading it all:

``` bash
head -c 4096 largefile.bin | xxd
```

Extract hex for a specific byte range in a file:

``` bash
xxd -s 1024 -l 256 file.bin | xxd -r -p  # Extract bytes 1024-1280
```

Convert plain hex string back to binary:

``` bash
echo "48656c6c6f" | xxd -r -p > output.bin
```

Search for a hex pattern in a binary file:

``` bash
xxd file.bin | grep "4865 6c6c"  # Search for "Hell"
```

Display file signature (magic bytes):

``` bash
xxd -l 16 file.bin  # View first 16 bytes to identify file type
```

## Performance Considerations

For large files, `xxd` and `hexdump` stream efficiently. Always use `-l` to avoid dumping gigabytes to your terminal:

``` bash
xxd -l 1M /dev/sda  # Safe: only 1 MB
```

When searching through massive files, pipe selectively:

``` bash
head -c 10M largefile.bin | xxd | grep "pattern"
```

## Which Tool to Use?

- **`xxd`**: Default choice for interactive use. Best readability, installed on nearly all Linux systems, excellent flag support.
- **`hexdump -C` / `hd`**: Quick option with clean output, good for scripting.
- **`od`**: POSIX standard, guaranteed to exist on any Unix system, useful for analyzing binary data structures with specific byte widths.
