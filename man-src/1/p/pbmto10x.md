---
title: "pbmto10x(1)"
name: "pbmto10x"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmto10x/"
description: "pbmto10x – convert a portable bitmap into Gemini 10X printer graphics"
---

<h2 class="name">NAME</h2>
<p> pbmto10x &#8211; convert a portable bitmap into Gemini 10X printer graphics </p>
<h2>SYNOPSIS</h2>
<p> <code>pbmto10x</code> [<code>-h</code>] [<i>pbmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable bitmap as input. Produces a file of Gemini 10X printer graphics as output. The 10x&#8217;s printer codes are alleged to be similar to the Epson codes. </p>
<p> Note that there is no 10xtopbm tool &#8211; this transformation is one way.</p>
<h2>OPTIONS</h2>
<p> The resolution is normally 60H by 72V. If the <code>-h</code> flag is specified, resolution is 120H by 144V. You may find it useful to rotate landscape images before printing.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-pbm/">pbm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1990 by Ken Yap </p>
<h2>Index</h2>
