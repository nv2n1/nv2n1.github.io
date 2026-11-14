---
title: "pamsharpness(1)"
name: "pamsharpness"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamsharpness/"
description: "pamsharpness – measure the sharpness of a PNM/PAM image"
---

<h2 class="name">NAME</h2>
<p> pamsharpness &#8211; measure the sharpness of a PNM/PAM image</p>
<h2>SYNOPSIS</h2>
<p> <code>pamsharpness</code> [<i>imagefile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamsharpness</code> reads a Netpbm image (PNM or PAM) and prints a number that tells how sharp it is. </p>
<p> Sharpness is a measure of how suddenly (in space) colors change in the image. <code>pamsharpness</code> computes the sharpness of the image as the average difference in intensity between each pixel and its 8 surrounding pixels, in each of the color components (R, G, B). </p>
<p> <code>pamsharpness</code> does not include the edges of the image, where there are not 8 pixels surrounding a pixel, in its computation. </p>
<p> <code>pamsharpness</code> assumes that the image is a PNM or PNM equivalent PAM. If it isn&#8217;t, the results are not necessarily meaningful. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamsharpmap/">pamsharpmap</a></code>(1) , <code><a href="/docs/linux/man/1-pammasksharpen/">pammasksharpen</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamsharpness</code> was added to Netpbm in Release 10.21 (March 2004). Bryan Henderson derived it from the program <code>pnmsharp</code> by B.W. van Schooten and distributed as part of the Photopnmtools package. </p>
<h2>Index</h2>
