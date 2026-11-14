---
title: "ppmdist(1)"
name: "ppmdist"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmdist/"
description: "ppmdist – simplistic grayscale assignment for machine generated, color images"
---

<h2 class="name">NAME</h2>
<p> ppmdist &#8211; simplistic grayscale assignment for machine generated, color images </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmdist</code> [<code>-intensity</code>|<code>-frequency</code>] [<i>ppmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input, performs a simplistic grayscale assignment intended for use with grayscale or bitmap printers. </p>
<p> Often conversion from ppm to pgm will yield an image with contrast too low for good printer output. The program maximizes contrast between the gray levels output. </p>
<p> A ppm input of n colors is read, and a pgm of n gray levels is written. The gray levels take on the values 0..n-1, while maxval takes on n-1. </p>
<p> The mapping from color to stepped grayscale can be performed in order of input pixel intensity, or input pixel frequency (number of repetitions).</p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dt><code>-frequency</code></p>
<dd>
<dd> Sort input colors by the number of times a color appears in the input, before mapping to evenly distributed graylevels of output. <code>-intensity</code> Sort input colors by their grayscale intensity, before mapping to evenly distributed graylevels of output. This is the default.</dl>
<h2>BUGS</h2>
<p> Helpful only for images with a very small number of colors. Perhaps should have been an option to <a href="/docs/linux/man/1-ppmtopgm/">ppmtopgm</a>(1).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ppmtopgm/">ppmtopgm</a>(1), <a href="/docs/linux/man/1-ppmhist/">ppmhist</a>(1), <a href="/docs/linux/man/5-ppm/">ppm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1993 by Dan Stromberg. </p>
<h2>Index</h2>
