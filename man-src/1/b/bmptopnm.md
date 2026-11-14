---
title: "bmptopnm(1)"
name: "bmptopnm"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bmptopnm/"
description: "bmptopnm – convert a BMP file into a portable anymap"
---

<h2 class="name">NAME</h2>
<p> bmptopnm &#8211; convert a BMP file into a portable anymap</p>
<h2>SYNOPSIS</h2>
<p> <code>bmptopnm</code> [<i>bmpfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> Reads a Microsoft Windows or OS/2 BMP file as input. Produces a PBM, PGM, or PNM image as output. If the input is colormapped and contains only black and white, the output is PBM. If the input is colormapped and contains only black white and gray, the output is PGM. Otherwise, the output is PPM. </p>
<p> This program cannot convert BMP files with compressed (run length encoded) image data. It recognizes the compression and issues an error message. </p>
<p> This program cannot convert BMP files with 16 bits per pixel (only because the author did not have a complete specification for them). It recognizes the format and issues an error message. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmtobmp/">ppmtobmp</a></code>(1), <code><a href="/docs/linux/man/1-ppmtowinicon/">ppmtowinicon</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1992 by David W. Sanderson. </p>
<h2>Index</h2>
