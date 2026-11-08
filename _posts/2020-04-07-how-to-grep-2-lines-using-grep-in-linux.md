---
title: "Matching Consecutive Lines with grep in Linux"
date: 2020-04-07 13:35:08 +0000
layout: post
canonical: https://www.systutorials.com/how-to-grep-2-lines-using-grep-in-linux/
---

grep processes input line-by-line by design, which makes matching patterns across multiple lines challenging. However, several approaches exist to search for consecutive lines as a single block, each with different tradeoffs.

## The problem

You need to verify that a file contains two specific consecutive lines with nothing between them. For example, checking if `~/.bashrc` has:

    export GOPATH=$HOME/go
    export PATH=$GOPATH/bin:$PATH

Standard line-by-line matching won’t help here. grep’s default behavior treats newlines as separators, not as part of the pattern itself.

## Using grep with -Pz (memory-efficient for small files)

The most straightforward approach uses two options together:

- `-z`: Treat input as null-byte-terminated instead of newline-terminated, reading the entire file as a single string
- `-P`: Use Perl-compatible regular expressions (PCRE), which properly handle `\n` as literal newline characters

``` bash
grep -Pz 'export GOPATH=\$HOME/go\nexport PATH=\$GOPATH/bin:\$PATH' ~/.bashrc
```

Breaking it down:

- `\n` matches the newline between the two lines
- `\$` escapes dollar signs (special in PCRE)
- The pattern matches anywhere in the file — no leading/trailing newlines required

For use in conditionals or scripts, add the `-q` flag to suppress output:

``` bash
grep -Pzq 'export GOPATH=\$HOME/go\nexport PATH=\$GOPATH/bin:\$PATH' ~/.bashrc && echo "Found" || echo "Not found"
```

## Practical examples with grep -Pz

Check for a specific comment followed by a function:

``` bash
grep -Pz '# Initialize database\nfunction init_db' setup.sh
```

Find two consecutive error patterns in logs:

``` bash
grep -Pz 'Connection timeout\nFailed to reconnect' app.log
```

Match lines with variable content between them (useful for JSON/YAML):

``` bash
grep -Pz 'server:\s+\{[^}]*"enabled":\s*true' config.json
```

The pattern `[^}]*` matches any characters except the closing brace, allowing flexibility in what appears between fields.

Verify a configuration block with optional whitespace:

``` bash
grep -Pz 'database:\n\s+host:' database.yml
```

## Limitations of grep -Pz

**Memory usage**: The `-z` option reads the entire file into memory as a single string. For multi-gigabyte files, this causes memory exhaustion. Use `head`, `tail`, or `sed` to limit input:

``` bash
head -100 largefile.log | grep -Pz 'pattern1\npattern2'
```

**Null bytes**: If your file contains actual null bytes, `-z` will break on them.

**PCRE support**: Some minimal grep implementations (busybox grep) don’t support `-P`. GNU grep does. Verify your version:

``` bash
grep --version
```

## pcregrep (better for large files)

If you’re on a system without GNU grep or prefer not to load entire files into memory, use `pcregrep`:

``` bash
pcregrep -M 'export GOPATH=\$HOME/go\nexport PATH=\$GOPATH/bin:\$PATH' ~/.bashrc
```

The `-M` flag enables multiline mode. pcregrep is part of the PCRE toolkit and explicitly designed for this use case. It reads input more efficiently than grep’s `-z` option and handles file streaming better.

## awk (best for POSIX portability and efficiency)

For maximum portability and to avoid loading entire files into memory, use awk:

``` bash
awk '/export GOPATH=\$HOME\/go/ { getline; if (/export PATH=\$GOPATH\/bin:\$PATH/) print "Found" }' ~/.bashrc
```

This approach:

- Reads the next line after matching the first pattern
- Checks if it matches the second pattern
- Avoids loading the entire file into memory
- Works on all POSIX systems
- More efficient for large files

For checking without printing:

``` bash
awk '/export GOPATH=\$HOME\/go/ { getline; if (/export PATH=\$GOPATH\/bin:\$PATH/) exit 0 } END { exit 1 }' ~/.bashrc && echo "Found"
```

## sed (another POSIX alternative)

Use sed’s `N` command to append the next line to the pattern space:

``` bash
sed -n '/export GOPATH=\$HOME\/go/{N;/export PATH=\$GOPATH\/bin:\$PATH/p;}' ~/.bashrc
```

This approach also avoids memory overhead and works on all POSIX systems. The `-n` flag suppresses default printing, and `p` prints only matching lines.

For conditional use:

``` bash
sed -n '/export GOPATH=\$HOME\/go/{N;/export PATH=\$GOPATH\/bin:\$PATH/p;}' ~/.bashrc | grep -q . && echo "Found" || echo "Not found"
```

## Choosing the right tool

- **grep -Pz**: Quick one-liners on files \< 100 MB. Simplest syntax, but PCRE dependency
- **pcregrep**: When grep doesn’t support `-P`, or for better streaming behavior
- **awk**: Most portable, most efficient for large files, best for complex logic
- **sed**: When you need POSIX compliance and have straightforward patterns

For production scripts handling logs or configuration files, awk or sed are safer choices than loading entire files into memory with grep -z.
