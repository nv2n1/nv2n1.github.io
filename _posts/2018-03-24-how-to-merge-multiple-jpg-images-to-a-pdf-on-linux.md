---
title: "Merge JPG Images into PDF on Linux"
date: 2018-03-24 11:43:56 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-merge-multiple-jpg-images-to-a-pdf-on-linux/
---

Converting a series of JPG images into a single PDF is useful for creating documents, presentations, or archiving scanned photos. Linux offers several tools for this task, each with different trade-offs between simplicity, quality preservation, and features.

## Using img2pdf (Recommended)

For most cases, `img2pdf` is the best choice because it merges images without re-encoding or re-compressing them, preserving original quality:

``` bash
img2pdf *.jpg -o output.pdf
```

To control the order of images, specify them explicitly:

``` bash
img2pdf image1.jpg image2.jpg image3.jpg -o output.pdf
```

You can also set page size and margins:

``` bash
img2pdf *.jpg -o output.pdf --imgsize 210x297mm --margin 10
```

The `--imgsize` flag accepts common sizes like `A4`, `letter`, or custom dimensions. If your images are already the right size, you can fit them to the page:

``` bash
img2pdf *.jpg -o output.pdf --fit shrink
```

Install img2pdf on Debian/Ubuntu:

``` bash
sudo apt install img2pdf
```

On RHEL/CentOS/Fedora:

``` bash
sudo dnf install img2pdf
```

## Using ImageMagick

ImageMagick’s `convert` command works but re-compresses images, reducing quality:

``` bash
convert *.jpg output.pdf
```

This approach is slower and larger in file size compared to img2pdf. However, ImageMagick is useful if you need to manipulate images during conversion (resize, rotate, adjust colors):

``` bash
convert *.jpg -resize 50% -quality 85 output.pdf
```

## Using Ghostscript

For more control over PDF compression and settings, use Ghostscript:

``` bash
convert *.jpg output.pdf && gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 \
  -dPDFSETTINGS=/ebook -o compressed.pdf output.pdf
```

## Using PDFtk (for manipulation after creation)

If you need to merge PDFs that you’ve already created, or reorder pages:

``` bash
pdftk page1.pdf page2.pdf output merged.pdf
```

## Handling Specific Formats

For mixed image formats (JPG, PNG, TIFF):

``` bash
img2pdf *.jpg *.png -o output.pdf
```

For images with rotation metadata:

``` bash
img2pdf --auto-orient *.jpg -o output.pdf
```

## Processing Large Image Sets

For directories with many images, sort them numerically:

``` bash
img2pdf $(ls -v *.jpg) -o output.pdf
```

Or use find with numerical sorting:

``` bash
find . -maxdepth 1 -name "*.jpg" -print0 | sort -z -V | xargs -0 img2pdf -o output.pdf
```

## Adding OCR (Optional)

To make PDFs searchable, use OCRmyPDF after creation:

``` bash
img2pdf *.jpg -o output.pdf
ocrmypdf output.pdf output-ocr.pdf
```

This requires `ocrmypdf` and Tesseract. Install on Debian/Ubuntu:

``` bash
sudo apt install ocrmypdf tesseract-ocr
```

## Performance Considerations

- **img2pdf**: Fastest, lossless, smallest output file
- **ImageMagick**: Slower, lossy compression, useful for pre-processing
- **Ghostscript**: Good for compression control after creation

For archival or quality-critical work, always use `img2pdf`. Reserve ImageMagick and Ghostscript for cases where you need image manipulation or aggressive compression.

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
