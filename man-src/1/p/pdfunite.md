---
title: "pdfunite(1)"
name: "pdfunite"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfunite/"
description: "pdfunite – Portable Document Format (PDF) page merger"
---

<h2 class="name">NAME</h2>
<p> pdfunite &#8211; Portable Document Format (PDF) page merger </p>
<h2>SYNOPSIS</h2>
<p> <code>pdfunite</code> [options] <i>PDF-sourcefile1..PDF-sourcefilen PDF-destfile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pdfunite</code> merges several PDF (Portable Document Format) files in order of their occurrence on command line to one PDF result file.</p>
<dl>
<dt>Neither of the PDF-sourcefile1 to PDF-sourcefilen should be encrypted.</p>
<dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> Print copyright and version information.</p>
<dt><code>-h</code></p>
<dd> Print usage information. (<code>-help</code> and <code>&#8211;help</code> are equivalent.)</dl>
<h2>EXAMPLE</h2>
<p> pdfunite sample1.pdf sample2.pdf sample.pdf</p>
<dl>
<dt>merges all pages from sample1.pdf and sample2.pdf (in that order) and creates sample.pdf</p>
<dd></dl>
<h2>AUTHOR</h2>
<p> The pdfunite software and documentation are copyright 1996-2004 Glyph &amp; Cog, LLC and copyright 2005-2011 The Poppler Developers &#8211; <a rel="nofollow" href="http://poppler.freedesktop.org">http://poppler.freedesktop.org</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdfdetach/">pdfdetach</a></code>(1), <code><a href="/docs/linux/man/1-pdffonts/">pdffonts</a></code>(1), <code><a href="/docs/linux/man/1-pdfimages/">pdfimages</a></code>(1), <code><a href="/docs/linux/man/1-pdfinfo/">pdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-pdftocairo/">pdftocairo</a></code>(1), <code><a href="/docs/linux/man/1-pdftohtml/">pdftohtml</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1), <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdftotext/">pdftotext</a></code>(1) <code><a href="/docs/linux/man/1-pdfseparate/">pdfseparate</a></code>(1), <code><a href="/docs/linux/man/1-pdfsig/">pdfsig</a></code>(1) </p>
<h2>Index</h2>
