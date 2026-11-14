---
title: "pdfattach(1)"
name: "pdfattach"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfattach/"
description: "pdfattach – Portable Document Format (PDF) document embedded file creator (version 3.03)"
---

<h2 class="name">NAME</h2>
<p> pdfattach &#8211; Portable Document Format (PDF) document embedded file creator (version 3.03) </p>
<h2>SYNOPSIS</h2>
<p> <code>pdfattach</code> [options] <i>input-PDF-file file-to-attach output-PDF-file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Pdfattach</code> adds a new embedded file (attachment) to an existing Portable Document Format (PDF) file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-replace</code></p>
<dd> Replace embedded file with same name (if it exists)</p>
<dt><code>-v</code></p>
<dd> Print copyright and version information.</p>
<dt><code>-h</code></p>
<dd> Print usage information. (<code>-help</code> and <code>&#8211;help</code> are equivalent.)</dl>
<h2>EXIT CODES</h2>
<dl>
<dt>0</p>
<dd> No error.</p>
<dt>1</p>
<dd> Error opening input PDF file.</p>
<dt>2</p>
<dd> Error opening file to attach.</p>
<dt>3</p>
<dd> Output file already exists.</p>
<dt>3</p>
<dd> There is already an attached file with that name.</p>
<dt>5</p>
<dd> Error saving the output file.</dl>
<h2>AUTHOR</h2>
<p> The pdfattach software and documentation are copyright 2019 The Poppler developers</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdfdetach/">pdfdetach</a></code>(1), <code><a href="/docs/linux/man/1-pdfimages/">pdfimages</a></code>(1), <code><a href="/docs/linux/man/1-pdfinfo/">pdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-pdftocairo/">pdftocairo</a></code>(1), <code><a href="/docs/linux/man/1-pdftohtml/">pdftohtml</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1), <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdftotext/">pdftotext</a></code>(1) <code><a href="/docs/linux/man/1-pdfseparate/">pdfseparate</a></code>(1), <code><a href="/docs/linux/man/1-pdfsig/">pdfsig</a></code>(1), <code><a href="/docs/linux/man/1-pdfunite/">pdfunite</a></code>(1) </p>
<h2>Index</h2>
