---
title: "Installing LaTeX and Compiling Documents on Linux"
date: 2018-03-24 08:04:32 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-compile-latex-on-linux/
---

LaTeX is a document preparation system widely used for scientific and technical documents. Most modern workflows use `pdflatex` or `xelatex` to compile directly to PDF, avoiding the outdated DVI → PostScript → PDF pipeline.

### Debian/Ubuntu

``` bash
sudo apt-get update
sudo apt-get install texlive-latex-base texlive-latex-extra texlive-fonts-recommended
```

For a complete installation with all packages:

``` bash
sudo apt-get install texlive-full
```

### RHEL/CentOS/Fedora

``` bash
sudo dnf install texlive-scheme-full
```

Or for a minimal install:

``` bash
sudo dnf install texlive-latex texlive-latex-fonts
```

### Arch Linux

``` bash
sudo pacman -S texlive-core texlive-latexextra
```

## Compiling LaTeX Documents

The modern approach is to use `pdflatex`, `xelatex`, or `lualatex` to generate PDF output directly. This is simpler and more reliable than the DVI conversion chain.

### Basic Compilation

For a document named `document.tex`:

``` bash
pdflatex document.tex
```

This generates `document.pdf` directly.

### With Bibliography

If your document uses BibTeX references:

``` bash
pdflatex document.tex
bibtex document.aux
pdflatex document.tex
pdflatex document.tex
```

Run `pdflatex` twice after `bibtex` to resolve all cross-references and citations correctly.

### Using XeLaTeX

For documents requiring advanced font support or Unicode:

``` bash
xelatex document.tex
bibtex document.aux
xelatex document.tex
xelatex document.tex
```

### Automating with Latexmk

The `latexmk` tool automatically handles recompilation, bibliography generation, and index creation:

``` bash
sudo apt-get install latexmk  # Debian/Ubuntu
sudo dnf install latexmk      # RHEL/Fedora
```

Then simply run:

``` bash
latexmk -pdf document.tex
```

This automatically runs `pdflatex`, `bibtex`, and indexing tools as needed. Use `-pdfxe` for XeLaTeX or `-pdflua` for LuaLaTeX.

## Using Make for Project Automation

For projects with multiple documents, a Makefile provides clear dependency management:

``` makefile
MAIN = document
LATEX = pdflatex
LATEXFLAGS = -interaction=nonstopmode -halt-on-error

.PHONY: all clean view

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex $(MAIN).bib
    $(LATEX) $(LATEXFLAGS) $(MAIN).tex
    bibtex $(MAIN)
    $(LATEX) $(LATEXFLAGS) $(MAIN).tex
    $(LATEX) $(LATEXFLAGS) $(MAIN).tex

view: $(MAIN).pdf
    xdg-open $(MAIN).pdf &

clean:
    rm -f $(MAIN).{pdf,aux,log,bbl,blg,out,toc,lot,lof}
    rm -f texput.log
```

Run `make` to compile, `make view` to open the PDF, and `make clean` to remove build artifacts.

## Handling Common Issues

### Undefined References

If you see `??` in the output or undefined reference warnings, rerun the full compilation cycle:

``` bash
pdflatex document.tex
bibtex document.aux
pdflatex document.tex
pdflatex document.tex
```

### Memory Issues with Large Documents

For documents with many images or complex graphics, increase TeX’s memory:

``` bash
pdflatex -interaction=nonstopmode --extra-mem-bot=10000000 document.tex
```

### Font Issues with XeLaTeX

Verify fonts are installed on your system:

``` bash
fc-list | grep "Font Name"
```

Specify fonts explicitly in your document’s preamble:

``` latex
\usepackage{fontspec}
\setmainfont{Liberation Serif}
\setsansfont{Liberation Sans}
```

## Continuous Compilation

For live editing, use `latexmk` in continuous mode:

``` bash
latexmk -pdf -pvc document.tex
```

This watches for changes and recompiles automatically. Press `q` to exit.

Alternatively, use `entr` for file monitoring:

``` bash
ls *.tex *.bib | entr pdflatex document.tex
```

## Output Quality

Modern `pdflatex` produces high-quality PDF output suitable for print and screen. If you need additional control over PDF properties, use `gs` (Ghostscript) for post-processing:

``` bash
gs -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -o optimized.pdf document.pdf
```

Use `/prepress` for print-ready PDFs with high image resolution, or `/ebook` for smaller file sizes.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Installing LaTeX and Compiling Documents on Linux with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for Installing LaTeX and Compiling Documents on Linux. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
