---
title: "Converting JPG Images to EPS Format"
date: 2013-07-12 16:32:28 +0000
modified: 2026-04-12 16:05:48 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /converting-jpg-images-to-eps/
---

If you’re working with LaTeX documents that need to include JPG or PNG images, converting them to EPS (Encapsulated PostScript) format is a straightforward approach. While modern LaTeX workflows often handle JPG directly, EPS conversion remains useful for compatibility with certain tools, print workflows, or when working with legacy build systems.

## Installation

ImageMagick is the standard tool for this task. Install it using your package manager:

**Debian/Ubuntu:**

``` bash
sudo apt install imagemagick
```

**RHEL/CentOS/Fedora:**

``` bash
sudo dnf install ImageMagick
```

**Alpine:**

``` bash
apk add imagemagick
```

## Basic Conversion

Convert a JPG to EPS with a single command:

``` bash
convert image.jpg image.eps
```

ImageMagick automatically detects the input format and generates the output based on the file extension.

## Practical Examples

**Convert multiple files in a directory:**

``` bash
for file in *.jpg; do
    convert "$file" "${file%.jpg}.eps"
done
```

**Preserve image quality during conversion:**

``` bash
convert -quality 95 image.jpg image.eps
```

**Resize while converting (useful for large images):**

``` bash
convert image.jpg -resize 2048x2048 image.eps
```

**Convert PNG with transparency (EPS doesn’t support alpha channels):**

``` bash
convert image.png -background white -flatten image.eps
```

**Specify DPI for print workflows (important for professional output):**

``` bash
convert -density 300 image.jpg -units PixelsPerInch image.eps
```

## LaTeX Integration

Once converted, include the EPS file in your LaTeX document:

``` latex
\documentclass{article}
\usepackage{graphicx}

\begin{document}

\begin{figure}[h]
    \centering
    \includegraphics[width=0.8\textwidth]{image.eps}
    \caption{My converted image}
\end{figure}

\end{document}
```

Compile with:

``` bash
pdflatex document.tex
```

Or use `dvips` if working with DVI output:

``` bash
latex document.tex
dvips -o document.ps document.dvi
ps2pdf document.ps
```

## Modern Alternatives

If you’re using pdfLaTeX or XeLaTeX (recommended), you can skip EPS conversion entirely and use JPG directly:

``` latex
\includegraphics[width=0.8\textwidth]{image.jpg}
```

For Lua or XeLaTeX with UTF-8, direct JPG support is native and often performs better than EPS conversion.

## Batch Processing with Quality Control

For production workflows, wrap conversions with error handling:

``` bash
#!/bin/bash
for jpg_file in *.jpg; do
    if convert "$jpg_file" -quality 90 "${jpg_file%.jpg}.eps" 2>/dev/null; then
        echo "Converted: $jpg_file"
    else
        echo "Failed: $jpg_file"
    fi
done
```

## Troubleshooting

**ImageMagick policy blocks PDF/EPS:**

If you encounter policy errors, check `/etc/ImageMagick-6/policy.xml` and verify EPS/PDF operations aren’t disabled. Some distributions restrict these formats for security reasons.

**Large file sizes:**

EPS files can be significantly larger than the original JPG. Use `-quality` and `-density` flags to control output size and resolution.

**Loss of color fidelity:**

EPS has different color space handling than JPG. Test with `-colorspace RGB` or `-colorspace CMYK` depending on your requirements.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
