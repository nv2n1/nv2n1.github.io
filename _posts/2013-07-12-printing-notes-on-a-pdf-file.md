---
title: "Printing PDF Annotations in Acrobat, Adobe Reader, and Foxit"
date: 2013-07-12 16:54:50 +0000
layout: post
canonical: https://www.systutorials.com/printing-notes-on-a-pdf-file/
---

Printing PDF annotations with fidelity across different readers requires understanding each tool’s specific workflow. The fundamentals haven’t changed much, but modern versions offer more reliable options than they did years ago.

## Adobe Acrobat (Full Version)

Acrobat provides the most control over annotation printing, but requires explicit configuration before print.

**Enable annotation printing in preferences:**

1.  Open Edit → Preferences → Commenting
2.  Configure these settings:
    - Font: Choose a sans-serif font like Segoe UI or Liberation Sans for clean print output
    - Print Notes and Comments: Enable this checkbox
    - Pop-up Opacity: Set to 100% for solid visibility when printing
    - Pop-up Scrolling: Disable to prevent unwanted text wrapping during output

**Adjust note positioning correctly:**

Acrobat doesn’t guarantee screen-to-print accuracy across zoom levels. View your document at 75% zoom while positioning annotations for the most predictable printed output. Individual sticky notes may require manual adjustment since different zoom levels and page scaling affect final placement.

**Print with markups enabled:**

Go to File → Print and ensure the print dialog shows “Document and Markups” selected. Selecting “Document only” will skip all annotations entirely.

## Adobe Reader (Free Version)

Adobe Reader DC and later support comment printing through the summarization workflow:

1.  Add all comments and notes to the PDF
2.  Open File → Print
3.  Locate the “Summarize Comments” option in the print dialog
4.  Complete the print job

This generates a summary page containing all comments that prints after the document. Individual note positioning isn’t preserved, but this method works reliably across systems for review workflows.

## Foxit Reader

Foxit Reader (available free on Linux, Windows, and macOS) handles comment printing similarly:

1.  Add annotations using Foxit’s comment tools
2.  Open File → Print
3.  Click “Summarize Comments”
4.  Complete the print job

Foxit’s lightweight footprint makes it a practical choice on Linux systems where full Acrobat isn’t available, though its summarization output works the same way as Adobe Reader.

## Flattening Annotations for Reliable Printing

For absolute certainty that annotations print correctly regardless of reader, flatten them into the PDF before printing. This converts all comments to static content that can’t be lost in translation between applications.

**Using pdftk:**

``` bash
pdftk input.pdf output flattened.pdf
```

**Using qpdf (more reliable on modern systems):**

``` bash
qpdf --replace-input --flatten-annotations=all input.pdf
```

The `--flatten-annotations=all` option in qpdf is more robust than pdftk for complex documents with overlapping annotations.

**Using Ghostscript for format conversion before flattening:**

``` bash
gs -sDEVICE=pdfwrite -dFIXEDMEDIA -dPDFFitPage \
   -sOutputFile=processed.pdf input.pdf
```

## Batch Processing Annotations

If you regularly print annotated PDFs, consider automating the flattening step:

``` bash
#!/bin/bash
for pdf in *.pdf; do
    qpdf --replace-input --flatten-annotations=all "$pdf"
    lp "$pdf"  # or use your preferred print command
done
```

This flattens all PDFs in the current directory and sends them to the default printer.

## Best Practices

- **Test print to file first** (PDF or PostScript format) before sending to a physical printer
- **Use consistent fonts** across all annotations for uniform output
- **Flatten annotations** if notes fail to print with reader-specific settings
- **Export comment summaries separately** for shared documents rather than relying on reader-specific features
- **Verify flattening** by opening the output file in a different PDF reader to confirm annotations are now part of the document layer
- **Use pdfdiff or similar tools** to compare annotated and flattened versions when dealing with sensitive documents

The Summarize Comments feature provides the most portable cross-reader approach, though it doesn’t preserve on-screen positioning of individual notes. For mission-critical documents where visual consistency matters, flattening eliminates reader dependency entirely and ensures annotations always print exactly as intended.
