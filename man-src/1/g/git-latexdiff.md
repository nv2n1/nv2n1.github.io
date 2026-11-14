---
title: "git-latexdiff(1)"
name: "git-latexdiff"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-latexdiff/"
---

<h2 class="name">NAME</h2>
 

 git-latexdiff - Call latexdiff on two Git revisions of a file 

<h2>OPTIONS</h2>

 

<dl>
<dt>
<dd> <pre><code>
Usage: git latexdiff [options] OLD [NEW]
       git latexdiff [options] OLD --
       git latexdiff [options] -- OLD
Call latexdiff on two Git revisions of a file.
OLD and NEW are Git revision identifiers. NEW defaults to HEAD.
If "--" is used for NEW, then diff against the working directory.
Options:
    --help                this help message
    --help-examples       show examples of usage
    --main &lt;file&gt;         name of the main LaTeX, R Sweave,
                            or Emacs Org mode file.
                            The search for the only file containing 'documentclass'
                            will be attempted, if not specified.
                            For non-LaTeX files, a reasonable `prepare` command
                            will be used unless explicitly provided
    --no-view             don't display the resulting PDF file
    --latex               run latex instead of pdflatex
    --xelatex             run xelatex instead of pdflatex
    --lualatex            run lualatex instead of pdflatex
    --tectonic            run tectonic instead of pdflatex
    --bibtex, --bbl       display changes in the bibliography
                             (runs bibtex to generate *.bbl files and
                             include them in the source file using
                             latexpand --expand-bbl before computing
                             the diff)
    --biber               like --bibtex, but runs biber instead.
    --run-bibtex, -b      run bibtex as well as latex to generate the PDF file
                             (pdflatex,bibtex,pdflatex,pdflatex)
                          NOTE: --bibtex usually works better
    --run-biber           run BibLaTex-Biber as well as latex to generate the PDF file
                             (pdflatex,biber,pdflatex,pdflatex)
                          NOTE: --biber usually works better
    --view                view the resulting PDF file
                            (default if -o is not used)
    --pdf-viewer &lt;cmd&gt;    use &lt;cmd&gt; to view the PDF file (default: $PDFVIEWER)
    --no-cleanup          don't cleanup temp dir after running
    --no-flatten          don't call latexpand to flatten the document
    --cleanup MODE        Cleanup temporary files according to MODE:
                           - keeppdf (default): keep only the
                                  generated PDF file
                           - none: keep all temporary files
                                  (may eat your diskspace)
                           - all: erase all generated files.
                                  Problematic with --view when the
                                  viewer is e.g. evince, and doesn't
                                  like when the file being viewed is
                                  deleted.
    --latexmk             use latexmk
    --build-dir           use pdfs from specific build directory
    --latexopt            pass additional options to latex (e.g. -shell-escape)
    -o &lt;file&gt;, --output &lt;file&gt;
                          copy resulting PDF into &lt;file&gt; (usually ending with .pdf)
                          Implies "--cleanup all"
    --tmpdirprefix        where temporary directory will be created (default: /tmp).
                            Relative path will use repository root as a base
    --verbose, -v         give more verbose output
    --quiet               redirect output from subprocesses to log files
    --prepare &lt;cmd&gt;       run &lt;cmd&gt; before latexdiff (e.g. run make to generate
                             included files)
    --filter &lt;cmd&gt;        run &lt;cmd&gt; after latexdiff and before compilation
                             (e.g. to fix up latexdiff output)
    --ln-untracked        symlink uncommited files from the working directory
    --version             show git-latexdiff version.
    --subtree             checkout the tree at and below the main file
                             (enabled by default, disable with --whole-tree)
    --whole-tree          checkout the whole tree (contrast with --subtree)
    --ignore-latex-errors keep on going even if latex gives errors, so long as
                          a PDF file is produced
    --ignore-makefile     ignore the Makefile, build as though it doesn't exist
    -*                    other options are passed directly to latexdiff
    --latexpand OPT       pass option OPT to latexpand. Use multiple times like
                          --latexpand OPT1 --latexpand OPT2 to pass multiple options.
    --latexdiff-flatten   use --flatten from latexdiff instead of latexpand
Unrecognized options are passed unmodified to latexdiff.
Examples:
Diff the previous revision with the latest commit:
    git latexdiff HEAD^
Diff the latest commit with the working tree:
    git latexdiff HEAD --
Diff latest commit with branch master:
    git latexdiff master HEAD
Pass --type=CHANGEBAR to latexdiff to get changebars in the margins
instead of red+trike/blue+underline diff:
    git latexdiff --type=CHANGEBAR HEAD^
Use a specific latexdiff configuration file:
    git latexdiff --config /path/to/file HEAD^
</code></pre></dl>
 

<h2>Index</h2>


