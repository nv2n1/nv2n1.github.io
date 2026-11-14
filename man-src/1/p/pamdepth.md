---
title: "pamdepth(1)"
name: "pamdepth"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamdepth/"
description: "pamdepth – change the maxval in a Netpbm image"
---

<h2 class="name">NAME</h2>
<p> pamdepth &#8211; change the maxval in a Netpbm image</p>
<h2>SYNOPSIS</h2>
<p> <code>pamdepth</code> <i>newmaxval</i> [<i>netpbmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamdepth</code> reads a Netpbm image as input, scales all the pixel values, and writes out the image with the new maxval. Scaling the colors down to a smaller maxval will result in some loss of information. </p>
<p> This program works on multi-image streams. </p>
<p> Be careful of off-by-one errors when choosing the new maxval. For instance, if you want the color values to be five bits wide, use a maxval of 31, not 32. </p>
<p> One important use of <code>pamdepth</code> is to convert a new format 2-byte-per-sample PNM file to the older 1-byte-per-sample format. Before April 2000, essentially all raw (binary) format PNM files had a maxval less than 256 and one byte per sample, and many programs may rely on that. If you specify a <i>newmaxval</i> less than 256, the resulting file should be readable by any program that worked with PNM files before April 2000. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , <code><a href="/docs/linux/man/1-pnmquant/">pnmquant</a></code>(1) , <code><a href="/docs/linux/man/1-ppmdither/">ppmdither</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-ppmbrighten/">ppmbrighten</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pamfunc/">pamfunc</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamdepth</code> was new in Netpbm 10.32 (February 2006). It replaced <code>pnmdepth</code>, by Jef Poskanzer. <code>pamdepth</code> is backward compatible with <code>pnmdepth</code> and adds the ability to process arbitrary PAM images and the ability to process multi-image input streams. <code>pnmdepth</code> handled only PNM images and ignored all but the first in any stream. </p>
<h2>Index</h2>
