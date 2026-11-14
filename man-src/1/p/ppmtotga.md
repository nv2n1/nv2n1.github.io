---
title: "ppmtotga(1)"
name: "ppmtotga"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtotga/"
description: "ppmtotga – convert portable pixmap into a TrueVision Targa file"
---

<h2 class="name">NAME</h2>
<p> ppmtotga &#8211; convert portable pixmap into a TrueVision Targa file </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtotga</code> [<code>-mono|-cmap|-rgb</code>] [<code>-norle</code>] [<i>ppmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input. Produces a TrueVision Targa file as output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-mono</code></p>
<dd> Forces Targa file to be of type 8 bit monochrome. Input must be a portable bitmap or a portable graymap.</p>
<dt><code>-cmap</code></p>
<dd> Forces Targa file to be of type 24 bit colormapped. Input must be a portable bitmap, a portable graymap or a portable pixmap containing no more than 256 distinct colors.</p>
<dt><code>-rgb</code></p>
<dd> Forces Targa file to be of type 24 bit unmapped color.</p>
<dt><code>-norle</code></p>
<dd> Disables run-length encoding, in case you have a Targa reader which can&#8217;t read run-length encoded files.</dl>
<p> All flags can be abbreviated to their shortest unique prefix. If no file type is specified the most highly constained compatible type is used, where monochrome is more constained than colormapped which is in turn more constained than unmapped.</p>
<h2>BUGS</h2>
<p> Does not support all possible Targa file types. Should really be in PNM, not PPM.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-tgatoppm/">tgatoppm</a>(1), <a href="/docs/linux/man/5-ppm/">ppm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989, 1991 by Mark Shand and Jef Poskanzer. </p>
<h2>Index</h2>
