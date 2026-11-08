---
title: "Installing the Caption LaTeX Package on Fedora"
date: 2018-03-24 08:14:22 +0000
layout: post
canonical: https://www.systutorials.com/how-to-install-the-caption-latex-package-on-fedora/
---

The `caption` LaTeX package provides customizable captions for floats (figures, tables, and other environments). It offers much more control than LaTeX’s default caption formatting.

## Install on Fedora

The caption package is included in the texlive collection:

```wp-block-code
# Install the full texlive collection (includes caption)
sudo dnf install texlive-collection-latexrecommended

# Or install just the caption package
sudo dnf install texlive-caption
```

Verify the installation:

```wp-block-code
kpsewhich caption.sty
```

If it returns a path like `/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty`, the package is installed.

## Basic Usage

Load the package in your document preamble:

```wp-block-code
\usepackage{caption}
```

Customize caption appearance:

```wp-block-code
\usepackage{caption}
\captionsetup{
    font=small,
    labelfont=bf,
    format=plain,
    labelsep=period,
    justification=centering
}
```

## Common Caption Styles

**Bold label with period separator:**

```wp-block-code
\captionsetup{labelfont=bf, labelsep=period}
% Produces: "Figure 1. Description text"
```

**Small caps label:**

```wp-block-code
\captionsetup{labelfont=sc, labelsep=quad}
% Produces: "FIGURE 1    Description text"
```

**Sans-serif captions:**

```wp-block-code
\captionsetup{font={sf, small}, labelfont=bf}
```

## Per-Environment Settings

Configure captions differently for figures and tables:

```wp-block-code
\captionsetup[figure]{font=small, labelfont=bf}
\captionsetup[table]{font=small, labelfont=it, position=above}
```

## Caption Position

By convention, figure captions go below and table captions go above:

```wp-block-code
\begin{figure}
    \includegraphics{image.pdf}
    \caption{Description of the figure}
    \label{fig:example}
\end{figure}

\begin{table}
    \caption{Description of the table}
    \label{tab:example}
    \begin{tabular}{cc}
        A & B \\
        1 & 2
    \end{tabular}
\end{table}
```

## Subcaptions

Combine with the `subcaption` package for subfigures:

```wp-block-code
\usepackage{caption}
\usepackage{subcaption}

\begin{figure}
    \begin{subfigure}{0.5\textwidth}
        \includegraphics{image1.pdf}
        \caption{First subfigure}
        \label{fig:sub1}
    \end{subfigure}
    \begin{subfigure}{0.5\textwidth}
        \includegraphics{image2.pdf}
        \caption{Second subfigure}
        \label{fig:sub2}
    \end{subfigure}
    \caption{Overall figure caption}
    \label{fig:main}
\end{figure}
```

## Caption Width and Formatting

```wp-block-code
% Set caption width narrower than text
\captionsetup{width=0.8\textwidth}

% Single-line captions centered, multi-line justified
\captionsetup{justification=centering, singlelinecheck=off}

% Skip space between caption and float
\captionsetup{skip=10pt}
```

## Compatibility with Other Packages

The caption package works well with:

- **hyperref** — Captions are properly linked in PDF bookmarks
- **babel** — Automatic translation of “Figure” and “Table” labels
- **memoir** — Caption package can override memoir’s caption settings
- **float** — Enhanced float placement alongside caption customization

Load `hyperref` last in your preamble to ensure proper link generation:

```wp-block-code
\usepackage{caption}
\usepackage{subcaption}
\usepackage{hyperref}  % Load last
```

## Quick Reference

- `sudo dnf install texlive-caption` — Install on Fedora
- `\usepackage{caption}` — Load the package
- `\captionsetup{labelfont=bf}` — Bold labels
- `\usepackage{subcaption}` — Subfigure support
- `kpsewhich caption.sty` — Verify installation

## Custom Caption Labels

Rename the default label text:

```wp-block-code
\usepackage{caption}
\captionsetup[figure]{name=Fig.}
\captionsetup[table]{name=Tab.}

% Produces: "Fig. 1. Description" instead of "Figure 1. Description"
```

For more complex label customization, use the `titlesec` or `caption` label format options:

```wp-block-code
\DeclareCaptionLabelFormat{r-paren}{#1 (#2)}
\captionsetup{labelformat=r-paren}
% Produces: "Figure (1) Description"
```

## List of Figures and Tables

The caption package improves the entries in lists of figures and tables:

```wp-block-code
\usepackage{caption}
\captionsetup{listformat= simple}  % Or: subsimple, parens, etc.

% In your document
\listoffigures
\listoftables
```

## Manually Installing LaTeX Packages

If a LaTeX package isn’t available through dnf, install it manually:

```wp-block-code
# Create local texmf tree
mkdir -p ~/texmf/tex/latex/caption

# Download from CTAN
curl -L https://ctan.org/tex-archive/macros/latex/contrib/caption.tar.gz | tar xz -C ~/texmf/tex/latex/

# Update filename database
texhash ~/texmf
```

LaTeX automatically searches `~/texmf/` for packages, so manually installed packages coexist with system packages without conflicts.

## Troubleshooting Caption Issues

**“Package caption Error: Continued float outside float.”:**

This error occurs when using `\ContinuedFloat` outside a figure or table environment. Ensure it’s inside the correct float:

```wp-block-code
\begin{figure}
    \includegraphics{part2.pdf}
    \caption{Example (cont.)}
    \ContinuedFloat  % Must be inside figure environment
\end{figure}
```

**Caption numbering is wrong:**

Reset the counter or check for conflicts with other packages that modify counters:

```wp-block-code
\setcounter{figure}{0}
\setcounter{table}{0}
```

**Caption not appearing in list of figures:**

Make sure you’ve run LaTeX twice — the first run collects caption data, the second generates the list. Also verify that `\caption` is inside the float environment, not outside it.
