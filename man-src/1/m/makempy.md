---
title: "makempy(1)"
name: "makempy"
section: "1"
letter: "m"
url: "/docs/linux/man/1-makempy/"
description: "makempy – convert PDF or PostScript text to MetaPost graphics"
---

<h2 class="name">NAME</h2>
<p> makempy &#8211; convert PDF or PostScript text to MetaPost graphics</p>
<h2>SYNOPSIS</h2>
<p> <code>makempy</code> <i>filenam</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>makempy</code> takes MetaPost output files (<i>*.mpo</i>) and translates them to <i>*.mpy</i> files. In order to include text as a graphic into a file typeset with (Con)TeX(t), you extract the text from Postscript of PDF files using <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1) and <code><a href="/docs/linux/man/1-pstoedit/">pstoedit</a></code>(1), creating a Metapost input file. </p>
<p> This file can then be processed by <code>makempy</code>. The <code>makempy</code> script does its work without user intervention. When it deduces that there are no changes, it does not do anything; otherwise it reports its steps and any errors.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> print basic usage information</p>
<dt><code>&#8211;silent</code></p>
<dd> don&#8217;t report status messages</p>
<dt><code>&#8211;force</code></p>
<dd> always process the file (no checksum test)</p>
<dt><code>&#8211;noclean</code></p>
<dd> don&#8217;t remove temporary files when finished</p>
<dt><code>&#8211;pdftops</code></p>
<dd> use <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), part of the <code><a href="/docs/linux/man/1-xpdf/">xpdf</a></code>(1) programs, to convert PDF to PostScript</p>
<dt><code>&#8211;ghostscript</code></p>
<dd> use GhostScript (see <code><a href="/docs/linux/man/1-pdf2ps/">pdf2ps</a></code>(1)) to convert PDF to PostScript </p>
</dl>
<h2>VARIABLES</h2>
<p> When set, the environment variables GS and GS_PROG will be used to identify GHOSTSCRIPT. The names of the other programs that are used can be set with PDFTOPS and PSTOEDIT.</p>
<dl>
<dt>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mpost/">mpost</a></code>(1), <code><a href="/docs/linux/man/1-mptopdf/">mptopdf</a></code>(1), <code><a href="/docs/linux/man/1-pstoedit/">pstoedit</a></code>(1), <code><a href="/docs/linux/man/1-texexec/">texexec</a></code>(1). </p>
<dd>The makempy manual, <i>mmakempy.pdf</i>, available from <a rel="nofollow" href="http://www.pragma-ade.com/dir/general/manuals/">http://www.pragma-ade.com/dir/general/manuals/</a> laURL: L raPRAGMA ADE </p>
<p> <a rel="nofollow" href="http://www.contextgarden.net">http://www.contextgarden.net</a> laURL: L raConTeXt wiki </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Frank K[:u]ster &lt;frank [at] kuesterei.ch&gt;, for the Debian GNU/Linux system. It may be used and modified by others without contacting the author. </p>
<h2>Index</h2>
