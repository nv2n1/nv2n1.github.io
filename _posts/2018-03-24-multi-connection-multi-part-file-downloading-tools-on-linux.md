---
title: "Parallel Download Tools for Linux: aria2, axel, and curl"
date: 2018-03-24 08:21:21 +0000
modified: 2026-04-11 16:03:42 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /multi-connection-multi-part-file-downloading-tools-on-linux/
---

When you need to download large files faster, parallelizing across multiple connections can significantly improve throughput. Standard tools like `wget` and `curl` use single connections by default, but several alternatives support multi-connection downloads that can achieve 3-5x speedups on capable networks.

## aria2c

aria2 is the most powerful option. It handles HTTP, HTTPS, FTP, BitTorrent, and Metalink protocols, supports multiple simultaneous sources, and offers granular control over connection behavior.

Basic multi-connection download:

``` bash
aria2c -x 10 -s 10 -k 1M http://example.com/largefile.iso
```

Flag breakdown:

- `-x 10` — maximum 10 connections per host
- `-s 10` — split file into 10 segments
- `-k 1M` — minimum 1MB per segment (prevents excessive fragmentation)

With custom output directory and filename:

``` bash
aria2c -x 10 -s 10 -k 1M -d /path/to/dir/ -o custom_name.iso http://example.com/largefile.iso
```

For resumable downloads with crash recovery:

``` bash
aria2c -x 10 -s 10 -k 1M --continue=true --allow-overwrite=false \
  -d /downloads/ http://example.com/file.iso
```

When downloading multiple files concurrently:

``` bash
aria2c -x 5 -s 5 -j 3 http://example.com/file1.iso http://example.com/file2.iso http://example.com/file3.iso
```

The `-j 3` flag processes 3 files in parallel. When running multiple concurrent downloads, reduce `-x` to avoid overwhelming the server — 5 connections per file across 3 parallel jobs is typically safe.

aria2 also maintains a session file, which is useful for resuming interrupted batch downloads:

``` bash
aria2c --save-session=/tmp/session.txt -x 5 -s 5 http://example.com/file1.iso http://example.com/file2.iso

# Resume later with:
aria2c --load-session=/tmp/session.txt
```

## axel

axel is lightweight and straightforward for simple HTTP/HTTPS downloads. It has minimal dependencies and lower memory overhead than aria2, making it suitable for resource-constrained systems or quick one-off downloads.

``` bash
axel -n 10 http://example.com/largefile.zip
```

The `-n 10` flag opens 10 parallel connections. axel automatically handles reassembly, so there’s no manual cleanup needed. It also supports resume with `-a` flag:

``` bash
axel -n 10 -a http://example.com/largefile.zip
```

## curl with GNU Parallel

For integration into shell scripts or pipelines, combine `curl` with GNU Parallel. This approach offers flexibility but requires manual file size calculation and range header setup.

First, determine file size:

``` bash
curl -sI http://example.com/file | grep -i content-length
```

Then split and download:

``` bash
FILESIZE=1073741824
PARTS=10
PARTSIZE=$((FILESIZE / PARTS))

seq 0 $((PARTS - 1)) | parallel -j 10 \
  "curl -r \$(({}*PARTSIZE))-\$((({} + 1)*PARTSIZE - 1)) \
  http://example.com/file -o file.part.{}"

cat file.part.* > file && rm file.part.*
```

This approach works well when you need to integrate downloads into larger automation workflows, but it’s more verbose than dedicated tools.

## Choosing the Right Tool

**aria2c**: Use for complex scenarios, multiple file downloads, BitTorrent support, or when you need session persistence and metadata handling. Best for production automation and large-scale batch operations.

**axel**: Pick for straightforward HTTP/HTTPS downloads on systems with tight resource constraints. Ideal for shell scripts and embedded environments.

**curl + parallel**: Useful for custom pipelines where you need full control over the download logic or must integrate with existing curl-based workflows.

## Server Compatibility

Not all servers support multi-connection downloads. Check before attempting:

``` bash
curl -I http://example.com/file | grep -i accept-ranges
```

If the response shows `Accept-Ranges: bytes`, the server supports range requests. If it’s absent or shows `Accept-Ranges: none`, multi-connection downloads won’t help — you’ll receive the full file from each connection.

## Connection Limits and Rate Limiting

Most servers limit concurrent connections per client to prevent abuse. Start conservative:

- Use `-x 5` or `-x 10` initially
- If you receive `429 Too Many Requests` responses, reduce connection count
- Respect `Retry-After` headers in server responses
- Add delays between requests if the server rate-limits aggressively

For aria2, configure a global connection limit to avoid accidental DOS-like behavior:

``` bash
aria2c -x 5 -s 5 --max-overall-download-limit=10M http://example.com/file
```

## Performance Expectations

On modern broadband with cooperative servers, multi-connection downloads typically provide 3-5x speedup over single-connection transfers. Actual gains depend on:

- Server bandwidth capacity
- Network latency and stability
- Number of available connections allowed
- File size (larger files benefit more from parallelization)

For files under 100MB, single-connection downloads are often sufficient. Multi-connection approaches shine with files in the gigabyte range or when bandwidth is shared across many competing transfers.
