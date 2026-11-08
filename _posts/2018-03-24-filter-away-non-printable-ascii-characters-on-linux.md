---
title: "Remove Non-Printable Characters in Linux"
date: 2018-03-24 11:41:12 +0000
layout: post
canonical: https://www.systutorials.com/filter-away-non-printable-ascii-characters-on-linux/
---

When processing text files or command output, non-printable ASCII characters corrupt formatting, break parsing, or create unexpected behavior. You need the right tool for your specific case — whether you’re stripping control characters, handling UTF-8, or cleaning up embedded escape sequences.

## Understanding Printable ASCII

The standard printable ASCII range includes:

- Tab (hex 09)
- Line Feed / Newline (hex 0A)
- Carriage Return (hex 0D)
- Printable characters (hex 20–7E)

Everything outside this range — including null bytes, bell characters, and escape sequences — is non-printable. The challenge is deciding what to preserve based on your input data.

## Using tr for Direct Filtering

The `tr` command is the fastest and most efficient tool for this job. Use `-c` (complement) to keep only characters you explicitly allow:

``` bash
tr -cd '[:print:]\n\t\r' < input.txt > output.txt
```

This keeps the POSIX `[:print:]` class (all printable characters and space), plus newlines, tabs, and carriage returns. If your system doesn’t support POSIX classes, use hex escapes:

``` bash
tr -cd '\x20-\x7E\x09\x0A\x0D' < input.txt > output.txt
```

To remove only control characters while preserving everything else (including high-bit characters for UTF-8):

``` bash
tr -d '[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]' < input.txt > output.txt
```

This targets the actual problem zones: null bytes, ASCII 0–8, ASCII 11–12, ASCII 14–31, and DEL (127).

## Using sed for Pattern-Based Filtering

When you need more control or want to perform additional transformations, `sed` handles pattern matching:

``` bash
sed 's/[^[:print:]\n\t\r]//g' input.txt > output.txt
```

Or to remove only control characters:

``` bash
sed 's/[[:cntrl:]]//g' input.txt > output.txt
```

The `[:cntrl:]` class is useful when processing UTF-8 files — it strips control codes without damaging multibyte sequences.

## Handling UTF-8 Properly

If your input contains valid UTF-8, removing entire high-bit characters destroys the data. Instead, target control characters only:

``` bash
tr -d '[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]' < input.txt > output.txt
```

Or with sed:

``` bash
sed 's/[[:cntrl:]]//g' input.txt > output.txt
```

Both preserve UTF-8 sequences (which use bytes in the 0x80–0xFF range) while removing actual control codes.

## Removing ANSI Escape Sequences

Log files often contain color codes and formatting sequences. Strip these with a two-step pipeline:

``` bash
cat messy.log | tr -d '[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]' | sed 's/\x1B\[[0-9;]*m//g' > clean.log
```

The first `tr` command removes control characters. The second `sed` command strips ANSI SGR (Select Graphic Rendition) codes — the escape sequences that handle colors and text attributes.

For more aggressive cleanup that also removes other escape sequences:

``` bash
sed 's/\x1B\[[^m]*m//g' input.txt > output.txt
```

## Comparing Performance

For large files:

- **tr** — Fastest. Optimized for character-by-character translation. Use this when possible.
- **sed** — Moderate speed. Better for complex patterns or multiple transformations in one pass.
- **grep** — Slowest for this use case. Line-buffered and overkill for character filtering.

For typical log processing (100MB files), `tr` completes in milliseconds while `sed` takes seconds.

## Practical Examples

Clean a file with mixed issues (control characters and escape codes):

``` bash
< noisy.txt tr -d '[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]' | sed 's/\x1B\[[0-9;]*m//g' > clean.txt
```

Extract only valid lines from binary-corrupted input:

``` bash
grep -aoP '[\x20-\x7E]{20,}' corrupted.bin
```

This finds sequences of at least 20 printable characters (useful for string extraction).

Process streaming data while preserving structure:

``` bash
tail -f application.log | tr -d '[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]'
```

## Edge Cases

**Null bytes in input:** `tr -d '\0' < input.txt > output.txt` removes only nulls.

**Preserving specific control characters:** If you need tabs and newlines but nothing else, use `tr -cd '\t\n' < input.txt > output.txt`.

**Testing what characters are present:** Use `od -c input.txt | head` to see all characters in octal, or `hexdump -C input.txt | head` for hex view.

Choose `tr` for straightforward filtering — it’s fast, simple, and reliable. Use `sed` when combining filtering with other transformations. Avoid overthinking it; the hex range `\x00-\x08\x0B\x0C\x0E-\x1F\x7F` removes all problematic control characters without damaging valid data.
