---
title: "Wrapping Long Lines in Text Files on Linux"
date: 2018-03-24 11:47:40 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-wrap-long-lines-in-a-text-file-on-linux/
---

Long lines in text files can be difficult to read in a terminal. Linux provides several built-in tools to wrap or fold long lines to fit your screen width, each with different strengths.

## Using fold — Simple Line Wrapping

`fold` wraps lines at a specified character width:

```wp-block-code
# Wrap at 80 characters
fold -w 80 longfile.txt

# Wrap at terminal width automatically
fold -w $(tput cols) longfile.txt

# Wrap at 80 characters, breaking at word boundaries
fold -s -w 80 longfile.txt
```

The `-s` flag is important: it breaks at whitespace when possible, preventing words from being split in the middle. Without `-s`, `fold` breaks at exactly the character limit.

## Using fmt — Smart Paragraph Reflow

`fmt` is more intelligent than `fold` — it understands paragraph breaks and reflows text naturally:

```wp-block-code
# Reflow text to 80 characters
fmt -w 80 longfile.txt

# Reflow with paragraph preservation (doesn't merge paragraphs)
fmt -p -w 80 longfile.txt

# Only reflow lines longer than the goal width
fmt -g 80 longfile.txt

# Uniform spacing — collapse multiple spaces to one
fmt -u -w 80 longfile.txt
```

Unlike `fold`, `fmt` joins short lines together into paragraphs and breaks long lines at word boundaries. It’s the better choice for prose and documentation.

## Using less — Interactive Viewing

When you just need to read a file with long lines, `less` offers toggleable wrapping:

```wp-block-code
# Open file with wrapping enabled
less longfile.txt

# Inside less, press these keys:
# -S    Toggle between wrap and chop mode
#       (chop mode: long lines truncated, scroll right with arrows)
#       (wrap mode: long lines wrap to next screen line)
# -S again to toggle back
```

You can also start less in chop mode:

```wp-block-code
less -S longfile.txt
```

## Using pr — Print-Formatted Output

`pr` formats text for printing with headers and page breaks:

```wp-block-code
# Format with 80-char width and page numbers
pr -w 80 -l 60 longfile.txt

# Number lines while wrapping
pr -n -w 80 longfile.txt

# Double-column output
pr -2 -w 80 longfile.txt

# Pipe to printer or PDF
pr -w 80 longfile.txt | lpr
```

## In-Place File Modification

To permanently wrap lines in a file (overwriting the original):

```wp-block-code
# Using fold with backup
fold -s -w 80 longfile.txt > longfile.tmp && mv longfile.tmp longfile.txt

# Using sed to insert newlines at column 80
sed -i 's/.\{80\}/&\n/g' longfile.txt

# Using fmt to reflow paragraphs permanently
fmt -w 80 longfile.txt > longfile.tmp && mv longfile.tmp longfile.txt
```

Always use a temporary file rather than piping back to the same file (`fold file > file` truncates the file to zero bytes).

## Wrapping in Vim and Neovim

Control line display in Vim:

```wp-block-code
" Visual wrapping (doesn't change file content)
:set wrap              " Enable soft wrapping at window edge
:set nowrap            " Disable wrapping, long lines extend right

" Set physical line width (inserts actual line breaks)
:set textwidth=80      " Auto-break at 80 chars while typing
:set formatoptions+=t  " Auto-wrap text using textwidth

" Manual reflow of a paragraph
gqip    " Reflow the current paragraph
gqap    " Reflow current paragraph (including surrounding blank line)
gqG     " Reflow from cursor to end of file
```

Neovim users can use the same commands. For automatic wrapping on save:

```wp-block-code
autocmd BufWritePre *.txt normal gggqG
```

## Wrapping Columns with column

For tabular data with long lines, `column` reformats into aligned columns:

```wp-block-code
# Align CSV-style data by delimiter
column -t -s',' data.csv

# Limit column width
column -t -s'   ' data.tsv | fold -s -w 120
```

## Handling Very Long Lines (Logs, Base64)

For files with extremely long single lines (encoded data, JSON blobs):

```wp-block-code
# View first 200 characters of each line
cut -c1-200 hugelines.txt

# Split base64 into 76-char lines (standard format)
fold -w 76 base64_data.txt

# Pretty-print JSON (requires python)
python3 -m json.tool data.json
```

## Quick Reference

- `fold -s -w 80 file` — Wrap at 80 chars, word-safe
- `fmt -w 80 file` — Reflow paragraphs to 80 chars
- `less -S file` — View with chop/wrap toggle (press -S)
- `pr -w 80 file` — Print-formatted with wrapping
- `:set wrap` in Vim — Soft wrap (visual only)
- `:set textwidth=80` in Vim — Hard wrap (modifies file)
- `gqip` in Vim — Reflow current paragraph
