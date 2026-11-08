---
title: "Converting JPG to EPS on Linux with ImageMagick and Ghostscript"
date: 2013-07-12 16:46:15 +0000
layout: post
canonical: https://www.systutorials.com/an-online-jpg-to-eps-converter/
---

Converting raster images to EPS format is necessary when working with LaTeX documents or professional publishing workflows that require PostScript compatibility. While online converters exist, command-line tools give you reproducibility, automation, and batch processing capabilities—essential for production work.

## Why EPS Still Matters

EPS (Encapsulated PostScript) embeds images with precise positioning metadata and works reliably with LaTeX, traditional publishing systems, and print workflows. Modern alternatives like PDF are better for screen viewing, but many academic publishers and print vendors still require EPS submissions. It’s also the only format some legacy publishing pipelines accept without conversion.

## Quick Conversion with ImageMagick

The standard approach on Linux uses ImageMagick’s `convert` command:

``` bash
convert input.jpg output.eps
```

This works with any raster format:

``` bash
convert input.png output.eps
convert input.gif output.eps
convert input.bmp output.eps
```

Control output quality and resolution with flags:

``` bash
convert input.jpg -quality 90 output.eps
convert input.jpg -density 300 output.eps
```

The `-density` flag sets DPI resolution, critical for print-quality output. Use 300 DPI for professional printing, 72 DPI for screen-only use.

## Batch Converting Multiple Files

Process all JPGs in a directory:

``` bash
for file in *.jpg; do
  convert "$file" "${file%.jpg}.eps"
done
```

For subdirectories, use `find`:

``` bash
find . -name "*.jpg" -type f | while read file; do
  convert "$file" "${file%.jpg}.eps"
done
```

Parallelize batch jobs with GNU Parallel for speed:

``` bash
find . -name "*.jpg" -type f | parallel convert {} {.}.eps
```

This processes multiple files simultaneously on multi-core systems.

## Ghostscript for High-Quality Conversions

When ImageMagick produces suboptimal results—particularly with images containing text or complex color profiles—Ghostscript delivers better output:

``` bash
gs -q -dNOPAUSE -dBATCH -sDEVICE=eps2write -sOutputFile=output.eps input.jpg
```

Ghostscript handles transparency, color spaces, and anti-aliasing more accurately for technical documents. Use this if your LaTeX rendering looks fuzzy or colors appear wrong.

For batch processing with Ghostscript:

``` bash
for file in *.jpg; do
  gs -q -dNOPAUSE -dBATCH -sDEVICE=eps2write -sOutputFile="${file%.jpg}.eps" "$file"
done
```

## GraphicsMagick for Speed

GraphicsMagick (gm) is a faster fork of ImageMagick with identical syntax:

``` bash
gm convert input.jpg output.eps
```

Use this for large batch conversions—it’s noticeably faster on I/O-heavy operations without sacrificing quality.

## Installation

Debian/Ubuntu:

``` bash
sudo apt install imagemagick ghostscript graphicsmagick
```

RHEL/CentOS/Fedora:

``` bash
sudo dnf install ImageMagick ghostscript GraphicsMagick
```

## Verifying Conversion Success

Check the output file type:

``` bash
file output.eps
```

Should return: `output.eps: PostScript document text`

Test in LaTeX:

``` latex
\documentclass{article}
\usepackage{graphicx}
\begin{document}
\includegraphics{output.eps}
\end{document}
```

Compile with:

``` bash
latex document.tex
dvipdf document.dvi
```

Or directly with pdflatex (which handles EPS through automatic conversion):

``` bash
pdflatex document.tex
```

## When to Use Each Tool

**ImageMagick**: Default choice for most conversions. Fast, reliable, widely available. Use for straightforward image conversion in automation scripts.

**Ghostscript**: Use when ImageMagick output looks wrong—text appears fuzzy, colors shift, or transparency breaks. Better color space handling for technical documents.

**GraphicsMagick**: Use for batch processing large image sets. Identical output quality to ImageMagick but faster execution on multi-file operations.

**Online converters**: Only for one-off conversions when you lack Linux access. Results depend on their backend (usually ImageMagick), so local tools give you more control.

## Common Gotchas

- **Embedding fonts**: EPS doesn’t embed fonts by default. If text in images must be preserved, ensure fonts are installed on the system where EPS will be rendered.
- **Transparency**: EPS doesn’t handle transparency the same way raster formats do. Ghostscript converts transparency to white background; set a background color explicitly with ImageMagick: `convert input.png -background white output.eps`
- **Color profiles**: CMYK JPGs may shift colors. Use `-colorspace RGB` before conversion if targeting sRGB outputs: `convert input.jpg -colorspace RGB output.eps`
- **Large files**: EPS files are uncompressed PostScript by default, resulting in much larger files than the source JPG. For LaTeX, consider using PDF instead unless EPS is explicitly required.

Command-line tools offer reproducibility and automation that online converters can’t match. Keep ImageMagick and Ghostscript installed for production workflows.
