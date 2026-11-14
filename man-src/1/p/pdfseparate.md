---
title: "pdfseparate(1)"
name: "pdfseparate"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfseparate/"
description: "pdfseparate – Portable Document Format (PDF) page extractor"
---

<h2 class="name">NAME</h2>
<p> pdfseparate &#8211; Portable Document Format (PDF) page extractor </p>
<h2>SYNOPSIS</h2>
<p> <code>pdfseparate</code> [options] <i>PDF-file PDF-page-pattern</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pdfseparate</code> extract single pages from a Portable Document Format (PDF). </p>
<p> pdfseparate reads the PDF file <i>PDF-file</i>, extracts one or more pages, and writes one PDF file for each page to <i>PDF-page-pattern.</i> </p>
<p> PDF-page-pattern should contain <code>%d</code> (or any variant respecting printf format), since %d is replaced by the page number.</p>
<dl>
<dt>The PDF-file should not be encrypted.</p>
<dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code><i> number</i></p>
<dd> Specifies the first page to extract. If -f is omitted, extraction starts with page 1.</p>
<dt><code>-l</code><i> number</i></p>
<dd> Specifies the last page to extract. If -l is omitted, extraction ends with the last page.</p>
<dt><code>-v</code></p>
<dd> Print copyright and version information.</p>
<dt><code>-h</code></p>
<dd> Print usage information. (<code>-help</code> and <code>&#8211;help</code> are equivalent.)</dl>
<h2>EXAMPLE</h2>
<p> pdfseparate sample.pdf sample-%d.pdf</p>
<dl>
<dt>extracts all pages from sample.pdf, if i.e. sample.pdf has 3 pages, it produces</p>
<dd>
<dt>sample-1.pdf, sample-2.pdf, sample-3.pdf</p>
<dd></dl>
<h2>AUTHOR</h2>
<p> The pdfseparate software and documentation are copyright 1996-2004 Glyph &amp; Cog, LLC and copyright 2005-2011 The Poppler Developers &#8211; <a rel="nofollow" href="http://poppler.freedesktop.org">http://poppler.freedesktop.org</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdfdetach/">pdfdetach</a></code>(1), <code><a href="/docs/linux/man/1-pdffonts/">pdffonts</a></code>(1), <code><a href="/docs/linux/man/1-pdfimages/">pdfimages</a></code>(1), <code><a href="/docs/linux/man/1-pdfinfo/">pdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-pdftocairo/">pdftocairo</a></code>(1), <code><a href="/docs/linux/man/1-pdftohtml/">pdftohtml</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1), <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdftotext/">pdftotext</a></code>(1) <code><a href="/docs/linux/man/1-pdfsig/">pdfsig</a></code>(1), <code><a href="/docs/linux/man/1-pdfunite/">pdfunite</a></code>(1) </p>
<h2>Index</h2>
