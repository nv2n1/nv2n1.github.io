---
title: "Compressing Files in Linux: gzip, bzip2, 7z, rar, and zip"
date: 2013-03-25 12:52:29 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-compressuncompress-files-in-linux-using-gzip-bzip2-7z-rar-and-zip/
---

File compression is a routine task in Linux administration. You’ll encounter several tools, each with different tradeoffs between compression ratio, speed, and compatibility. This guide covers the most common compression formats: gzip, bzip2, 7z, xz, and zip.

The examples below assume you’re compressing a directory called `dir`. Each tool supports compression level options — you can use maximum compression (slower, smaller files) or faster compression (larger files). The commands shown use maximum compression; strip those flags if you prefer speed over size.

## gzip

Gzip is fast and widely available. It’s not ideal for archiving entire directory trees since it compresses a single stream, but it’s common for single files and as part of tar operations.

**Compress:**

``` bash
gzip -r --best -c dir > ./dir.gz
```

**Uncompress:**

``` bash
gunzip ./dir.gz
# or
gzip -d ./dir.gz
```

For faster compression without maximum compression:

``` bash
gzip -r -c dir > ./dir.gz
```

## bzip2

Bzip2 offers better compression than gzip but is slower. Pair it with tar for directory compression.

**Compress:**

``` bash
tar -c dir | bzip2 --best -c > ./dir.tar.bz2
```

**Uncompress:**

``` bash
tar xf ./dir.tar.bz2
# or
bunzip2 -c ./dir.tar.bz2 | tar x
```

Faster compression:

``` bash
tar -c dir | bzip2 -c > ./dir.tar.bz2
```

## xz

Xz provides excellent compression ratios, often better than bzip2, though it’s slower. It’s increasingly the default compression in many distributions.

**Compress:**

``` bash
tar -cf - dir | xz --best -c > ./dir.tar.xz
```

**Uncompress:**

``` bash
tar xf ./dir.tar.xz
```

Faster compression:

``` bash
tar -cf - dir | xz -c > ./dir.tar.xz
```

You can also use tar’s built-in xz support:

``` bash
tar -cJf ./dir.tar.xz dir
```

## 7z

7z delivers excellent compression but is slower and less portable. It’s useful when maximum compression matters and you control the decompression environment.

**Compress:**

``` bash
7z a -t7z -m0=lzma2 -mx=9 -mfb=64 -md=32m -ms=on ./dir.7z dir
```

**Uncompress:**

``` bash
7z x ./dir.7z
```

Faster compression:

``` bash
7z a -t7z ./dir.7z dir
```

## RAR

RAR is proprietary and less common on Linux. Most distributions don’t include it by default. If you must work with RAR files, install `rar` or `unrar`:

**Compress (requires `rar` package):**

``` bash
rar a -m5 ./dir.rar dir
```

**Uncompress:**

``` bash
unrar x ./dir.rar
# or
rar x ./dir.rar
```

Most scenarios benefit from open formats (gzip, bzip2, xz, 7z) instead. Use RAR primarily for compatibility with Windows environments.

## ZIP

Zip is portable across Windows, macOS, and Linux. It’s slower than gzip but more compatible for cross-platform sharing.

**Compress:**

``` bash
zip -r -9 ./dir.zip dir
```

**Uncompress:**

``` bash
unzip ./dir.zip
```

Faster compression:

``` bash
zip -r ./dir.zip dir
```

Exclude files during compression:

``` bash
zip -r -9 ./dir.zip dir -x "*.log" "*.tmp"
```

## Quick Comparison

| Tool | Ratio | Speed | Portable | Use Case |
|----|----|----|----|----|
| gzip | Good | Fast | Excellent | Single files, streaming |
| bzip2 | Better | Slow | Good | Archives, older systems |
| xz | Excellent | Slow | Good | Modern distributions, long-term storage |
| 7z | Excellent | Slowest | Fair | Maximum compression, controlled environment |
| ZIP | Fair | Moderate | Excellent | Cross-platform sharing |
| RAR | Good | Moderate | Poor | Proprietary, legacy support |

## Practical Tips

**Multithreaded compression:** Gzip, bzip2, and xz all have multithreaded variants for faster compression on modern hardware:

``` bash
# pigz (parallel gzip)
pigz -r -9 -c dir > ./dir.gz

# pbzip2 (parallel bzip2)
pbzip2 --best -c < file.txt > file.txt.bz2

# xz with multiple threads
xz --threads=4 --best file
```

**Verify integrity:** After decompression, verify the archive wasn’t corrupted:

``` bash
gzip -t ./dir.gz
7z t ./dir.7z
unzip -t ./dir.zip
```

**List contents without extracting:**

``` bash
tar -tzf ./dir.tar.gz
7z l ./dir.7z
unzip -l ./dir.zip
```

**Remove source after compression:** Safely delete the original only after verifying the compressed file:

``` bash
tar -czf dir.tar.gz dir && rm -rf dir
```

For most Linux systems, xz provides the best balance of compression ratio and modern tool support. Use gzip for compatibility and speed, zip for cross-platform scenarios, and 7z when maximum compression is essential.
