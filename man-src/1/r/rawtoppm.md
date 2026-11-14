---
title: "rawtoppm(1)"
name: "rawtoppm"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rawtoppm/"
description: "rawtoppm – convert raw RGB bytes into a portable pixmap"
---

<h2 class="name">NAME</h2>
<p> rawtoppm &#8211; convert raw RGB bytes into a portable pixmap </p>
<h2>SYNOPSIS</h2>
<p> <code>rawtoppm</code> [<code>-headerskip</code> <i>N</i>] [<code>-rowskip</code> <i>N</i>] [<code>-rgb</code>|<code>-rbg</code>|<code>-grb</code> |<code>-gbr</code>|<code>-brg</code>|<code>-bgr</code> ] [<code>-interpixel</code>|<code>-interrow</code>] <i>width height</i> [<i>imagedata</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads raw RGB bytes as input. Produces a portable pixmap as output. The input file is just RGB bytes. You have to specify the width and height on the command line, since the program obviously can&#8217;t get them from the file. The maxval is assumed to be 255. If the resulting image is upside down, run it through <code>pnmflip -tb .</code></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-headerskip</code></p>
<dd> If the file has a header, you can use this flag to skip over it.</p>
<dt><code>-rowskip</code></p>
<dd> If there is padding at the ends of the rows, you can skip it with this flag.</p>
<dt><code>-rgb -rbg -grb -gbr -brg -bgr</code></p>
<dd> These flags let you specify alternate color orders. The default is <code>-rgb</code>.</p>
<dt><code>-interpixel -interrow</code></p>
<dd> These flags let you specify how the colors are interleaved. The default is <code>-interpixel</code>, meaning interleaved by pixel. A byte of red, a byte of green, and a byte of blue, or whatever color order you specified. <code>-interrow</code> means interleaved by row &#8211; a row of red, a row of green, a row of blue, assuming standard rgb color order. An <code>-interplane</code> flag &#8211; all the red pixels, then all the green, then all the blue &#8211; would be an obvious extension, but is not implemented. You could get the same effect by splitting the file into three parts (perhaps using <i>dd</i>), turning each part into a PGM file with rawtopgm, and then combining them with rgb3toppm.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-ppm/">ppm</a>(5), <a href="/docs/linux/man/1-rawtopgm/">rawtopgm</a>(1), <a href="/docs/linux/man/1-rgb3toppm/">rgb3toppm</a>(1), <a href="/docs/linux/man/1-pnmflip/">pnmflip</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
