---
title: "LaTeX Essentials: Key Commands and Document Setup"
date: 2013-07-12 16:54:49 +0000
author: "Eric Ma"
layout: post
categories: [security-cryptography-2]
canonical: /latex-cheat-sheet/
---

Every LaTeX document requires a basic framework. Here’s the minimum viable structure:

``` latex
\documentclass{article}
\usepackage[utf-8]{inputenc}

\title{My Document}
\author{Author Name}
\date{\today}

\begin{document}

\maketitle

\section{Introduction}
Your content here.

\end{document}
```

Common document classes:

- `article` — reports, papers, short documents
- `report` — longer documents with chapters
- `book` — book-length documents with front/back matter
- `beamer` — slide presentations
- `letter` — formal correspondence

Add packages with `\usepackage{}` before `\begin{document}`. The `inputenc` package with UTF-8 encoding is standard for modern systems and ensures proper handling of non-ASCII characters.

## Text Formatting

Basic formatting commands:

``` latex
\textbf{bold text}
\textit{italic text}
\texttt{monospace/typewriter}
\textsc{small caps}
\underline{underlined text}
```

Use `\emph{}` for semantic emphasis—it toggles italic (or returns to roman if already italic), making it preferred over raw formatting for emphasis. Combine multiple formats with nesting:

``` latex
\textbf{\textit{bold italic text}}
```

## Sections and Headings

Structure documents hierarchically:

``` latex
\section{Main Section}
\subsection{Subsection}
\subsubsection{Sub-subsection}
\paragraph{Paragraph Heading}
\subparagraph{Subparagraph Heading}
```

For unnumbered sections, append an asterisk:

``` latex
\section*{Unnumbered Section}
\subsection*{Unnumbered Subsection}
```

This applies to all heading levels. Unnumbered sections won’t appear in the table of contents by default.

## Lists

**Unordered lists** with `itemize`:

``` latex
\begin{itemize}
    \item First item
    \item Second item
    \begin{itemize}
        \item Nested item
    \end{itemize}
\end{itemize}
```

**Ordered lists** with `enumerate`:

``` latex
\begin{enumerate}
    \item First step
    \item Second step
    \item Third step
\end{enumerate}
```

**Definition/description lists** with `description`:

``` latex
\begin{description}
    \item[Term] Definition goes here
    \item[Another Term] Its definition
\end{description}
```

## Math Mode

Inline math uses single dollar signs: `$x = y + 2$` renders within text.

Display math (centered on its own line) uses double dollar signs or dedicated environments:

``` latex
$$E = mc^2$$

\begin{equation}
    E = mc^2
\end{equation}
```

Use `equation*` (or `align*`) for unnumbered display math:

``` latex
\begin{align*}
    x &= 1 \\
    y &= 2 \\
    z &= 3
\end{align*}
```

Use `align*` for aligned equations; the `&` marks alignment points.

**Common math symbols and operators:**

``` latex
% Greek letters
\alpha, \beta, \gamma, \Delta, \Sigma

% Operators
\pm, \times, \div, \leq, \geq, \neq, \approx, \equiv

% Sets
\in, \subset, \cup, \cap, \emptyset, \mathbb{R}, \mathbb{Z}

% Logic and relations
\forall, \exists, \Rightarrow, \Leftrightarrow, \therefore

% Calculus
\int, \sum, \prod, \infty, \partial, \nabla, \lim
```

For more complex math, use the `amsmath` and `amssymb` packages:

``` latex
\usepackage{amsmath}
\usepackage{amssymb}
```

## Tables

Create tables with the `tabular` environment:

``` latex
\begin{tabular}{l c r}
    Left & Center & Right \\
    \hline
    A & B & C \\
    D & E & F
\end{tabular}
```

Format specifiers:

- `l` — left-aligned
- `c` — centered
- `r` — right-aligned
- `|` — vertical lines
- `p{width}` — fixed-width column

Separate columns with `&` and rows with `\\`. Use `\hline` for horizontal lines.

For floating tables with captions and labels:

``` latex
\begin{table}
    \centering
    \begin{tabular}{|l|c|r|}
        \hline
        Name & Score & Grade \\
        \hline
        Alice & 95 & A \\
        Bob & 87 & B \\
        Charlie & 92 & A \\
        \hline
    \end{tabular}
    \caption{Student Scores}
    \label{tab:scores}
\end{table}
```

Reference with `\ref{tab:scores}` or `\autoref{tab:scores}` (requires `hyperref` package).

## Figures and Images

Insert images with the `graphicx` package:

``` latex
\usepackage{graphicx}

\begin{figure}
    \centering
    \includegraphics[width=0.8\textwidth]{image.png}
    \caption{Image caption describing the figure}
    \label{fig:myfigure}
\end{figure}
```

Width options:

- `width=0.8\textwidth` — 80% of page width
- `height=5cm` — fixed height (maintains aspect ratio)
- `scale=0.7` — scale by factor

Reference with `\ref{fig:myfigure}` or `\autoref{fig:myfigure}`.

## Citations and Bibliography

Use modern `biblatex` with `biber` backend (superior to legacy BibTeX):

Create a `.bib` file (`references.bib`):

``` bibtex
@article{smith2023,
    author = {John Smith},
    title = {A Great Paper on Machine Learning},
    journal = {Nature},
    year = {2023},
    volume = {42},
    pages = {123--145},
    doi = {10.1234/example}
}

@book{knuth1984,
    author = {Donald E. Knuth},
    title = {The TeXbook},
    publisher = {Addison-Wesley},
    year = {1984}
}
```

In your LaTeX document:

``` latex
\usepackage[style=authoryear]{biblatex}
\addbibresource{references.bib}

% Later, in your text:
\cite{smith2023}
\textcite{knuth1984}  % Author (year) format

% At end of document:
\printbibliography
```

Compilation with `biber`:

``` bash
pdflatex document.tex
biber document
pdflatex document.tex
pdflatex document.tex
```

Or use `latexmk` to automate the process (see below).

## Essential Packages

Common packages for technical and academic writing:

``` latex
\usepackage{amsmath}        % Advanced math environments
\usepackage{amssymb}        % Additional math symbols
\usepackage{geometry}       % Page margins: \usepackage[margin=1in]{geometry}
\usepackage{hyperref}       % Clickable links and PDF bookmarks
\usepackage{listings}       % Source code with syntax highlighting
\usepackage{xcolor}         % Colored text: \textcolor{red}{red text}
\usepackage{graphicx}       % Image inclusion
\usepackage{biblatex}       % Bibliography management
```

**For code listings with syntax highlighting:**

``` latex
\usepackage{listings}
\usepackage{xcolor}

\lstset{
    language=Python,
    basicstyle=\ttfamily\small,
    keywordstyle=\color{blue},
    commentstyle=\color{gray},
    breaklines=true
}

\begin{lstlisting}
def hello():
    print("Hello, World!")
\end{lstlisting}
```

## Compilation

Modern workflows use `pdflatex` or `xelatex` for rendering and `latexmk` to manage dependencies:

``` bash
# Basic compilation
pdflatex document.tex

# Automatic multi-pass compilation (recommended)
latexmk -pdf document.tex

# Watch mode (recompile on file changes)
latexmk -pdf -pvc document.tex

# Clean auxiliary files
latexmk -c document.tex
```

Use `latexmk` for documents with bibliography, cross-references, or indexes—it automatically runs multiple passes to resolve all references. Configure it with a `.latexmkrc` file in your project directory for consistent behavior across systems.

**For Unicode and system fonts**, use `xelatex` instead:

``` bash
latexmk -xelatex -pdf document.tex
```
