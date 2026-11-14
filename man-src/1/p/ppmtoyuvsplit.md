---
title: "ppmtoyuvsplit(1)"
name: "ppmtoyuvsplit"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtoyuvsplit/"
description: "ppmtoyuvsplit – convert a portable pixmap into 3 subsampled raw YUV files"
---

<h2 class="name">NAME</h2>
<p> ppmtoyuvsplit &#8211; convert a portable pixmap into 3 subsampled raw YUV files </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtoyuvsplit</code> <i>basename</i> [<i>ppmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input. Produces 3 raw files basename.Y, basename.U and basename.V as output. These files are the subsampled raw YUV representation of the input pixmap, as required by the Stanford MPEG codec. The subsampling is done by arithmetic mean of 4 pixels colors into one. The YUV values are scaled according to CCIR.601, as assumed by MPEG.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mpeg/">mpeg</a>(1), <a href="/docs/linux/man/5-ppm/">ppm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1993 by Andre Beck. (Andre_Beck [at] IRS.Inf.TU-Dresden.de) </p>
<p> Based on ppmtoyuv.c </p>
<h2>Index</h2>
