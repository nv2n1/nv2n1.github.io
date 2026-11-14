---
title: "ppmtoeyuv(1)"
name: "ppmtoeyuv"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtoeyuv/"
description: "ppmtoeyuv – convert a portable pixmap into a Berkeley YUV file"
---

<h2 class="name">NAME</h2>
<p> ppmtoeyuv &#8211; convert a portable pixmap into a Berkeley YUV file </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtoeyuv</code> [<i>ppmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input. Produces a Berkeley Encoder YUV (not the same as Abekas YUV) file on the Standard Output file. </p>
<p> With no argument, takes input from Standard Input. Otherwise, <i>ppmfile </i> is the file specification of the input file. </p>
<p> <code>ppmtoeyuv</code> handles multi-image PPM input streams, outputting consecutive eyuv images. There must be at least one image, though. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-eyuvtoppm/">eyuvtoppm</a></code>(1), <code><a href="/docs/linux/man/1-ppmtoyuv/">ppmtoyuv</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) </p>
<h2>Index</h2>
