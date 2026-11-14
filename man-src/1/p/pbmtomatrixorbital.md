---
title: "pbmtomatrixorbital(1)"
name: "pbmtomatrixorbital"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmtomatrixorbital/"
description: "pbmtomatrixorbital – convert a PBM image to a Matrix Orbital LCD image"
---

<h2 class="name">NAME</h2>
<p> pbmtomatrixorbital &#8211; convert a PBM image to a Matrix Orbital LCD image</p>
<h2>SYNOPSIS</h2>
<p> <code>pbmtomatrixorbital</code> </p>
<p> [<i>pbmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pbmtomatrixorbital</code> reads a PBM image as input and produces as output an image that can be uploaded to a Matrix Orbital LCD display. </p>
<p> You can upload the image to the LCD via the serial port to which it is connected with the program <code>mo-upload.pl</code>, which you can get from the package <code>pbmtomatrixorbital</code>. Yes, the package is the same name as this Netpbm program, and it contains its own <code>pbmtomatrixorbital</code> program which is slightly different from this one because it is not part of the Netpbm package. </p>
<h2>HISTORY</h2>
<p> <code>pbmtomatrixorbital</code> was added to Netpbm in Release 10.18 (September 2003). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pbmtox10bm/">pbmtox10bm</a></code>(1) , <code><a href="/docs/linux/man/1-xbmtopbm/">xbmtopbm</a></code>(1) , <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1) </p>
<h2>Index</h2>
