---
title: "Converting PowerPoint Slides to High-DPI TIFF for Print"
date: 2018-03-24 11:49:04 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-change-the-dpi-of-tiff-images-exported-by-powerpoint/
---

PowerPoint’s export function defaults to 96 DPI, which is suitable for screen display but inadequate for printing posters, documents, or any material requiring high resolution. While PowerPoint includes DPI settings, they’re often unreliable or have limited effect on TIFF output. Here are the practical methods to generate proper high-DPI TIFF files from PowerPoint slides.

## PowerPoint’s Built-in Export Settings

PowerPoint does offer a DPI control in the export dialog, but it frequently fails to apply correctly to TIFF output. To access it:

1.  Open your presentation and navigate to **File \> Export \> Change File Type**
2.  Select **TIFF** as the format
3.  Click **Export**, then look for **Options** (availability varies by Office version)
4.  Set your desired DPI (150, 200, 300, etc.)
5.  Export the slides

If this works for you, great. However, many users report the setting has no effect, particularly on Windows. The limitation stems from how PowerPoint handles rasterization internally.

## Reliable Method: Export to PDF, Then Convert

The most consistent approach is exporting to PDF first, then converting to TIFF with proper DPI settings using `ImageMagick` or `Ghostscript`.

**Export PowerPoint to PDF:**

1.  **File \> Export as PDF**
2.  Click **Options** and enable **Optimize for printing** (ensures higher quality)
3.  Save the PDF

**Convert PDF to TIFF with ImageMagick:**

``` bash
convert -density 300 presentation.pdf -compress lzw output.tiff
```

The `-density` parameter controls DPI. Use `300` for print-quality output, `150` for general use.

For multi-slide presentations, ImageMagick creates individual files:

``` bash
convert -density 300 presentation.pdf output-%d.tiff
```

This generates `output-0.tiff`, `output-1.tiff`, etc.

## Using Ghostscript for Better Control

Ghostscript offers more granular control over PDF-to-TIFF conversion and often produces superior results:

``` bash
gs -q -dNOPAUSE -dBATCH -dSAFER \
  -sDEVICE=tiff32nc \
  -r300x300 \
  -sOutputFile=slide-%d.tiff \
  presentation.pdf
```

Replace `300x300` with your desired DPI. The `tiff32nc` device produces 32-bit uncompressed TIFF; alternatives include:

- `tiff24nc` – 24-bit color
- `tiff32nc` – 32-bit with alpha channel
- `tiffg4` – black and white (CCITT Group 4 compression)

## LibreOffice Impress Alternative

If you’re open to using LibreOffice instead of Microsoft Office, Impress provides more reliable export control:

1.  **File \> Export as PDF** (with print optimization enabled)
2.  Convert using the PDF-to-TIFF methods above

Alternatively, LibreOffice Impress can export directly to image formats with DPI specification through command-line:

``` bash
libreoffice --headless --convert-to png --outdir /tmp presentation.odp
# Then convert PNG to TIFF
convert -density 300 slide-*.png -compress lzw output-%d.tiff
```

## Command-Line Batch Processing

For handling multiple presentations, automate the conversion:

``` bash
#!/bin/bash
for pptx in *.pptx; do
  pdf="${pptx%.pptx}.pdf"
  # Convert PPTX to PDF using libreoffice
  libreoffice --headless --convert-to pdf "$pptx"
  # Convert PDF to TIFF at 300 DPI
  convert -density 300 "$pdf" -compress lzw "${pdf%.pdf}-%d.tiff"
done
```

## Verification

Verify your TIFF file’s DPI using `identify` from ImageMagick:

``` bash
identify -verbose output.tiff | grep Resolution
```

Or with `tiffinfo`:

``` bash
tiffinfo output.tiff | grep Resolution
```

## Considerations

- **DPI vs. pixel dimensions**: Higher DPI requires more disk space. A 10″×8″ poster at 300 DPI produces approximately 3000×2400 pixels.
- **Compression**: Use `lzw` compression for lossless results without significant file bloat.
- **Color accuracy**: PDF export with print optimization helps preserve colors more accurately than direct PowerPoint export.
- **Font handling**: Converting through PDF ensures fonts are properly embedded and won’t reflow unpredictably.

For print-ready output, the PDF-to-TIFF conversion pipeline is more reliable than relying on PowerPoint’s inconsistent native export settings.
