---
title: "Splitting Text Files by Lines on Linux: A split Command Guide"
date: 2018-03-24 08:22:17 +0000
modified: 2026-04-11 16:02:49 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-split-a-text-file-by-lines-on-linux/
---

The `split` command is the standard tool for breaking large text files into smaller chunks on Linux. Here’s the basic syntax:

``` bash
split -l 1024 content.txt splitted-content.txt-
```

This creates output files named `splitted-content.txt-aa`, `splitted-content.txt-ab`, and so on, with each containing 1024 lines.

## Understanding output naming

By default, `split` appends two-character suffixes starting with `aa`. The naming scheme continues alphabetically:

- `splitted-content.txt-aa` (lines 1–1024)
- `splitted-content.txt-ab` (lines 1025–2048)
- `splitted-content.txt-ac` (lines 2049–3072)

If you need more than 676 splits (26² combinations), increase the suffix length with `-a`:

``` bash
split -l 1024 -a 3 content.txt splitted-content.txt-
```

This generates three-character suffixes: `aaa`, `aab`, `aac`, etc.

## Numeric suffixes for easier processing

For cleaner sorting and scripting, use numeric suffixes with `-d`:

``` bash
split -l 1024 -d content.txt splitted-content.txt-
```

Output files become: `splitted-content.txt-00`, `splitted-content.txt-01`, `splitted-content.txt-02`, etc.

This is particularly useful when processing files programmatically, since numeric sorting is more predictable across different locales and shells.

## Splitting by file size instead of lines

When line count is irrelevant or you’re working with mixed content, use `-b` to split by byte size:

``` bash
split -b 10M content.txt splitted-content.txt-
```

This creates files approximately 10MB each. Useful for handling large files before transfer or parallel processing.

You can also use units like `G` for gigabytes or `K` for kilobytes:

``` bash
split -b 1G largefile.bin chunk-
```

## Splitting into a specific number of chunks

To divide a file into exactly N equal parts regardless of size, use `-n`:

``` bash
split -n 4 content.txt splitted-content.txt-
```

This creates four roughly equal-sized files. With `-n l/N`, you can also split based on line count distribution:

``` bash
split -n l/10 content.txt chunk-
```

## Practical examples

**Split a large CSV file for parallel processing:**

``` bash
split -l 50000 data.csv chunk-

for file in chunk-*; do
  process_csv "$file" &
done
wait
```

**Split and compress output on the fly:**

``` bash
split -l 1024 content.txt - | gzip > content.txt.split.gz
```

**Verify line counts after splitting:**

``` bash
for file in splitted-content.txt-*; do
  echo "$file: $(wc -l < "$file") lines"
done
```

**Check total file size of chunks:**

``` bash
du -sh splitted-content.txt-* | tail -1
```

## Reassembling split files

Combine chunks back into a single file:

``` bash
cat splitted-content.txt-* > content.txt
```

With numeric suffixes, ensure proper ordering using brace expansion:

``` bash
cat splitted-content.txt-{00..99} > content.txt
```

For alphabetic suffixes, the glob expansion typically respects the original order in modern shells, but verify the chunk count matches your expectation.

## Handling permissions and ownership

The `split` command creates output files with default permissions (usually 0644). If you need specific permissions:

``` bash
split -l 1024 content.txt splitted-content.txt-
chmod 600 splitted-content.txt-*
chown user:group splitted-content.txt-*
```

## Common gotchas

**Uneven final chunk:** If file size isn’t evenly divisible, the last chunk contains fewer lines than specified. This is expected behavior and not an error.

**Memory with very long lines:** The `split` command processes line-by-line rather than in fixed buffers. Files with extremely long lines (\>1GB per line) may cause memory issues, though this is rare in practice.

**Glob expansion order:** When reassembling with `cat splitted-*`, verify alphabetic or numeric order matches your expectation. Use explicit ranges or pipe through `sort` if unsure:

``` bash
cat $(ls -1 splitted-content.txt-* | sort) > content.txt
```

**Preserving content after split:** Always verify the output before deleting the original file:

``` bash
split -l 50000 large.txt chunk-
wc -l large.txt chunk-* | tail -1  # Verify line counts match
rm large.txt
```

The `split` command remains the most efficient and portable way to divide text files on Linux, requiring no additional tools or dependencies.
