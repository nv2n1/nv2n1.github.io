---
title: "pdf2ps(1)"
name: "pdf2ps"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdf2ps/"
description: "pdf2ps – Ghostscript PDF to PostScript translator"
---

<h2 class="name">NAME</h2>
<p> pdf2ps &#8211; Ghostscript PDF to PostScript translator </p>
<h2>SYNOPSIS</h2>
<p> <code>pdf2ps</code> [ <i>options</i> ] <i>input.pdf [output.ps]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pdf2ps</code> uses <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1) to convert the Adobe <code>Portable Document Format</code> (PDF) file &quot;input.pdf&quot; to <code>PostScript</code>(tm) in &quot;output.ps&quot;. Normally the output is allowed to use PostScript Level 2 (but not PostScript LanguageLevel 3) constructs; the <code>-dLanguageLevel=1</code> option restricts the output to Level 1, while <code>-dLanguageLevel=3</code> allows using LanguageLevel 3 in the output.</p>
<h2>FILES</h2>
<p> Run &quot;<code>gs -h</code>&quot; to find the location of Ghostscript documentation on your system, from which you can get more details.</p>
<h2>VERSION</h2>
<p> This document was last revised for Ghostscript version 9.55.0.</p>
<h2>AUTHOR</h2>
<p> Artifex Software, Inc. are the primary maintainers of Ghostscript. </p>
<h2>Index</h2>
