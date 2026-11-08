---
title: "Converting PDFs to Text While Preserving Layout on Linux"
date: 2018-03-24 11:48:58 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-convert-pdf-to-text-with-format-kept-on-linux/
---

Many PDF-to-text conversions strip away formatting and spatial relationships, making tables unreadable and multi-column layouts collapse into linear text. If you need to preserve the relative positions of text elements—especially tables, columns, and indentation—you have several solid options.

## pdftotext with layout preservation

The simplest approach is `pdftotext`, which comes with most distributions as part of the Poppler utilities package:

``` bash
pdftotext -layout file.pdf file.txt
```

The `-layout` flag tells pdftotext to maintain the original physical layout as closely as possible, preserving column structure, spacing, and text positioning. Without it, the tool would “undo” the layout and output text in reading order instead.

You can also combine `-layout` with other useful options:

``` bash
# Preserve layout and use a specific encoding
pdftotext -layout -enc UTF-8 file.pdf file.txt

# Extract only a range of pages
pdftotext -layout -f 1 -l 5 file.pdf file.txt

# Extract with physical page breaks preserved
pdftotext -layout -eol dos file.pdf file.txt
```

The `-eol` flag controls line ending style (unix, dos, or mac). For multi-column PDFs, `-layout` generally works well, though the output quality depends on how the PDF was structured internally.

## Alternative: pdftohtml

For more complex documents or when you need better structure preservation, convert to HTML first, then extract text:

``` bash
pdftohtml -c file.pdf file.html
# Then convert HTML to text with a tool like lynx or w3m
lynx -dump -nolist file.html > file.txt
```

This approach captures more semantic structure than direct PDF-to-text conversion.

## Using pandoc for better formatting

Pandoc handles PDF conversion with good layout preservation and can output to multiple formats:

``` bash
# Convert PDF to plain text with layout
pandoc file.pdf -t plain -o file.txt

# Convert to Markdown for better structure preservation
pandoc file.pdf -t markdown -o file.md
```

Pandoc often produces cleaner output for documents with consistent formatting.

## Handling scanned PDFs

If your PDF contains scanned images rather than embedded text, you’ll need OCR:

``` bash
# Install tesseract if not already present
sudo apt install tesseract-ocr

# Extract text with layout preservation
tesseract file.pdf file -l eng pdf
```

This generates both `file.txt` and `file.pdf` (the latter with embedded OCR text).

## Testing and validation

Always verify the output on a sample before batch-processing:

``` bash
# Test on first page only
pdftotext -layout -f 1 -l 1 file.pdf test.txt
cat test.txt
```

Check that tables remain aligned, column spacing is preserved, and multi-column layouts haven’t collapsed. If the output is poor, try the HTML conversion route or pandoc instead.

## Troubleshooting Common Issues

When encountering problems on Linux systems, follow a systematic approach. Check system logs first using journalctl for systemd-based distributions. Verify service status with systemctl before attempting restarts. For network issues, use ip addr and ss -tulpn to diagnose connectivity problems.

Package management issues often stem from stale caches. Run dnf clean all on Fedora or apt clean on Ubuntu before retrying failed installations. If a package has unmet dependencies, try resolving them with dnf autoremove or apt autoremove.

## Related System Commands

These commands are frequently used alongside the tools discussed in this article:

- systemctl status service-name – Check if a service is running
- journalctl -u service-name -f – Follow service logs in real time
- rpm -qi package-name – Query installed package information
- dnf history – View package transaction history
- top or htop – Monitor system resource usage

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
