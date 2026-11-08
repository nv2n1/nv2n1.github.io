---
title: "ASCII Table, Character Codes, and Linux Text Tools"
date: 2013-07-15 10:05:25 +0000
modified: 2026-04-11 17:16:20 +0000
author: "Eric Ma"
layout: post
categories: [databases-storage]
canonical: /ascii-table-and-ascii-code/
---

ASCII stands for American Standard Code for Information Interchange. It’s a 7-bit character encoding standard mapping numeric values (0-127) to printable characters and control codes. Since computers work with numbers at the lowest level, ASCII provides a universal way to represent text—each character has a unique numeric value.

Standardized in 1963, ASCII remains foundational to modern computing. Most character-encoding schemes today (UTF-8, UTF-16, ISO-8859-1) maintain backward compatibility with ASCII for the 0-127 range, meaning the first 128 characters are identical across these encodings.

## ASCII Ranges

The 128 ASCII codes divide into three categories:

- **Control codes (0-31)**: Non-printing characters originally designed for device control, text formatting, and transmission protocols. Most original purposes are obsolete, but several remain essential: LF (line feed), CR (carriage return), TAB, and ESC (escape sequences).
- **Printable characters (32-126)**: Space, punctuation, digits 0-9, uppercase letters A-Z, lowercase letters a-z, and symbols.
- **DEL (127)**: The delete character, technically classified as a control code.

## Converting Characters and ASCII Codes

### Using printf

Convert a character to its ASCII code:

``` bash
printf '%d\n' "'A"
# Output: 65
```

Convert an ASCII code to a character:

``` bash
printf '\x41\n'
# Output: A
```

Or using octal:

``` bash
printf "\\$(printf '%03o' 65)\n"
# Output: A
```

Multiple conversions at once:

``` bash
printf 'Char: A\n'
printf '  Decimal: %d\n' "'A"
printf '  Hex: %x\n' "'A"
printf '  Octal: %o\n' "'A"
# Output:
# Char: A
#   Decimal: 65
#   Hex: 41
#   Octal: 101
```

### Using od (octal dump)

Inspect ASCII values in a file or string:

``` bash
echo "Hello" | od -An -td1
#  72  101  108  108  111
```

Display in hexadecimal:

``` bash
echo "Hello" | od -An -tx1
#  48  65  6c  6c  6f
```

Display with character names:

``` bash
echo "test" | od -c
# 0000000 t e s t \n
```

### Using xxd for hex dumps

``` bash
echo "test" | xxd
# 00000000: 7465 7374 0a                             test.
```

The `0a` at the end is the newline character (LF, decimal 10).

### Using Python

Convert individual characters:

``` python
ord('A')        # Returns: 65
chr(65)         # Returns: 'A'
```

Process entire strings:

``` python
[ord(c) for c in "Hello"]  # Returns: [72, 101, 108, 108, 111]
{ord(c): c for c in "ASCII"}  # Returns: {65: 'A', 83: 'S', 67: 'C', 73: 'I'}
```

### Using Bash parameter expansion

Extract the ASCII value of the first character:

``` bash
var="Hello"
printf '%d\n' "'${var:0:1}"
# Output: 72
```

## Key Control Characters

Most control codes are obsolete for their original purposes, but a few remain relevant in system administration and text processing:

| Code | Decimal | Hex  | Name            | Purpose                                 |
|------|---------|------|-----------------|-----------------------------------------|
| NUL  | 0       | 0x00 | Null            | String terminator in C                  |
| BEL  | 7       | 0x07 | Bell            | Alert signal (rarely used)              |
| BS   | 8       | 0x08 | Backspace       | Cursor control                          |
| TAB  | 9       | 0x09 | Horizontal Tab  | Text formatting, field separation       |
| LF   | 10      | 0x0A | Line Feed       | Newline (Unix/Linux)                    |
| CR   | 13      | 0x0D | Carriage Return | Legacy newline (Windows/old Mac)        |
| ESC  | 27      | 0x1B | Escape          | ANSI escape sequences, terminal control |
| DEL  | 127     | 0x7F | Delete          | Erase character                         |

## Complete ASCII Table (0-127)

