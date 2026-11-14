---
title: "lualatex(1)"
name: "lualatex"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lualatex/"
description: "latex, pdflatex, xelatex, lualatex, dvilualatex, cslatex, pdfcslatex, platex, uplatex, lamed – structured text formatting and typesetting"
---

<h2 class="name">NAME</h2>
<p> latex, pdflatex, xelatex, lualatex, dvilualatex, cslatex, pdfcslatex, platex, uplatex, lamed &#8211; structured text formatting and typesetting </p>
<h2>SYNOPSIS</h2>
<p> <code>latex</code> [<i>first-line</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page is a mere skeleton. </p>
<p> The LaTeX language is described in the book <i>LaTeX &#8211; A Document Preparation System</i>. LaTeX is a TeX macro package, not a modification to the TeX source program, so all the capabilities described in <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) are present. </p>
<p> The LaTeX macros encourage writers to think about the content of their documents, rather than the form. The ideal, very difficult to realize, is to have no formatting commands (like &#8220;switch to italic&#8221; or &#8220;skip 2 picas&#8221;) in the document at all; instead, everything is done by specific markup instructions: &#8220;emphasize&#8221;, &#8220;start a section&#8221;. </p>
<p> The primary source of documentation for LaTeX is the LaTeX manual referenced below. </p>
<p> <code>lualatex</code>, <code>pdflatex</code>, <code>pdfcslatex</code>, <code>xelatex</code> are LaTeX formats based on the respective engines. All output PDF by default.<br />
 <code>platex</code>, <code>uplatex</code> are Japanese LaTeX formats based on e-pTeX and e-upTeX (DVI output).<br />
 <code>lamed</code> is the Aleph-based LaTeX format (DVI output).<br />
 <code>dvilualatex</code> is LuaTeX-based and outputs DVI.<br />
 <code>cslatex</code> is csTeX-based (primitives integrated into pdfTeX) and outputs DVI. </p>
<p> On some systems <code>latex209</code> and <code>slitex</code> may still be available for compatibility with older versions of LaTeX. These should not be used for new texts. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-amstex/">amstex</a></code>(1), <code><a href="/docs/linux/man/1-luatex/">luatex</a></code>(1), <code><a href="/docs/linux/man/1-pdftex/">pdftex</a></code>(1), <code><a href="/docs/linux/man/1-ptex/">ptex</a></code>(1), <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1), <code><a href="/docs/linux/man/1-xetex/">xetex</a></code>(1). </p>
<p> Leslie Lamport, <i>LaTeX &#8211; A Document Preparation System</i>, Addison-Wesley, 1985, ISBN 020115790X. </p>
<p> Frank Mittelbach, Michel Goossens, Johannes Braams, David Carlisle, and Chris Rowley, <i>LaTeX Companion</i>, Addison-Wesley, 2004, ISBN 0201362996 (2nd edition). </p>
<p> The LaTeX home page is <a rel="nofollow" href="http://latex-project.org.">http://latex-project.org.</a><br />
 A list of some LaTeX tutorials is at <a rel="nofollow" href="http://www.tex.ac.uk/cgi-bin/texfaq2html?label=man-latex.">http://www.tex.ac.uk/cgi-bin/texfaq2html?label=man-latex.</a><br />
 An unofficial reference manual for LaTeX is at <a rel="nofollow" href="https://ctan.org/pkg/latex2e-help-texinfo.">https://ctan.org/pkg/latex2e-help-texinfo.</a> </p>
<h2>Index</h2>
