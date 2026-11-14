---
title: "ppmdither(1)"
name: "ppmdither"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmdither/"
description: "ppmdither – ordered dither for color images"
---

<h2 class="name">NAME</h2>
<p> ppmdither &#8211; ordered dither for color images </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmdither</code> [<code>-dim</code> <i>power</i>] [<code>-red</code> <i>shades</i>] [<code>-green</code> <i>shades</i>] [<code>-blue</code> <i>shades</i>] [<i>ppmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input, and applies dithering to it to reduce the number of colors used down to the specified number of shades for each primary. The default number of shades is red=5, green=9, blue=5, for a total of 225 colors. To convert the image to a binary rgb format suitable for color printers, use -red 2 -green 2 -blue 2. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-dim</code><i> power</i></p>
<dd> The size of the dithering matrix. The dithering matrix is a square whose dimension is a power of 2. <i>power</i> is that power of 2. The default is 4, for a 16 by 16 matrix.</p>
<dt><code>-red</code><i> shades</i></p>
<dd> The number of red shades to be used, including black; minimum of 2.</p>
<dt><code>-green</code><i> shades</i></p>
<dd> The number of green shades to be used, including black; minimum of 2.</p>
<dt><code>-blue</code><i> shades</i></p>
<dd> The number of blue shades to be used, including black; minimum of 2.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pnmdepth/">pnmdepth</a>(1), <a href="/docs/linux/man/1-ppmquant/">ppmquant</a>(1), <a href="/docs/linux/man/5-ppm/">ppm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Christos Zoulas. </p>
<h2>Index</h2>
