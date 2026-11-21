---
title: "psorder(1)"
name: "psorder"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psorder/"
description: "psorder – PostScript pageorder filter"
---

<h2 class="name">NAME</h2>
<p> psorder &#8211; PostScript pageorder filter </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>psorder</code> [-duf] <i>sourcefile</i></dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>psorder</code></p>
<dd>is a filter that re-orders the pages of a PostScript document. The result is written to the standard output. By default, documents are processed into ascending order (the lowest numbered page is printed first). Some PostScript documents specify that the order of their pages should never be changed; the default action of <code>psorder</code> is to follow this specification. </dd>
<p> If no source file is given, or if <i>sourcefile</i> is `<code>&#8211;</code>&#8216;, <code>psorder</code> reads from the standard input file.</p>
<h2>OPTIONS</h2>
<p> <code>-d</code></p>
<dl>
<dt>
</dt><dd> Re-order the pages of the document in downward or descending order. This is typically used to change the order of a document to be printed by a printer that stacks pages face-up, such as an Apple LaserWriter or LaserWriter Plus.</dd></dl>
<p> <code>-u</code></p>
<dl>
<dt>
</dt><dd> Specifies forward order, and is the default. It is used to try and ensure the correct ordering when a document will be printed by a printer that stacks the pages face-down.</dd></dl>
<p> <code>-f</code></p>
<dl>
<dt>
</dt><dd> Force <code>psorder</code> to re-order the pages, even if the document claims that its page order is not to be trifled with. This option should only be used experimentally, as it may cause documents to print incorrectly.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-psf/">psf</a></code>(8), <code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1). </p>
