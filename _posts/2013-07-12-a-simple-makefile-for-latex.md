---
title: "Building LaTeX Documents with Make"
date: 2013-07-12 16:32:05 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/a-simple-makefile-for-latex/
---

Compiling LaTeX documents with BibTeX involves multiple passes—typically three runs of `latex` followed by one `bibtex` run to resolve citations. This sequence is identical across most documents, making it perfect for automation with a Makefile.

## Basic Makefile Template

Here’s a practical Makefile for LaTeX with BibTeX support:

``` makefile
FILENAME = main
LATEX = pdflatex
BIBTEX = bibtex
VIEWER = evince

.PHONY: all clean read view

all: $(FILENAME).pdf

$(FILENAME).pdf: $(FILENAME).tex
    $(LATEX) $(FILENAME)
    $(BIBTEX) $(FILENAME)
    $(LATEX) $(FILENAME)
    $(LATEX) $(FILENAME)

read: $(FILENAME).pdf
    $(VIEWER) $(FILENAME).pdf &

clean:
    rm -f $(FILENAME).aux $(FILENAME).bbl $(FILENAME).blg
    rm -f $(FILENAME).log $(FILENAME).out $(FILENAME).toc
    rm -f $(FILENAME).lof $(FILENAME).lot
    rm -f *~ *.swp

.PHONY: help
help:
    @echo "Usage:"
    @echo "  make              - Compile to PDF"
    @echo "  make read         - Compile and open in $(VIEWER)"
    @echo "  make clean        - Remove intermediate files"
```

## Configuration

Set the `FILENAME` variable to match your main `.tex` file. For example, if your document is `thesis.tex`, change:

``` makefile
FILENAME = thesis
```

The `LATEX` variable defaults to `pdflatex`, which directly generates PDF. If you need DVI output instead, change it to `latex`:

``` makefile
LATEX = latex
```

## Common Usage

**Compile to PDF:**

``` bash
make
```

**Compile and open in your PDF viewer:**

``` bash
make read
```

**Clean intermediate files without recompiling:**

``` bash
make clean
```

**Clean and rebuild:**

``` bash
make clean && make
```

## Handling Bibliography Entries

The Makefile assumes you have a `.bib` file referenced in your LaTeX document via `\bibliography{}`. BibTeX generates `.bbl` and `.blg` files that persist between runs, which is why `make clean` removes them—forcing a full rebuild on the next `make` call.

If your document doesn’t use BibTeX, remove these lines:

``` makefile
$(BIBTEX) $(FILENAME)
```

For projects with multiple chapters or includes, add dependencies to the PDF target:

``` makefile
$(FILENAME).pdf: $(FILENAME).tex chapter1.tex chapter2.tex references.bib
    $(LATEX) $(FILENAME)
    $(BIBTEX) $(FILENAME)
    $(LATEX) $(FILENAME)
    $(LATEX) $(FILENAME)
```

## Advanced Options

Use `xelatex` or `lualatex` for Unicode and system font support:

``` makefile
LATEX = xelatex
```

For continuous compilation during editing, pair this with a file watcher:

``` bash
while inotifywait -e modify *.tex; do make; done
```

Or use dedicated tools like `latexmk`, which intelligently detects when recompilation is needed:

``` bash
latexmk -pdf -pvc main.tex
```

The advantage of a custom Makefile is simplicity and explicit control—you see exactly what happens on each run, making debugging easier when compilation fails.

## Practical Tips and Common Gotchas

When working with programming languages on Linux, environment management is crucial. Use version managers like asdf, pyenv, or sdkman to handle multiple language versions without system-wide conflicts. Always pin dependency versions in production to prevent unexpected breakage from upstream changes.

For build automation, modern alternatives often outperform traditional tools. Consider using just or task instead of Make for simpler task definitions. Use containerized build environments to ensure reproducibility across different development machines.

## Debugging Strategies

Start with the simplest debugging approach and escalate as needed. Print statements and logging often reveal the issue faster than attaching a debugger. For complex issues, use language-specific debuggers like gdb for C and C++, jdb for Java, or dlv for Go. Always check error messages carefully before diving into code.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
