---
title: "ppmtobmp(1)"
name: "ppmtobmp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtobmp/"
description: "ppmtobmp – convert a portable pixmap into a BMP file"
---

<h2 class="name">NAME</h2>
<p> ppmtobmp &#8211; convert a portable pixmap into a BMP file </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtobmp</code> [<code>-windows</code>] [<code>-os2</code>] [<code>-bpp=</code><i>bits_per_pixel</i>] [<i>ppmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input. Produces a Microsoft Windows or OS/2 BMP file as output.</p>
<h2>OPTIONS</h2>
<p> All options can be abbreviated to their shortest unique prefix and you can use a double dash in place of the single dash, GNU-style.</p>
<dl>
<dt><code>-windows</code></p>
<dd> Tells the program to produce a Microsoft Windows BMP file. (This is the default.)</p>
<dt><code>-os2</code></p>
<dd> Tells the program to produce an OS/2 BMP file. (Before August 2000, this was the default).</p>
<dt><code>-bpp</code></p>
<dd> This determines how many bits per pixel you want the BMP file to contain. Only 1, 4, 8, and 24 are possible. By default, <code>ppmtobmp</code> chooses the smallest number with which it can represent all the colors in the input image. If you specify a number too small to represent all the colors in the input image, <code>ppmtobmp</code> tells you and terminates. You can use <code>ppmquant</code> or <code>ppmdither</code> to reduce the number of colors in the image. </p>
</dl>
<h2>NOTES</h2>
<p> To get a faithful reproduction of the input image, the maxval of the input image must be 255. If it is something else, <code>ppmtobmp</code> the colors in the BMP file may be slightly different from the colors in the input. </p>
<p> Windows icons are not BMP files. Use <code>ppmtowinicon</code> to create those. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-bmptoppm/">bmptoppm</a></code>(1), <code><a href="/docs/linux/man/1-ppmtowinicon/">ppmtowinicon</a></code>(1), <code><a href="/docs/linux/man/1-ppmquant/">ppmquant</a></code>(1), <code><a href="/docs/linux/man/1-ppmdither/">ppmdither</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1992 by David W. Sanderson. </p>
<h2>Index</h2>
