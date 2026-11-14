---
title: "spottopgm(1)"
name: "spottopgm"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spottopgm/"
description: "spottopgm – convert SPOT satellite images to a PGM image"
---

<h2 class="name">NAME</h2>
<p> spottopgm &#8211; convert SPOT satellite images to a PGM image</p>
<h2>SYNTAX</h2>
<p> <code>spottopgm</code> [<code>-1</code>|<code>-2</code>|<code>-3</code>] [<i>Firstcol</i> <i>Firstline</i> <i>Lastcol</i> <i>Lastline</i>] <i>inputfile</i> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-1</code></p>
<dd>
<dt><code>-2</code></p>
<dd>
<dt><code>-3</code></p>
<dd> Extract the given color from the SPOT image. The colors are infrared, visible light, and ultraviolet, although I don&#8217;t know which corresponds to which number. If the image is in color, <code>spottopgm</code> announces this on Standard Error. The default color is 1. </p>
</dl>
<h2>PARAMETERS</h2>
<dl>
<dt><i>Firstcol Firstline Lastcol Lastline</i></p>
<dd> Extract the specified rectangle from the SPOT image. Most SPOT images are 3000 lines long and 3000 or more columns wide. Unfortunately, the SPOT format only gives the width and not the length. The width is printed on standard error. The default rectangle is the width of the input image by 3000 lines. </p>
</dl>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>spottopgm</code> converts the named <code>inputfile</code> to PGM format, defaulting to the first color and the whole SPOT image unless you specify otherwise with the options. </p>
<h2>LIMITATIONS</h2>
<p> <code>spottopgm</code> doesn&#8217;t determine the length of the input file; this would involve two passes over the input file. It defaults to 3000 lines instead. </p>
<p> <code>spottopgm</code> could extract a three-color image (as a PPM), but I didn&#8217;t feel like making the program more complicated than it is now. Besides, there is no one-to-one correspondence between red, green, blue and infrared, visible and ultraviolet. </p>
<p> I&#8217;ve had only a limited number of SPOT images to play with, and therefore wouldn&#8217;t guarantee that this will work on any other images. </p>
<h2>AUTHOR</h2>
<p> Warren Toomey <i>wkt [at] csadfa.cs.adfa.oz.au</i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pgm/">pgm</a></code>(1) </p>
<h2>Index</h2>
