---
title: "eps2eps(1)"
name: "eps2eps"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eps2eps/"
description: "ps2ps, eps2eps – Ghostscript PostScript \"distiller\""
---

<h2 class="name">NAME</h2>
<p> ps2ps, eps2eps &#8211; Ghostscript PostScript &quot;distiller&quot; </p>
<h2>SYNOPSIS</h2>
<p> <code>ps2ps</code> [ <i>options</i> ] <i>input output.ps</i><br />
 <code>eps2eps</code> [ <i>options</i> ] <i>input output.eps</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ps2ps</code> uses <i><a href="/docs/linux/man/1-gs/">gs</a></i>(1) to convert <code>PostScript</code>(tm) or <code>PDF</code>(tm) file &quot;input&quot; to simpler, normalized and (usually) faster PostScript in &quot;output.ps&quot;. The output is level 2 DSC 3.0 conforming PostScript. </p>
<p> <code>eps2eps</code> performs the equivalent optimization, creating Encapsulated PostScript (EPS) files. NB, despite the name, the input need not be an EPS file, PostScript or indeed PDF files are equally acceptable. </p>
<p> Both accept any general Ghostscript command line options, and options specific to the ps2write and eps2write devices.</p>
<h2>FILES</h2>
<p> Run &quot;<code>gs -h</code>&quot; to find the location of Ghostscript documentation on your system, from which you can get more details.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ps2pdf/">ps2pdf</a>(1), <a href="/docs/linux/man/1-ps2ascii/">ps2ascii</a>(1), <a href="/docs/linux/man/1-ps2epsi/">ps2epsi</a>(1)</p>
<h2>VERSION</h2>
<p> This document was last revised for Ghostscript version 9.55.0.</p>
<h2>AUTHOR</h2>
<p> Artifex Software, Inc. are the primary maintainers of Ghostscript. </p>
<h2>Index</h2>
