---
title: "pbmtolps(1)"
name: "pbmtolps"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmtolps/"
description: "pbmtolps – convert PBM image to PostScript"
---

<h2 class="name">NAME</h2>
<p> pbmtolps &#8211; convert PBM image to PostScript</p>
<h2>SYNOPSIS</h2>
<p> <code>pbmtolps</code> [<code>-dpi</code> <i>n</i>] [<i>pbmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pbmtolps</code> reads a PBM image as input and outputs PostScript. The output Postscript uses lines instead of the image operator to generate a (device dependent) picture which will be imaged much faster. </p>
<p> The Postscript path length is constrained to be less that 1000 points so that no limits are overrun on the Apple Laserwriter and (presumably) no other printers. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmtops/">pnmtops</a></code>(1) , <code><a href="/docs/linux/man/1-pstopnm/">pstopnm</a></code>(1) , <code><a href="/docs/linux/man/1-pbmtoepsi/">pbmtoepsi</a></code>(1) , <code><a href="/docs/linux/man/1-psidtopgm/">psidtopgm</a></code>(1) , <code>gs</code>, <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1) , </p>
<h2>AUTHOR</h2>
<p> George Phillips &lt;<i>phillips [at] cs.ubc.ca</i>&gt; </p>
<h2>Index</h2>
