---
title: "pbmtoepsi(1)"
name: "pbmtoepsi"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmtoepsi/"
description: "pbmtoepsi – convert a portable bitmap into an encapsulated PostScript style preview bitmap"
---

<h2 class="name">NAME</h2>
<p> pbmtoepsi &#8211; convert a portable bitmap into an encapsulated PostScript style preview bitmap </p>
<h2>SYNOPSIS</h2>
<p> <code>pbmtoepsi</code> [<code>-bbonly</code>] [<i>pbmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable bitmap as input. Produce an encapsulated Postscript style bitmap as output. The output is not a stand alone postscript file, it is only a preview bitmap, which can be included in an encapsulated PostScript file. Note that there is no epsitopbm tool &#8211; this transformation is one way. </p>
<p> This utility is a part of the pstoepsi tool by Doug Crabill (dgc [at] cs.purdue.edu).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-bbonly</code></p>
<dd> Only create a boundary box, don&#8217;t fill it with the image.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5), <code><a href="/docs/linux/man/1-pnmtops/">pnmtops</a></code>(1), <code><a href="/docs/linux/man/1-pstopnm/">pstopnm</a></code>(1), <code><a href="/docs/linux/man/1-psidtopgm/">psidtopgm</a></code>(1), <code><a href="/docs/linux/man/1-pbmtolps/">pbmtolps</a></code>(1), <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1988 Jef Poskanzer, modified by Doug Crabill 1992 </p>
<h2>Index</h2>
