---
title: "pdfopt(1)"
name: "pdfopt"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfopt/"
description: "pdfopt – Ghostscript PDF Optimizer"
---

<h2>NAME</h2>
<p> pdfopt &#8211; Ghostscript PDF Optimizer</p>
<h2>SYNOPSIS</h2>
<p> <code>pdfopt</code> [ <i>options</i> ] <i>input.pdf output.pdf</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pdfopt</code> uses <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1) to convert the Adobe <code>Portable Document Format</code> (PDF) file &quot;input.pdf&quot; to a so-called optimized form in &quot;output.pdf&quot;. Optimization puts the elements of the file into a more linear order and adds &quot;hint&quot; pointers, allowing Adobe&#8217;s Acrobat(TM) products to display individual pages of the file more quickly when accessing the file through a network. </p>
<p> Note: input.pdf and output.pdf must not be the same. If they are, the file will probably be destroyed. <code>pdfopt</code> currently does not check for this.</p>
<h2>FILES</h2>
<p> Run &quot;<code>gs -h</code>&quot; to find the location of Ghostscript documentation on your system, from which you can get more details.</p>
<h2>SEE ALSO</h2>
<p> &quot;Linearized PDF&quot; in Adobe&#8217;s PDF reference manual, <a rel="nofollow" href="http://partners.adobe.com/asn/developer/acrosdk/DOCS/pdfspec.pdf">http://partners.adobe.com/asn/developer/acrosdk/DOCS/pdfspec.pdf</a></p>
<h2>VERSION</h2>
<p> This document was last revised for Ghostscript version 9.06.</p>
<h2>AUTHOR</h2>
<p> Artifex Software, Inc. are the primary maintainers of Ghostscript. </p>
<h2>Index</h2>
