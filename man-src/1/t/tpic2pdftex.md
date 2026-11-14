---
title: "tpic2pdftex(1)"
name: "tpic2pdftex"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tpic2pdftex/"
description: "tpic2pdftex – convert tpic \\specials for use by pdftex"
---

<h2 class="name">NAME</h2>
<p> tpic2pdftex &#8211; convert tpic \specials for use by pdftex</p>
<h2>SYNOPSIS</h2>
<p> <code>pic</code> -t <i>somefile.pic</i> | <code>tpic2pdftex</code> &gt; <i>somefile.tex</i> </p>
<p> Process <i>somefile.tex</i> by <code>pdftex/pdflatex.</code> </p>
<h2>DESCRIPTION</h2>
<p> Experimental <code>awk</code> script for conversion of <code>tpic</code> \specials as produced by <code>(groff-)pic</code> into <code>pdfTeX</code> \pdfliteral sections for further processing by <code>pdftex.</code> </p>
<h2>NOTES</h2>
<p> Current version: 1.97. </p>
<p> <code>tpic</code> \special description see e. g.: Goossens, Rahtz, Mittelbach: The LaTeX Graphics Companion, Addison-Wesley, 1997, pp. 464. </p>
<h2>BUGS</h2>
<p> Spline curve shapes not fully authentic (unknown algorithm). Bounding box does not care for line thickness (groff pic feature). Splines might be outside bounding box. Fill color does not work correctly for arrowheads (pic limitation). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pic/">pic</a></code>(1), <code><a href="/docs/linux/man/1-grap/">grap</a></code>(1), <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-awk/">awk</a></code>(1), <code><a href="/docs/linux/man/1-pdftex/">pdftex</a></code>(1). </p>
<h2>Index</h2>
