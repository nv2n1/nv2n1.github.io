---
title: "hyperxmp-add-bytecount(1)"
name: "hyperxmp-add-bytecount"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hyperxmp-add-bytecount/"
description: "hyperxmp-add-bytecount – adds/updates byteCount specification in XMP packet in PDF file."
---

<h2>SYNOPSIS</h2>
<p> <code>hyperxmp-add-bytecount</code> [<i>options</i>] <i>filename.pdf</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>hyperxmp-add-bytecount</code> adds/updates the byteCount specification in the XMP packet in a PDF file(s), with byteCount = file size. The XMP packet needs to be of, or compatible with, the format produced from a document that uses the LaTeX hyperxmp package </p>
<p> If no XMP packet of a compatible form is found in the PDF file, no change is made to the file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></dt>
<dd> Write usage summary and exit.</dd>
<dt><code>-version</code></dt>
<dd> Output version information and exit.</dd></dl>
<h2>BUGS</h2>
<p> Email bug reports to John Collins and/or Scott Pakin </p>
