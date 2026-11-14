---
title: "gemtopnm(1)"
name: "gemtopnm"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gemtopnm/"
description: "gemtopnm – convert a GEM .img file into a portable anymap"
---

<h2 class="name">NAME</h2>
<p> gemtopnm &#8211; convert a GEM .img file into a portable anymap</p>
<h2>SYNOPSIS</h2>
<p> <code>gemtopnm</code> [<code>-d</code>] [<i>gemfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a GEM .img file, either the one plane (black/white) or four plane (16 color) varieety, as input. Reads from stdin if input file is omitted. Produces a PBM or PPM file as output, depending on whether the input is one or four plane.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code></p>
<dd> Produce output describing the contents of the .img file. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pbmtogem/">pbmtogem</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1988 Diomidis D. Spinellis (dds [at] cc.ic.ac.uk). </p>
<h2>Index</h2>
