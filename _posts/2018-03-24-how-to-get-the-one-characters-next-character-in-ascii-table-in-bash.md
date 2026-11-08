---
title: "Getting the Next ASCII Character in Bash"
date: 2018-03-24 11:52:40 +0000
modified: 2026-04-11 15:48:19 +0000
author: "David Yang"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-get-the-one-characters-next-character-in-ascii-table-in-bash/
---

Sometimes you need to find the ASCII character that comes after a given character. This is useful for generating sequences, creating substitution ciphers, or manipulating character ranges in shell scripts.

## Using `printf` with ASCII Values

The most portable and straightforward approach uses `printf` to convert between characters and their ASCII numeric values:

``` bash
#!/bin/bash

get_next_char() {
    local char="$1"
    local ascii

    # Get ASCII value of the character
    ascii=$(printf '%d' "'$char")

    # Increment and convert back to character
    printf "\\$(printf '%03o' $((ascii + 1)))"
}

# Example usage
echo "Next char after 'A' is: $(get_next_char 'A')"
echo "Next char after 'z' is: $(get_next_char 'z')"
echo "Next char after '9' is: $(get_next_char '9')"
```

The `printf '%d' "'$char"` syntax extracts the ASCII value by treating the character as a string literal. The single quote before the character forces `printf` to interpret it as an ASCII value.

## Handling Edge Cases

When working near the boundaries of the ASCII table, you may want to validate or handle wraparound:

``` bash
#!/bin/bash

get_next_char_safe() {
    local char="$1"
    local ascii

    ascii=$(printf '%d' "'$char")

    # Check if we're at ASCII 127 (DEL character)
    if [[ $ascii -ge 127 ]]; then
        echo "Warning: Character at ASCII boundary" >&2
        return 1
    fi

    printf "\\$(printf '%03o' $((ascii + 1)))"
}

# Generate a character range
generate_range() {
    local start="$1"
    local end="$2"
    local current="$start"
    local current_ascii end_ascii

    current_ascii=$(printf '%d' "'$current")
    end_ascii=$(printf '%d' "'$end")

    while [[ $current_ascii -le $end_ascii ]]; do
        printf "\\$(printf '%03o' $current_ascii)"
        ((current_ascii++))
    done
}

# Generate a-z
echo "Lowercase letters:"
generate_range 'a' 'z'
echo ""
```

## Using `od` for Inspection

To verify ASCII values and see the relationship between characters:

``` bash
# See ASCII value of a character
echo -n 'A' | od -An -td1

# See multiple characters
echo -n 'ABC' | od -An -td1
```

## Practical Example: ROT13-style Cipher

Here’s a real-world use case that rotates characters within their range:

``` bash
#!/bin/bash

rotate_char() {
    local char="$1"
    local shift="${2:-1}"
    local ascii new_ascii

    ascii=$(printf '%d' "'$char")
    new_ascii=$((ascii + shift))

    # For lowercase letters, wrap around
    if [[ $ascii -ge 97 && $ascii -le 122 ]]; then
        new_ascii=$(( (ascii - 97 + shift) % 26 + 97 ))
    # For uppercase letters, wrap around
    elif [[ $ascii -ge 65 && $ascii -le 90 ]]; then
        new_ascii=$(( (ascii - 65 + shift) % 26 + 65 ))
    fi

    printf "\\$(printf '%03o' $new_ascii)"
}

# Test
echo "$(rotate_char 'a' 1)$(rotate_char 'b' 1)$(rotate_char 'c' 1)"  # bcd
echo "$(rotate_char 'z' 1)$(rotate_char 'Z' 1)"  # aA (wraps around)
```

## Performance Considerations

For processing large strings character-by-character, the `printf` approach works but can be slow. Use tools like `tr` when possible:

``` bash
# Simple character substitution (much faster for bulk operations)
echo "Hello" | tr 'a-z' 'b-za'

# Or with sed for more complex transformations
echo "Hello" | sed 's/./\\x27/g'  # Replace with single quotes
```

## Compatibility

The `printf` method works reliably across Bash 3.0+, making it suitable for scripts that need to run on older systems. The `$(...)` command substitution syntax is POSIX-compliant. If you need maximum portability, avoid `[[` conditionals and use `[ ]` instead, though `[[` is standard in Bash.
