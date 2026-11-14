---
title: "pgmdeshadow(1)"
name: "pgmdeshadow"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgmdeshadow/"
description: "pgmdeshadow – Deshadow a PGM image"
---

<h2 class="name">NAME</h2>
<p> pgmdeshadow &#8211; Deshadow a PGM image</p>
<h2>SYNOPSIS</h2>
<p> <code>pgmdeshadow</code> </p>
<p> [<i>pnmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pgmdeshadow</code> removes gray shadows from an image. This is useful for an image containing text, such as a scanned book pages, where a shadow typically appears near the book crease or near one side of the image. <code>pgmdeshadow</code> recognizes a gray shadow as an area of smoothly changing color, starting from the outer edges of the image. The program uses a simple image reconstruction algorithm to determine the local shadow gray level, then divides each pixel&#8217;s gray level by the local shadow gray level. </p>
<p> The algorithm is the &#8216;fast hybrid grayscale reruction&#8217; algorithm from Luc Vincent, &quot;Morphological Grayscale Reruction in Image Analysis: Applications and Efficient Algorithms. </p>
<h2>OPTIONS</h2>
<p> None. </p>
<h2>REFERENCES</h2>
<dl>
<dt>&bull;</p>
<dd> Luc Vincent, &#8216;Morphological Grayscale Reruction in Image Analysis: Applications and Efficient Algorithms,&#8217; IEEE Transactions on Image Processing, vol. 2, no. 2, April 1993, pp. 176-201. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmshadow/">ppmshadow</a></code>(1) , <code><a href="/docs/linux/man/1-pgm/">pgm</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pgmdeshadow</code> was added to Netpbm in Version 10.35 (August 2006). </p>
<h2>Index</h2>
