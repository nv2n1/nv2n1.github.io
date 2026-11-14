---
title: "ppmtopgm(1)"
name: "ppmtopgm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtopgm/"
description: "ppmtopgm – convert a portable pixmap into a portable graymap"
---

<h2 class="name">NAME</h2>
<p> ppmtopgm &#8211; convert a portable pixmap into a portable graymap </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtopgm</code> [<i>ppmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input. Produces a portable graymap as output. The output is a &quot;black and white&quot; rendering of the original image, as in a black and white photograph. The quantization formula used is .299 r + .587 g + .114 b. </p>
<p> Note that although there is a <code>pgmtoppm</code> program, it is not necessary for simple conversions from pgm to ppm , because any ppm program can read pgm (and pbm ) files automatically. <code>pgmtoppm</code> is for colorizing a pgm file. Also, see <code>ppmtorgb3</code> for a different way of converting color to gray. And <code>ppmdist </code> generates a grayscale image from a color image, but in a way that makes it easy to differentiate the original colors, not necessarily a way that looks like a black and white photograph. </p>
<h2>QUOTE</h2>
<pre>
Cold-hearted orb that rules the night
Removes the colors from our sight
Red is gray, and yellow white
But we decide which is right
And which is a quantization error.
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pgmtoppm/">pgmtoppm</a></code>(1),<code><a href="/docs/linux/man/1-ppmtorgb3/">ppmtorgb3</a></code>(1),<code><a href="/docs/linux/man/1-rgb3toppm/">rgb3toppm</a></code>(1),<code><a href="/docs/linux/man/1-ppmdist/">ppmdist</a></code>(1),<code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5),<code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Jef Poskanzer. </p>
<h2>Index</h2>
