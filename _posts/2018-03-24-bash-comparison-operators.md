---
title: "Bash Comparison Operators: Complete Guide to String, Integer, and File Tests"
date: 2018-03-24 08:22:50 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/bash-comparison-operators/
---

Bash provides comparison operators for conditionals through the `test` command (aliased as `[`), the `[[ ]]` compound command, and the `(( ))` arithmetic command. Each has specific use cases and behavior differences worth understanding.

## String Comparisons

String comparisons work with `test`/`[` and `[[ ]]`:

| Operator             | Meaning                                        |
|----------------------|------------------------------------------------|
| `-n STRING`          | String length is nonzero (true if not empty)   |
| `-z STRING`          | String length is zero (true if empty)          |
| `STRING1 = STRING2`  | Strings are equal                              |
| `STRING1 != STRING2` | Strings are not equal                          |
| `STRING1 < STRING2`  | STRING1 sorts before STRING2 lexicographically |
| `STRING1 > STRING2`  | STRING1 sorts after STRING2 lexicographically  |

The `<` and `>` operators require `[[ ]]` or escaping in `[ ]` (e.g., `\<` and `\>`). Always use `=` for equality in both `[ ]` and `[[ ]]`; avoid `==` in POSIX contexts.

``` bash
# Check if string is empty
if [[ -z "$config_file" ]]; then
    echo "Error: config file not specified"
    exit 1
fi

# String equality
if [[ "$username" == "admin" ]]; then
    echo "Admin access granted"
fi

# Lexicographic comparison
if [[ "$version" > "1.0.0" ]]; then
    echo "Version is 1.0.0 or higher"
fi
```

## Integer Comparisons

Use arithmetic-specific operators for integer comparisons:

| Operator | Meaning               |
|----------|-----------------------|
| `-eq`    | Equal                 |
| `-ne`    | Not equal             |
| `-lt`    | Less than             |
| `-le`    | Less than or equal    |
| `-gt`    | Greater than          |
| `-ge`    | Greater than or equal |

The `(( ))` command is preferred for readability and is POSIX-compliant in most modern shells:

``` bash
# Using (( )) — preferred
if (( exit_code != 0 )); then
    echo "Command failed with exit code $exit_code"
fi

if (( count > 100 )); then
    echo "Count exceeds threshold"
fi

# Using [ ] with -lt, -gt, etc. — still valid
if [ "$count" -ge 50 ]; then
    echo "At least 50 items"
fi
```

## File Tests

File tests check existence, type, and permissions:

| Test                   | True if                                    |
|------------------------|--------------------------------------------|
| `-e FILE`              | File exists                                |
| `-f FILE`              | File exists and is a regular file          |
| `-d FILE`              | File exists and is a directory             |
| `-L FILE` or `-h FILE` | File is a symbolic link                    |
| `-b FILE`              | File is a block device                     |
| `-c FILE`              | File is a character device                 |
| `-p FILE`              | File is a named pipe (FIFO)                |
| `-S FILE`              | File is a socket                           |
| `-r FILE`              | File is readable by current user           |
| `-w FILE`              | File is writable by current user           |
| `-x FILE`              | File is executable by current user         |
| `-s FILE`              | File exists and has size greater than zero |
| `-u FILE`              | File has the set-user-ID bit set           |
| `-g FILE`              | File has the set-group-ID bit set          |
| `-k FILE`              | File has the sticky bit set                |
| `-O FILE`              | File is owned by the effective user ID     |
| `-G FILE`              | File is owned by the effective group ID    |
| `-t FD`                | File descriptor FD is open on a terminal   |

``` bash
# Check if file exists and is readable
if [[ -f "$config_file" && -r "$config_file" ]]; then
    source "$config_file"
fi

# Create directory if it doesn't exist
if [[ -d "$backup_dir" ]]; then
    echo "Backup directory exists"
else
    mkdir -p "$backup_dir"
fi

# Check if file is executable
if [[ -x "$script" ]]; then
    ./"$script"
fi

# Check if stdout is connected to a terminal
if [[ -t 1 ]]; then
    echo "Output is going to a terminal"
fi
```

## File Comparisons

Compare files by modification time or inode:

| Operator | Meaning                                          |
|----------|--------------------------------------------------|
| `-nt`    | FILE1 is newer than FILE2 (by modification time) |
| `-ot`    | FILE1 is older than FILE2 (by modification time) |
| `-ef`    | FILE1 and FILE2 refer to the same inode          |

``` bash
# Update backup only if source is newer
if [[ "$source_file" -nt "$backup_file" ]]; then
    cp "$source_file" "$backup_file"
fi

# Check if two paths point to the same file
if [[ "$file1" -ef "$file2" ]]; then
    echo "Both paths reference the same file"
fi

# Find recently modified files
for file in *.log; do
    if [[ "$file" -nt "$LAST_CHECK" ]]; then
        echo "Modified: $file"
    fi
done
```

## Logical Operators

Combine expressions with logical operators:

| Operator | Meaning                                           |
|----------|---------------------------------------------------|
| `!`      | Logical NOT (negate the expression)               |
| `&&`     | Logical AND (both true)                           |
| `\|\|`   | Logical OR (either true)                          |
| `(` `)`  | Grouping (escape in `[ ]`, not needed in `[[ ]]`) |

Use `&&` and `||` instead of the older `-a` and `-o` operators:

``` bash
# Check file exists and is readable
if [[ -f "$file" && -r "$file" ]]; then
    cat "$file"
fi

# Check directory or symlink
if [[ -d "$dir" || -L "$dir" ]]; then
    cd "$dir"
fi

# Verify command is installed
if ! command -v git &>/dev/null; then
    echo "Git not installed"
    exit 1
fi

# Complex conditions with grouping
if [[ (-f "$file1" || -f "$file2") && -w "$output_dir" ]]; then
    process_input
fi
```

## Best Practices

**Prefer `[[ ]]` over `[ ]`:** The `[[ ]]` compound command is safer with unquoted variables, supports pattern matching, and handles special characters correctly. It’s bash-specific but standard in modern scripts:

``` bash
# Safe: works even if $var contains spaces or special characters
if [[ $var == "value" ]]; then
    :
fi

# Works but requires quoting to be safe
if [ "$var" = "value" ]; then
    :
fi
```

**Always quote variables:** Quote variables unless you explicitly need word splitting or glob expansion:

``` bash
# Correct
if [[ -f "$filename" ]]; then
    :
fi

# Dangerous if $filename contains spaces
if [ -f $filename ]; then
    :
fi
```

**Use `(( ))` for arithmetic:** For integer comparisons, the `(( ))` arithmetic command is cleaner and more readable than `-eq`, `-lt`, and similar:

``` bash
# Preferred
if (( count > 10 )); then
    echo "Count is greater than 10"
fi

# Still valid but less readable
if [ "$count" -gt 10 ]; then
    echo "Count is greater than 10"
fi
```

**Avoid `-a` and `-o`:** Use `&&` and `||` with `[[ ]]` instead:

``` bash
# Avoid
if [ -f "$file" -a -r "$file" ]; then
    :
fi

# Prefer
if [[ -f $file && -r $file ]]; then
    :
fi
```

**Understand link dereferencing:** File tests dereference symbolic links by default (follow the link to its target). Use `-L` or `-h` to test the link itself:

``` bash
# Test the target of the symlink
if [[ -f "$path" ]]; then
    echo "$path is a regular file (or points to one)"
fi

# Test the symlink itself
if [[ -L "$path" ]]; then
    echo "$path is a symbolic link"
fi
```

For complete documentation, consult `man test` or `help test` in your shell.
