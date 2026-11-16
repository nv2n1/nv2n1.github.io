---
title: "pbmtolj(1)"
name: "pbmtolj"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmtolj/"
description: "pbmtolj – convert a portable bitmap into HP LaserJet format"
---

<h2 class="name">NAME</h2>
<p> pbmtolj &#8211; convert a portable bitmap into HP LaserJet format</p>
<h2>SYNOPSIS</h2>
<p> <code>pbmtolj</code> [<code>-resolution</code> <i>N</i>] [<code>-float</code>] [<code>-noreset</code>] [<code>-packbits</code>] [<code>-delta</code>] [<code>-compress</code>] [<i>pbmfile</i>] [<code>-copies</code> <i>N</i>] </p>
<h2>DESCRIPTION</h2>
<p> Reads a PBM image as input. Produces HP LaserJet data as output. </p>
<p> Note that there is no ljtopbm tool. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-resolution</code></dt>
<dd> Specifies the resolution of the output device, in dpi. Typical values are 75, 100, 150, 300, and 600. The default is 75.</dd>
<dt><code>-float</code></dt>
<dd> Suppresses positioning information. The default is to write the sequence <i>ESC &amp; l 0 E</i> to the output file.</dd>
<dt><code>-noreset</code></dt>
<dd> Prevents pbmtolj from writing the reset sequences to the beginning and end of the output file.</dd>
<dt><code>-packbits</code></dt>
<dd> Enables use of TIFF packbits compression.</dd>
<dt><code>-delta</code></dt>
<dd> Enables use of delta-between-rows compression.</dd>
<dt><code>-compress</code></dt>
<dd> Enables use of both TIFF packbits, and delta-between-rows compression.</dd>
<dt><code>-copies</code></dt>
<dd> Specifies the the number of copies. The default is 1. This option controls the &quot;number of copies&quot; printer control; <code>pbmtolj</code> generates only one copy of the image.</dd></dl>
<p> All flags can be abbreviated to their shortest unique prefix. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1988 by Jef Poskanzer and Michael Haberler. <code>-float</code> and <code>-noreset</code> options added by Wim Lewis. <code>-delta, -packbits,</code> and <code>-compress</code> options added by Dave Platt. </p>
<h2>Index</h2>
