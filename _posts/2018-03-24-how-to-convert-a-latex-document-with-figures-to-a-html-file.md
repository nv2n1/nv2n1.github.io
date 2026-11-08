---
title: "Converting LaTeX Documents with Figures to HTML"
date: 2018-03-24 08:22:27 +0000
author: "Eric Ma"
layout: post
categories: [web-development]
canonical: /how-to-convert-a-latex-document-with-figures-to-a-html-file/
---

Converting LaTeX to HTML while preserving figures is essential when publishing technical documentation online. The right tool depends on your document complexity and output requirements.

## tex4ht (htlatex)

tex4ht is the most reliable option for LaTeX documents with figures, math, and complex formatting. It’s part of the TeX Live distribution and available on all major platforms.

Install via package manager:

``` bash
# Ubuntu/Debian
sudo apt install tex4ht

# Fedora/RHEL
sudo dnf install texlive-tex4ht

# macOS
brew install tex4ht
```

Basic conversion:

``` bash
htlatex myfile.tex
```

This generates `myfile.html`, `myfile.css`, and image files (typically PNG) for figures and equations in the same directory.

## Configuration Options

Control output format and behavior with configuration strings passed to htlatex:

``` bash
htlatex myfile.tex "html5,mathml,pic-align"
```

Common options:

- `html5` — Generate HTML5 output (recommended over older XHTML)
- `mathml` — Use MathML for equation rendering (semantic, no JavaScript required)
- `mathjax` — Use MathJax for equations (requires JavaScript, better for complex math)
- `pic-align` — Align figures properly relative to text
- `pic-m` — Convert figures to inline graphics
- `charset=utf-8` — Specify character encoding explicitly

## Handling Figures

Standard `\includegraphics` commands convert automatically, but you may need to adjust based on figure format and location.

If figures use PDF format and aren’t converting properly:

``` bash
# Convert PDF figures to PNG at high resolution
for fig in figures/*.pdf; do
    convert -density 300 "$fig" "${fig%.pdf}.png"
done
```

For documents with many figures, use explicit output directory and verbose mode:

``` bash
htlatex myfile.tex "html5,pic-align" "" "" --output-directory=html -v
```

If figures reference absolute paths, convert them to relative paths in your LaTeX source first, or use `\graphicspath`:

``` latex
\usepackage{graphicx}
\graphicspath{% raw %}{{{% endraw %}./figures/}}
```

## Math Rendering

Choose your math strategy based on the output environment:

**MathML (no JavaScript)**:

``` bash
htlatex myfile.tex "html5,mathml"
```

**MathJax (better rendering, requires JavaScript)**:

``` bash
htlatex myfile.tex "html5,mathjax"
```

**KaTeX (lightweight, modern)**:

``` bash
htlatex myfile.tex "html5,mathjax"
# Then manually replace MathJax CDN with KaTeX in generated HTML
```

## CSS and Styling

tex4ht generates a default CSS file (`myfile.css`). Customize it directly for branding or layout adjustments.

Suppress default CSS if you want to style from scratch:

``` bash
htlatex myfile.tex "html5,pic-align" "" "0"
```

Add custom CSS in your LaTeX preamble:

``` latex
\usepackage{xcolor}
\begin{document}
\Configure{HtmlPar}{\par}
```

## Alternative: Pandoc

For simpler documents without complex LaTeX macros or TikZ graphics:

``` bash
pandoc -f latex -t html5 --mathml --wrap=none myfile.tex -o myfile.html
```

Pandoc is faster and produces cleaner HTML for straightforward documents, but struggles with:

- Custom LaTeX commands
- TikZ diagrams
- Complex macros and environments

## Batch Processing

Convert multiple files efficiently:

``` bash
#!/bin/bash
for file in *.tex; do
    echo "Converting $file..."
    htlatex "$file" "html5,mathml,pic-align" "" "" --output-directory=html
done
```

For large projects, use `make` to avoid reconverting unchanged files:

``` makefile
HTML_FILES = $(patsubst %.tex,html/%.html,$(wildcard *.tex))

all: $(HTML_FILES)

html/%.html: %.tex
    htlatex $< "html5,mathml,pic-align" "" "" --output-directory=html
```

## Troubleshooting

**Figures not appearing:**

- Verify relative paths in `\includegraphics` are correct
- Check image file permissions and formats
- Run with verbose flag: `htlatex myfile.tex "html5,pic-align" "" "" -v`
- Test PNG output explicitly: `convert -density 300 input.pdf output.png`

**Broken equations:**

- Try MathML: `htlatex myfile.tex "html5,mathml"`
- Check for unsupported LaTeX packages; some conflict with tex4ht
- Verify preamble UTF-8 encoding: `\usepackage[utf-8]{inputenc}`

**Unwanted whitespace or layout issues:**

- Edit generated CSS manually
- Use `pic-align` and `pic-m` options together
- Strip HTML comments: `sed -i 's/<!--.*-->//g' myfile.html`

**TikZ figures not converting:**

- tex4ht has limited TikZ support; convert TikZ to SVG or PDF first
- Use `\immediate\write18` in TeX to externalize graphics

tex4ht remains the practical standard for LaTeX-to-HTML conversion with figures. Choose Pandoc only if your document is simple and doesn’t rely on LaTeX-specific features.
