---
title: "bibtex(1)"
name: "bibtex"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bibtex/"
description: "bibtex – make a bibliography for (La)TeX"
---
<h2>SYNOPSIS</h2>
<p> <code>bibtex</code> [<code>-min-crossrefs=</code><i>number</i>] [<code>-terse</code>] <i>auxname</i>[<i></i><code>.aux</code>]  </p>
<h2>DESCRIPTION</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> BibTeX reads the top-level auxiliary (<code>.aux</code>) file <i>auxname</i> that was output during the running of <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1) or <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) and creates a bibliography (<code>.bbl</code>) file that will be incorporated into the document on subsequent runs of LaTeX or TeX. </p>
<p> BibTeX looks up, in bibliographic database (<code>.bib</code>) files specified by the \bibliography command, the entries specified by the \cite and \nocite commands in the LaTeX or TeX source file. It formats the information from those entries according to instructions in a bibliography style (<code>.bst</code>) file (specified by the \bibliographystyle command, and it outputs the results to the <code>.bbl</code> file. </p>
<p> The LaTeX manual explains what a LaTeX source file must contain to work with BibTeX. Appendix B of the manual describes the format of the <code>.bib</code> files. The `BibTeXing&#8217; document describes extensions and details of this format, and it gives other useful hints for using BibTeX.  </p>
<h2>OPTIONS</h2>
<p> The <code>-min-crossrefs</code> option defines the minimum number of <code>crossref</code> required for automatic inclusion of the crossref base entry in the citation list; the default is two. To avoid these automatic inclusions altogether, give this option a sufficiently large number, and be sure to remove any previous <code>.aux </code> and <code>.bbl</code> files. Otherwise the option may appear to have no effect, since BibTeX will have added the citation for the base entry to the <code>.aux</code> file, and nothing will remove it. </p>
<p> With the <code>-terse</code> option, BibTeX operates silently. Without it, a banner and progress reports are printed on <i>stdout</i>. </p>
<h2>ENVIRONMENT</h2>
<p> BibTeX searches the directories in the path defined by the BSTINPUTS environment variable for <code>.bst</code> files. If BSTINPUTS is not set, it uses the system default. For <code>.bib</code> files, it uses the BIBINPUTS environment variable if that is set, otherwise the default. See <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) for the details of the searching. </p>
<p> If the environment variable TEXMFOUTPUT is set, BibTeX attempts to put its output files in it, if they cannot be put in the current directory. Again, see <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1). No special searching is done for the <code>.aux</code> file.  </p>
<h2>FILES</h2>
<dl>
<dt><i>*.bst</i></dt>
<dd> <p> Bibliography style files. </p>
 </dd>
<dt><i>btxdoc.tex</i></dt>
<dd> <p> ``BibTeXing&#8217;&#8216; - LaTeXable documentation for general BibTeX users </p>
 </dd>
<dt><i>btxhak.tex</i></dt>
<dd> <p> ``Designing BibTeX Styles&#8217;&#8216; - LaTeXable documentation for style designers </p>
 </dd>
<dt><i>btxdoc.bib</i></dt>
<dd> <p> database file for those two documents </p>
 </dd>
<dt><i>xampl.bib</i></dt>
<dd> <p> database file giving examples of all standard entry types </p>
 </dd>
<dt><i>btxbst.doc</i></dt>
<dd> <p> template file and documentation for the standard styles </p>
 </dd></dl>
<p> All those files should be available somewhere on your system. </p>
<p> The host math.utah.edu has a vast collection of <code>.bib</code> files available for anonymous ftp, including references for all the standard TeX books and a complete bibliography for TUGboat.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1), <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1). <br />
 Leslie Lamport, <i>LaTeX - A Document Preparation System</i>, Addison-Wesley, 1985, ISBN 0-201-15790-X.  </p>
<h2>AUTHOR</h2>
<p> Oren Patashnik, Stanford University. This man page describes the web2c version of BibTeX. Other ports of BibTeX, such as Donald Knuth&#8217;s version using the Sun Pascal compiler, do not have the same path searching implementation, or the command-line options. </p>
