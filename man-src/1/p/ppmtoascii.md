---
title: "ppmtoascii(1)"
name: "ppmtoascii"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtoascii/"
description: "ppmtoascii – convert a PPM image to ASCII graphics with ANSI terminal color"
---

<h2 class="name">NAME</h2>
<p> ppmtoascii &#8211; convert a PPM image to ASCII graphics with ANSI terminal color</p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtoascii</code> </p>
<p> [<code>-1&#215;2</code>|<code>-2&#215;4</code>] </p>
<p> [<i>ppmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>ppmtoascii</code> reads a PPM image as input and produces a somewhat crude ASCII graphic image as output, with ANSI terminal control characters so it has crude color when sent to a color text terminal. </p>
<p> There is no converter for the other direction. </p>
<p> <code>ppmtoterm</code> does a similar thing, but displays each character of the image as a single pixel (using the same dense character for every pixel), whereas <code>ppmtoascii</code> combines 2 or 8 pixels into one character, where the character roughly represents those particular pixels. </p>
<p> Note that ANSI provides for only eight colors (including black and white). </p>
<p> Note that an ANSI terminal can&#8217;t display a single character in multiple colors, so where a character represents 8 pixels of differing colors, the color of the character is one that is the average of the colors of those pixels. </p>
<p> <code>pbmtoascii</code> does the same thing for PBM images, with no terminal control characters (because none are needed for a strictly black and white image). </p>
<h2>OPTIONS</h2>
<p> The <code>-1&#215;2</code> and <code>-2&#215;4</code> options give you two alternate ways for the pixels to get mapped to characters. With <code>1&#215;2</code>, the default, each character represents a group of 1 pixel across by 2 pixels down. With <code>-2&#215;4</code>, each character represents 2 pixels across by 4 pixels down. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pbmtoascii/">pbmtoascii</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-ppmtoterm/">ppmtoterm</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>ppmtoascii</code> was new in Netpbm 10.51 (June 2010). Frank Ch. Eigler derived it from <code>pbmtoascii</code>. </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2010 by Frank Ch. Eigler. </p>
<h2>Index</h2>
