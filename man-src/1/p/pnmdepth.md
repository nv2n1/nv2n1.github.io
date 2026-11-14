---
title: "pnmdepth(1)"
name: "pnmdepth"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmdepth/"
description: "pnmdepth – change the maxval in a portable anymap"
---

<h2 class="name">NAME</h2>
<p> pnmdepth &#8211; change the maxval in a portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmdepth</code> <i>newmaxval</i> [<i>pnmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable anymap as input. Scales all the pixel values, and writes out the image with the new maxval. Scaling the colors down to a smaller maxval will result in some loss of information. </p>
<p> Be careful of off-by-one errors when choosing the new maxval. For instance, if you want the color values to be five bits wide, use a maxval of 31, not 32. </p>
<p> One important use of <code>pnmdepth</code> is to convert a new format 2-byte-per-sample PNM file to the older 1-byte-per-sample format. Before April 2000, essentially all raw (binary) format PNM files had a maxval less than 256 and one byte per sample, and many programs may rely on that. If you specify a <i>newmaxval</i> less than 256, the resulting file should be readable by any program that worked with PNM files before April 2000. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-pnm/">pnm</a>(5), <a href="/docs/linux/man/1-ppmquant/">ppmquant</a>(1), <a href="/docs/linux/man/1-ppmdither/">ppmdither</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989, 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
