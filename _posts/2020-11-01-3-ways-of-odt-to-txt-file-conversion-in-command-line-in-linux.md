---
title: "Converting ODT Files to TXT in Linux: 3 Command-Line Methods"
date: 2020-11-01 07:35:51 +0000
author: "David Yang"
layout: post
categories: [linux-systems-administration]
canonical: /3-ways-of-odt-to-txt-file-conversion-in-command-line-in-linux/
---

ODT files often contain formatting that you don’t need. Whether you’re archiving content, preparing text for further processing, or just need readability without markup, converting to plain text is straightforward. Here are the practical approaches and their tradeoffs.

## LibreOffice Conversion

LibreOffice’s `--convert-to` flag handles ODT natively:

``` bash
libreoffice --headless --convert-to txt input.odt
```

The `--headless` flag prevents the GUI from launching, essential for scripting or remote systems.

**Output characteristics:**

- Preserves all text content and spacing exactly as stored
- Strips all formatting (bold, italic, headings become plain text)
- Maintains code blocks with original indentation
- Fast and reliable for large batches

**Example output:**

    This is an example docx file.

    This is a title

    This is a heading level 1

    This is some text with format: bold, italic and underline.

    Also some code below.

    int main() {
      std::cout << "Hello World!\n";
      return 0;
    }

For batch conversion:

``` bash
for file in *.odt; do
  libreoffice --headless --convert-to txt "$file"
done
```

## Pandoc Plain Text Output

Pandoc converts ODT to plain text while attempting to preserve some formatting indicators:

``` bash
pandoc -t plain input.odt -o input.txt
```

**Output characteristics:**

- Uses uppercase for emphasized text (BOLD, ITALIC)
- Underscores for italics: `_italic_`
- May collapse whitespace in code blocks
- Good for human-readable text with minimal markup

**Example output:**

    This is an example docx file.

    This is a title

    THIS IS A HEADING LEVEL 1

    This is some text with format: BOLD, _italic_ and _underline_.

    Also some code below.

    int main() {
    std::cout << "Hello World!\n";
    return 0;
    }

## Pandoc to Markdown

For better formatting preservation, output to Markdown instead of plain text:

``` bash
pandoc -t markdown input.odt -o input.md
```

**Output characteristics:**

- Preserves heading structure with Markdown syntax
- Uses `**bold**` and `*italic*` conventions
- Code blocks may need manual cleanup
- Resulting file is still plain text but semantically richer

**Example output:**

``` markdown
This is an example docx file.

This is a title

This is a heading level 1
=========================

This is some text with format: **bold**, *italic* and *underline*.

Also some code below.

int main() {\
std::cout \<\< "Hello World!\\n";\
return 0;\
}
```

The escaped characters and backslashes in code sections often need manual fixes:

``` markdown
int main() {
  std::cout << "Hello World!\n";
  return 0;
}
```

## Batch Conversion Comparison

For processing multiple files, create a wrapper script:

``` bash
#!/bin/bash
# Convert all ODT files to Markdown (preserves more structure)

for file in *.odt; do
  output="${file%.odt}.md"
  pandoc -t markdown "$file" -o "$output"
  echo "Converted $file to $output"
done
```

Or if you need true plaintext without any markup:

``` bash
#!/bin/bash
# Convert to plaintext, strip all formatting

for file in *.odt; do
  output="${file%.odt}.txt"
  libreoffice --headless --convert-to txt --outdir "$(dirname "$file")" "$file"
  mv "${file%.odt}.txt" "$output"
  echo "Converted $file to $output"
done
```

## Choosing the Right Tool

- **LibreOffice**: When you need exact spacing preservation and don’t need any formatting hints. Reliable but loses all markup information.
- **Pandoc plain**: When formatting hints are useful but you want minimal markup. Better for documents with emphasized text.
- **Pandoc Markdown**: When you might convert back to formatted output or need structure preserved. Markdown is readable and editable.

For complex documents with extensive code, combine approaches: extract code blocks from LibreOffice’s output to fix formatting issues, then manually integrate into Pandoc’s Markdown version for the best result.

Both tools handle large ODT files efficiently. Choose based on your workflow—if you’re archiving, Markdown preserves more information. If you’re extracting text for processing, plain text from LibreOffice avoids formatting noise.
