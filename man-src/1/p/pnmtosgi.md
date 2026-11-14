---
title: "pnmtosgi(1)"
name: "pnmtosgi"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmtosgi/"
description: "pnmtosgi – convert a portable anymap to a SGI image file"
---

<h2 class="name">NAME</h2>
<p> pnmtosgi &#8211; convert a portable anymap to a SGI image file </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmtosgi</code> [<code>-verbatim</code>|<code>-rle</code>] [<code>-imagename</code> <i>Name</i>] [<code>pnmfile</code>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable anymap as input. Produces an SGI image file as output. The SGI image will be 2-dimensional (1 channel) for PBM and PGM input, and 3-dimensional (3 channels) for PPM.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-verbatim</code></p>
<dd> Write an uncompressed file.</p>
<dt><code>-rle (default)</code></p>
<dd> Write a compressed (run length encoded) file.</p>
<dt><code>-imagename name</code></p>
<dd> Write the string &quot;name&quot; into the imagename field of the header. The name string is limited to 79 characters. If no name is given, pnmtosgi writes &quot;no name&quot; into this field.</dl>
<h2>BUGS</h2>
<p> Probably.</p>
<h2>REFERENCES</h2>
<p> SGI Image File Format documentation (draft v0.95) by Paul Haeberli (paul [at] sgi.com). Available via ftp at sgi.com:graphics/SGIIMAGESPEC.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-pnm/">pnm</a>(5), <a href="/docs/linux/man/1-sgitopnm/">sgitopnm</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1994 by Ingo Wilken (Ingo.Wilken [at] informatik.uni-oldenburg.de) </p>
<h2>Index</h2>
