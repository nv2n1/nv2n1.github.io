---
title: "pamedge(1)"
name: "pamedge"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamedge/"
description: "pamedge – edge-detect an image"
---

<h2 class="name">NAME</h2>
<p> pamedge &#8211; edge-detect an image</p>
<h2>SYNOPSIS</h2>
<p> <code>pamedge</code> [<i>imagefile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamedge</code> reads a Netpbm image (PNM or PAM) and produces an image that outlines the edges. </p>
<p> The output image is of the same type as the input, except that the maxval of the output is at least 255 and if the input is PBM, the output is PGM. </p>
<p> You can pipe the result through <tt>pamditherbw -threshold</tt> and play with the threshold value to get a PBM (bilevel image) of the edges. </p>
<p> The edge detection technique used is to take the Pythagorean sum of two Sobel gradient operators at 90 degrees to each other. For more details see &#8216;Digital Image Processing&#8217; by Gonzalez and Wintz, chapter 7. </p>
<p> The maxval of the output is the same as the maxval of the input, except at least 255. The effect is better with larger maxvals, so you may want to increase the maxval of the input by running it through <code>pamdepth</code> first. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pgmenhance/">pgmenhance</a></code>(1) , <code><a href="/docs/linux/man/1-pamditherbw/">pamditherbw</a></code>(1) , <code><a href="/docs/linux/man/1-pamdepth/">pamdepth</a></code>(1) , <code><a href="/docs/linux/man/1-pammasksharpen/">pammasksharpen</a></code>(1) , <code><a href="/docs/linux/man/1-pamsharpness/">pamsharpness</a></code>(1) , <code><a href="/docs/linux/man/1-pamsharpmap/">pamsharpmap</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamedge</code> was added to Netpbm in Release 10.14 (March 2003). It replaced <code>pgmedge</code>, which was the same thing, but worked only on PGM and PBM images. </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Jef Poskanzer. Adapted to <code>pnmedge</code> Peter Kichgessner in 1995, and then to <code>pamedge</code> by Bryan Henderson in 2003. </p>
<h2>Index</h2>
