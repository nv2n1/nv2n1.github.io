---
title: "pbmtoescp2(1)"
name: "pbmtoescp2"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmtoescp2/"
description: "pbmtoescp2 – convert a PBM image to a ESC/P2 printer file"
---

<h2 class="name">NAME</h2>
<p> pbmtoescp2 &#8211; convert a PBM image to a ESC/P2 printer file</p>
<h2>SYNOPSIS</h2>
<p> <code>pbmtoescp2</code> </p>
<p> [<code>-compress=</code><i>compressionmode</i>] [<code>-resolution=</code><i>dpi</i>] [<i>pbmfile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or equals signs between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pbmtoescp2</code> reads a PBM image as input. It produces an ESC/P2 raster graphic printer control stream as output. </p>
<p>&nbsp;<wbr>This program creates an output that is printable on Epson printers that understand the ESC/P2 printer control language (e.g. the Stylus models). For older Epson 9-pin dot matrix printers, which use the ESC/P protocol, see <code>pbmtoepson</code>. </p>
<h2>OPTIONS</h2>
<p> Input is read from file <i>pbmfile</i> if specified, otherwise from stdin. Output is written to stdout. </p>
<dl>
<dt><code>-compress=</code><i>compressionmode</i></p>
<dd> This determines the compression mode that <code>pbmtoescp2</code> uses in its output. Valid values for <i>compressionmode</i> are <code>0</code> and <code>1</code>. <code>-compress=0</code> results in a printer control stream with uncompressed raster graphic data. <code>-compress=1</code> results in a printer control stream with RLE compressed raster graphic data (RLE means Run Length Encoding). The default is <code>-compress=1</code>. </p>
<dt><code>-resolution=</code><i>dpi</i></p>
<dd> This determines the horizontal and the vertical print resolution set in the printer control stream. Another way of looking at it is a declaration of what the resolution of the input image is (PBM images don&#8217;t have inherent resolution). Valid values for <i>dpi</i> are <code>180</code> and <code>360</code>. See hints for more information on this. </p>
<p> The default is <code>-resolution=360</code>. </p>
</dl>
<h2>HINTS</h2>
<p> RLE compresses very well bitmaps of line drawings, preferably horizontal oriented contents like texts, sheets of music, etc. However, bitmaps derived from photographs are not ideal for RLE. In extreme cases, when no byte repetitions occur in the input, the result will be even slightly bigger than the input. To avoid this, use compression mode 0 to switch off RLE. </p>
<p> Each pixel in the input PBM image becomes one dot in the printed output. Therefore, you must make sure the width and height of the input are appropriate for the print resolution you choose and the print area you want. E.g. if you print at 180 dpi and want the image to print as 8 inches by 10, you must supply a PBM that is 1440 pixels wide by 1800 pixels high. You can adjust the size of the input with <code>pamscale</code>, <code>pamstretch</code>, <code>pbmreduce</code>, or <code>pamenlarge</code>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-escp2topbm/">escp2topbm</a></code>(1) , <code><a href="/docs/linux/man/1-pbmtoepson/">pbmtoepson</a></code>(1) , <code><a href="/docs/linux/man/1-pamscale/">pamscale</a></code>(1) , <code><a href="/docs/linux/man/1-pamstretch/">pamstretch</a></code>(1) , <code><a href="/docs/linux/man/1-pbmreduce/">pbmreduce</a></code>(1) , <code><a href="/docs/linux/man/1-pamenlarge/">pamenlarge</a></code>(1) , <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2003 by Ulrich Walcher (<i>u.walcher [at] gmx.de</i>). </p>
<h2>HISTORY</h2>
<p> <code>pbmtoescp2</code> was added to Netpbm in Release 10.18 (August 2003); it was created around the same time. </p>
<h2>Index</h2>
