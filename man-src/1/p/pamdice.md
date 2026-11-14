---
title: "pamdice(1)"
name: "pamdice"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamdice/"
description: "pamdice – slice a Netpbm image into many horizontally and/or vertically"
---

<h2 class="name">NAME</h2>
<p> pamdice &#8211; slice a Netpbm image into many horizontally and/or vertically</p>
<h2>SYNOPSIS</h2>
<p> <code>pamslice</code> <code>-outstem=</code><i>filenamestem</i> [<code>-width=</code><i>width</i>] [<code>-height=</code><i>height</i>] [<code>-verbose</code>] [<i>filename</i>] </p>
<p> You can use the minimum unique abbreviation of the options. You can use two hyphens instead of one. You can separate an option name from its value with white space instead of an equals sign. </p>
<h2>DESCRIPTION</h2>
<p> Reads a PAM, PBM, PGM, or PPM image as input. Splits it horizontally and/or vertically into equal size pieces and writes them into separate files as the same kind of image. </p>
<p> See the <code>-outstem</code> option for information on naming of the output files. </p>
<p> The <code>-width</code> and <code>-height</code> options determine the size of the output pieces. </p>
<p> <code>pnmcat</code> can rejoin the images. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-outstem=</code>filenamestem</p>
<dd> This option determines the names of the output files. Each output file is named <i>filenamestem</i><code>_</code><i>y</i><code>_</code><i>x</i><code>.</code><i>type</i> where <i>filenamestem</i> is the value of the <code>-outstem</code> option, <i>x</i> and y are the horizontal and vertical locations, respectively, in the input image of the output image, zero being the leftmost and top, and <i>type</i> is <code>.pbm</code>, <code>.pgm</code>, <code>.ppm</code>, or <code>.pam</code>, depending on the type of image. </p>
<dt><code>-width=</code><i>width</i></p>
<dd> gives the width in pixels of the output images. The rightmost pieces are smaller than this if the input image is not a multiple of <i>width </i> pixels wide. </p>
<dt><code>-height=</code><i>height</i></p>
<dd> gives the height in pixels of the output images. The bottom pieces are smaller than this if the input image is not a multiple of <i>height </i> pixels high. </p>
<dt><code>-verbose</code></p>
<dd> Print information about the processing to Standard Error. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamcut/">pamcut</a></code>(1), <code><a href="/docs/linux/man/1-pnmcat/">pnmcat</a></code>(1), <code><a href="/docs/linux/man/1-pgmslice/">pgmslice</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> put by Bryan Henderson in the public domain in 2001 </p>
<h2>Index</h2>
