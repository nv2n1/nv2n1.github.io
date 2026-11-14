---
title: "pamsharpmap(1)"
name: "pamsharpmap"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamsharpmap/"
description: "pamsharpmap – create map of sharpness in a PNM/PAM image"
---

<h2 class="name">NAME</h2>
<p> pamsharpmap &#8211; create map of sharpness in a PNM/PAM image</p>
<h2>SYNOPSIS</h2>
<p> <code>pamsharpmap</code> [<i>imagefile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamsharpmap</code> reads a Netpbm image (PNM or PAM) and produces an image that shows how sharp it is at each location. </p>
<p> Sharpness is a measure of how suddenly (in space) colors change in the image. <code>pamsharpmap</code> computes the sharpness of each component color (R, G, B) separately and produces a pixel whose intensity of each component color is directly proportional to the sharpness of that component color at the same location in the input image. Thus, at a point where the image is very sharp in its red and green components, but dull in its blue component, you will see a yellow pixel in the output. </p>
<p> <code>pamsharpmap</code> computes sharpness at a point simply as the average difference in intensity between the pixel at that point and the 8 pixels surrounding it. </p>
<p> At the edges of the image, where there are not 8 pixels surrounding a pixel, <code>pamsharpmap</code> assumes the image is extended with a black border. </p>
<p> <code>pamsharpmap</code> assumes that the image is a PNM or PNM equivalent PAM. If it isn&#8217;t, the results are not necessarily meaningful. </p>
<p> The output image is the same dimensions, depth, and tuple type as the input, and has maxval 255. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamsharpness/">pamsharpness</a></code>(1) , <code><a href="/docs/linux/man/1-pammasksharpen/">pammasksharpen</a></code>(1) , <code><a href="/docs/linux/man/1-pamedge/">pamedge</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamsharpmap</code> was added to Netpbm in Release 10.21 (March 2004). Bryan Henderson derived it from the program <code>pnmsharp</code> by B.W. van Schooten and distributed as part of the Photopnmtools package. </p>
<h2>Index</h2>