| Dec | Oct | Hex  | Char | Dec | Oct | Hex  | Char | Dec | Oct | Hex  | Char | Dec | Oct | Hex  | Char |
|-----|-----|------|------|-----|-----|------|------|-----|-----|------|------|-----|-----|------|------|
| 0   | 000 | 0x00 | NUL  | 32  | 040 | 0x20 | SP   | 64  | 100 | 0x40 | @    | 96  | 140 | 0x60 | \`   |
| 1   | 001 | 0x01 | SOH  | 33  | 041 | 0x21 | !    | 65  | 101 | 0x41 | A    | 97  | 141 | 0x61 | a    |
| 2   | 002 | 0x02 | STX  | 34  | 042 | 0x22 | “    | 66  | 102 | 0x42 | B    | 98  | 142 | 0x62 | b    |
| 3   | 003 | 0x03 | ETX  | 35  | 043 | 0x23 | \#   | 67  | 103 | 0x43 | C    | 99  | 143 | 0x63 | c    |
| 4   | 004 | 0x04 | EOT  | 36  | 044 | 0x24 | \$   | 68  | 104 | 0x44 | D    | 100 | 144 | 0x64 | d    |
| 5   | 005 | 0x05 | ENQ  | 37  | 045 | 0x25 | %    | 69  | 105 | 0x45 | E    | 101 | 145 | 0x65 | e    |
| 6   | 006 | 0x06 | ACK  | 38  | 046 | 0x26 | &    | 70  | 106 | 0x46 | F    | 102 | 146 | 0x66 | f    |
| 7   | 007 | 0x07 | BEL  | 39  | 047 | 0x27 | ‘    | 71  | 107 | 0x47 | G    | 103 | 147 | 0x67 | g    |
| 8   | 010 | 0x08 | BS   | 40  | 050 | 0x28 | (    | 72  | 110 | 0x48 | H    | 104 | 150 | 0x68 | h    |
| 9   | 011 | 0x09 | TAB  | 41  | 051 | 0x29 | )    | 73  | 111 | 0x49 | I    | 105 | 151 | 0x69 | i    |
| 10  | 012 | 0x0A | LF   | 42  | 052 | 0x2A | \*   | 74  | 112 | 0x4A | J    | 106 | 152 | 0x6A | j    |
| 11  | 013 | 0x0B | VT   | 43  | 053 | 0x2B | \+   | 75  | 113 | 0x4B | K    | 107 | 153 | 0x6B | k    |
| 12  | 014 | 0x0C | FF   | 44  | 054 | 0x2C | ,    | 76  | 114 | 0x4C | L    | 108 | 154 | 0x6C | l    |
| 13  | 015 | 0x0D | CR   | 45  | 055 | 0x2D | –    | 77  | 115 | 0x4D | M    | 109 | 155 | 0x6D | m    |
| 14  | 016 | 0x0E | SO   | 46  | 056 | 0x2E | .    | 78  | 116 | 0x4E | N    | 110 | 156 | 0x6E | n    |
| 15  | 017 | 0x0F | SI   | 47  | 057 | 0x2F | /    | 79  | 117 | 0x4F | O    | 111 | 157 | 0x6F | o    |
| 16  | 020 | 0x10 | DLE  | 48  | 060 | 0x30 | 0    | 80  | 120 | 0x50 | P    | 112 | 160 | 0x70 | p    |
| 17  | 021 | 0x11 | DC1  | 49  | 061 | 0x31 | 1    | 81  | 121 | 0x51 | Q    | 113 | 161 | 0x71 | q    |
| 18  | 022 | 0x12 | DC2  | 50  | 062 | 0x32 | 2    | 82  | 122 | 0x52 | R    | 114 | 162 | 0x72 | r    |
| 19  | 023 | 0x13 | DC3  | 51  | 063 | 0x33 | 3    | 83  | 123 | 0x53 | S    | 115 | 163 | 0x73 | s    |
| 20  | 024 | 0x14 | DC4  | 52  | 064 | 0x34 | 4    | 84  | 124 | 0x54 | T    | 116 | 164 | 0x74 | t    |
| 21  | 025 | 0x15 | NAK  | 53  | 065 | 0x35 | 5    | 85  | 125 | 0x55 | U    | 117 | 165 | 0x75 | u    |
| 22  | 026 | 0x16 | SYN  | 54  | 066 | 0x36 | 6    | 86  | 126 | 0x56 | V    | 118 | 166 | 0x76 | v    |
| 23  | 027 | 0x17 | ETB  | 55  | 067 | 0x37 | 7    | 87  | 127 | 0x57 | W    | 119 | 167 | 0x77 | w    |
| 24  | 030 | 0x18 | CAN  | 56  | 070 | 0x38 | 8    | 88  | 130 | 0x58 | X    | 120 | 170 | 0x78 | x    |
| 25  | 031 | 0x19 | EM   | 57  | 071 | 0x39 | 9    | 89  | 131 | 0x59 | Y    | 121 | 171 | 0x79 | y    |
| 26  | 032 | 0x1A | SUB  | 58  | 072 | 0x3A | :    | 90  | 132 | 0x5A | Z    | 122 | 172 | 0x7A | z    |
| 27  | 033 | 0x1B | ESC  | 59  | 073 | 0x3B | ;    | 91  | 133 | 0x5B | \[   | 123 | 173 | 0x7B | {    |
| 28  | 034 | 0x1C | FS   | 60  | 074 | 0x3C | \<   | 92  | 134 | 0x5C | \\   | 124 | 174 | 0x7C | \|   |
| 29  | 035 | 0x1D | GS   | 61  | 075 | 0x3D | =    | 93  | 135 | 0x5D | \]   | 125 | 175 | 0x7D | }    |
| 30  | 036 | 0x1E | RS   | 62  | 076 | 0x3E | \>   | 94  | 136 | 0x5E | ^    | 126 | 176 | 0x7E | ~    |
| 31  | 037 | 0x1F | US   | 63  | 077 | 0x3F | ?    | 95  | 137 | 0x5F | \_   | 127 | 177 | 0x7F | DEL  |

## Practical Use Cases

### Finding Non-ASCII or Control Characters

Identify lines containing bytes outside the standard ASCII range:

``` bash
grep -P -n "[\x80-\xFF]" filename
```

View control characters in context:

``` bash
od -c filename | head -20
```

Check for embedded null bytes (often problematic in text files):

``` bash
grep -c $'\x00' filename
```

### Byte-Level File Analysis

Examine raw bytes with ASCII equivalents side-by-side:

``` bash
xxd -g 1 filename | head -20
```

This format shows hex values and printable ASCII characters, making it straightforward to spot text embedded in binary data.

Add the `-l` flag to limit output by byte count:

``` bash
xxd -g 1 -l 512 filename
```

### Extracting Text from Binary Files

Extract all printable ASCII strings from a binary file:

``` bash
strings filename
```

Filter by minimum string length:

``` bash
strings -n 8 filename    # Only strings 8+ characters long
```

Combine with grep to find specific patterns:

``` bash
strings binary_file | grep -i "version"
```

### Text Processing and Line Endings

Check file line ending types:

``` bash
file filename  # Shows line ending type (CRLF, LF, etc.)
```

Find lines with non-standard line endings (mixed LF/CR):

``` bash
od -c filename | grep -E "(\\\\n|\\\\r)"
```

Convert DOS line endings (CR+LF) to Unix (LF):

``` bash
dos2unix filename
```

Or using sed (works on systems without `dos2unix`):

``` bash
sed -i 's/\r$//' filename
```

Convert Unix to DOS line endings:

``` bash
sed -i 's/$/\r/' filename
```

### Log Analysis

Check for control characters that might corrupt log parsing:

``` bash
cat logfile | od -c | grep -E '\\[0-7][0-7][0-7]'
```

Display any character outside printable ASCII in escape notation:

``` bash
cat logfile | sed 's/[^[:print:]\n]/./g'
```

Generate a summary of non-ASCII characters found:

``` bash
od -An -tx1 logfile | tr -s ' ' '\n' | sort | uniq -c | grep -v '^[[:space:]]*[0-9]\+ 2[0-7]' | grep -v '^[[:space:]]*[0-9]\+ [0-4][0-9a-f]'
```

### Working with Special Characters in Scripts

Safely handle strings containing ASCII codes:

``` bash
# Store a tab character
tab=$'\t'
# Store a newline
newline=$'\n'
# Use in commands
awk -v tab="$tab" '{print $1 tab $2}' input.txt
```

Generate test data with specific ASCII codes:

``` bash

# Create a file with null-terminated strings
printf 'string1\x00string
```
