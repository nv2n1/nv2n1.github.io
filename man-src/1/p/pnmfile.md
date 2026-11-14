---
title: "pnmfile(1)"
name: "pnmfile"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmfile/"
description: "pnmfile – describe a portable anymap"
---

<h2 class="name">NAME</h2>
<p> pnmfile &#8211; describe a portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmfile</code> [<code>-allimages</code>] [<i>pnmfile &#8230;</i>] </p>
<h2>DESCRIPTION</h2>
<p> Reads one or more Netpbm files as input. Writes out short descriptions of the image type, size, etc. This is mostly for use in shell scripts, so the format is not particularly pretty. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-allimages</code></p>
<dd> Describe every image in each input file. Without this option, <code>pnmfile</code> describes only the first image in each input file. Note that before July 2000, a file could not contain more than one image and many programs ignore all but the first. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5), <code><a href="/docs/linux/man/1-file/">file</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
