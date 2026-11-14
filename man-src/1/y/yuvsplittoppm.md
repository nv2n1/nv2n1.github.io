---
title: "yuvsplittoppm(1)"
name: "yuvsplittoppm"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yuvsplittoppm/"
description: "yuvsplittoppm – convert a Y- and a U- and a V-file into a portable pixmap"
---

<h2 class="name">NAME</h2>
<p> yuvsplittoppm &#8211; convert a Y- and a U- and a V-file into a portable pixmap </p>
<h2>SYNOPSIS</h2>
<p> <code>yuvsplittoppm </code> <i>basename width height</i> [-ccir601]</p>
<h2>DESCRIPTION</h2>
<p> Reads three files, containing the YUV components, as input. These files are <i>basename</i>.Y, <i>basename</i>.U, and <i>basename</i>.V. Produces a portable pixmap on stdout. </p>
<p> Since the YUV files are raw files, the dimensions <i>width</i> and <i>height</i> must be specified on the command line.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-ccir601</code></p>
<dd> Assumes that the YUV triplets are scaled into the smaller range of the CCIR 601 (MPEG) standard. Else, the JFIF (JPEG) standard is assumed.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ppmtoyuvsplit/">ppmtoyuvsplit</a>(1), <a href="/docs/linux/man/1-yuvtoppm/">yuvtoppm</a>(1), <a href="/docs/linux/man/5-ppm/">ppm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Marcel Wijkstra &lt;wijkstra [at] fwi.uva.nl&gt;, based on <i>ppmtoyuvsplit.</i> </p>
<h2>Index</h2>
