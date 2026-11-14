---
title: "yuvtoppm(1)"
name: "yuvtoppm"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yuvtoppm/"
description: "yuvtoppm – convert Abekas YUV bytes into a portable pixmap"
---

<h2 class="name">NAME</h2>
<p> yuvtoppm &#8211; convert Abekas YUV bytes into a portable pixmap </p>
<h2>SYNOPSIS</h2>
<p> <code>yuvtoppm</code> <i>width height</i> [<i>imagedata</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads raw Abekas YUV bytes as input. Produces a portable pixmap as output. The input file is just YUV bytes. You have to specify the width and height on the command line, since the program obviously can&#8217;t get them from the file. The maxval is assumed to be 255.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ppmtoyuv/">ppmtoyuv</a>(1), <a href="/docs/linux/man/5-ppm/">ppm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Marc Boucher &lt;marc [at] PostImage.COM&gt;, based on Example Conversion Program, A60/A64 Digital Video Interface Manual, page 69. </p>
<p> Copyright (C) 1991 by DHD PostImage Inc. </p>
<p> Copyright (C) 1987 by Abekas Video Systems Inc. </p>
<h2>Index</h2>
