---
title: "pgmedge(1)"
name: "pgmedge"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgmedge/"
description: "pgmedge – edge-detect a portable graymap"
---

<h2 class="name">NAME</h2>
<p> pgmedge &#8211; edge-detect a portable graymap</p>
<h2>SYNOPSIS</h2>
<p> <code>pgmedge</code> [<i>pgmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> Reads a portable graymap as input. Outlines the edges, and writes a portable graymap as output. Piping the result through <code>pgmtopbm -threshold</code> and playing with the threshold value will give a bitmap of the edges. </p>
<p> The edge detection technique used is to take the Pythagorean sum of two Sobel gradient operators at 90 degrees to each other. For more details see &quot;Digital Image Processing&quot; by Gonzalez and Wintz, chapter 7. </p>
<p> The maxval of the output is the same as the maxval of the input The effect is better with larger maxvals, so you may want to increase the maxval of the input by running it through <code>pnmdepth</code> first. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pgmenhance/">pgmenhance</a></code>(1), <code><a href="/docs/linux/man/1-pgmtopbm/">pgmtopbm</a></code>(1), <code><a href="/docs/linux/man/1-pnmdepth/">pnmdepth</a></code>(1), <code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5), <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
