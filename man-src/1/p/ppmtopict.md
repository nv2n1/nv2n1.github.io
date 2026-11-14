---
title: "ppmtopict(1)"
name: "ppmtopict"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtopict/"
description: "ppmtopict – convert a portable pixmap into a Macintosh PICT file"
---

<h2 class="name">NAME</h2>
<p> ppmtopict &#8211; convert a portable pixmap into a Macintosh PICT file </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtopict</code> [<i>ppmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input. Produces a Macintosh PICT file as output. </p>
<p> The generated file is only the data fork of a picture. You will need a program such as <i>mcvert</i> to generate a Macbinary or a BinHex file that contains the necessary information to identify the file as a PICT file to MacOS. </p>
<p> Even though PICT supports 2 and 4 bits per pixel, <i>ppmtopict</i> always generates an 8 bits per pixel file.</p>
<h2>BUGS</h2>
<p> The picture size field is only correct if the output is to a file since writing into this field requires seeking backwards on a file. However the PICT documentation seems to suggest that this field is not critical anyway since it is only the lower 16 bits of the picture size.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-picttoppm/">picttoppm</a>(1), <a href="/docs/linux/man/5-ppm/">ppm</a>(5), <a href="/docs/linux/man/1-mcvert/">mcvert</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1990 by Ken Yap &lt;ken [at] cs.rocester.edu&gt;. </p>
<h2>Index</h2>
