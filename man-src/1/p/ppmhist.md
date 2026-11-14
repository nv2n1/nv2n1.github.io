---
title: "ppmhist(1)"
name: "ppmhist"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmhist/"
description: "ppmhist – print a histogram of a portable pixmap"
---

<h2 class="name">NAME</h2>
<p> ppmhist &#8211; print a histogram of a portable pixmap</p>
<h2>SYNOPSIS</h2>
<p> <code>ppmhist</code> [<code>-hexcolor</code>] [<code>-noheader</code>] [<code>-map</code>] [<code>-nomap</code>] [<code>-sort=</code>{<code>frequency</code>,<code>rgb</code>}] [<i>ppmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> Reads a PPM image as input. Generates a histogram of the colors in the image, i.e. a list of all the colors and how many pixels of each color are in the image. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-sort=</code>{<code>frequency</code>,<code>rgb</code>}</p>
<dd> The <code>-sort</code> option determines the order in which the colors are listed in the output. <code>frequency </code> means to list them in order of how pixels in the input image have the color, with the most represented colors first. <code>rgb</code> means to sort them first by the intensity of the red component of the color, the of the green, then of the blue, with the least intense first. </p>
<p> The default is <code>frequency</code>. </p>
<dt><code>-hexcolor</code></p>
<dd> Print the color components in hexadecimal. Default is decimal.</p>
<dt><code>-noheader</code></p>
<dd> Do not print the column headings.</p>
<dt><code>-map</code></p>
<dd> Generates a PPM file of the colormap for the image, with the color histogram as comments.</p>
<dt><code>-nomap</code></p>
<dd> Generates the histogram for human reading. This is the default. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5), <code><a href="/docs/linux/man/1-pgmhist/">pgmhist</a></code>(1), <code><a href="/docs/linux/man/1-ppmtomap/">ppmtomap</a></code>(1), <code><a href="/docs/linux/man/1-pnmhistmap/">pnmhistmap</a></code>(1), <code><a href="/docs/linux/man/1-ppmchange/">ppmchange</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Jef Poskanzer. </p>
<h2>Index</h2>
