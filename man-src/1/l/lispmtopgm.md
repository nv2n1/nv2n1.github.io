---
title: "lispmtopgm(1)"
name: "lispmtopgm"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lispmtopgm/"
description: "lispmtopgm – convert a Lisp Machine bitmap file into pgm format"
---

<h2 class="name">NAME</h2>
<p> lispmtopgm &#8211; convert a Lisp Machine bitmap file into pgm format </p>
<h2>SYNOPSIS</h2>
<p> <code>lispmtopgm</code> [<i>lispmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a Lisp Machine bitmap as input. Produces a portable graymap as output. </p>
<p> This is the file format written by the tv:write-bit-array-file function on TI Explorer and Symbolics lisp machines. </p>
<p> Multi-plane bitmaps on lisp machines are color; but the lispm image file format does not include a color map, so we must treat it as a graymap instead. This is unfortunate.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pgmtolispm/">pgmtolispm</a>(1), <a href="/docs/linux/man/5-pgm/">pgm</a>(5)</p>
<h2>BUGS</h2>
<p> The Lispm bitmap file format is a bit quirky; Usually the image in the file has its width rounded up to the next higher multiple of 32, but not always. If the width is not a multiple of 32, we don&#8217;t deal with it properly, but because of the Lispm microcode, such arrays are probably not image data anyway. </p>
<p> Also, the lispm code for saving bitmaps has a bug, in that if you are writing a bitmap which is not mod32 across, the file may be up to 7 bits too short! They round down instead of up, and we don&#8217;t handle this bug gracefully. </p>
<p> No color.</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Jamie Zawinski and Jef Poskanzer. </p>
<h2>Index</h2>
