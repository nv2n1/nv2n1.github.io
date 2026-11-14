---
title: "pbmtobbnbg(1)"
name: "pbmtobbnbg"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmtobbnbg/"
description: "pbmtobbnbg – convert a portable bitmap into BitGraph graphics"
---

<h2 class="name">NAME</h2>
<p> pbmtobbnbg &#8211; convert a portable bitmap into BitGraph graphics </p>
<h2>SYNOPSIS</h2>
<p> <code>pbmtobbnbg</code> [<i>rasterop</i>] [<i>x</i> <i>y</i>] &lt; <i>pbmfile</i></p>
<h2>DESCRIPTION</h2>
<p> Reads a portable bitmap as input. Produces BBN BitGraph terminal Display Pixel Data (DPD) sequence as output. </p>
<p> The rasterop can be specified on the command line. If this is omitted, 3 (replace) will be used. A position in (x,y) coordinates can also be specified. If both are given, the rasterop comes first. The portable bitmap is always taken from the standard input. </p>
<p> Note that there is no bgtopbm tool. </p>
<p> This programm was initially named pbmtobg.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-pbm/">pbm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright 1989 by Mike Parker. </p>
<h2>Index</h2>
