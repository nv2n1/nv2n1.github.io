---
title: "pnmtorle(1)"
name: "pnmtorle"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmtorle/"
description: "pnmtorle – convert a Netpbm image file into an RLE image file."
---

<h2 class="name">NAME</h2>
<p> pnmtorle &#8211; convert a Netpbm image file into an RLE image file. </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmtorle</code> [ <code>-h</code> ] [ <code>-v</code> ] [ <code>-a</code> ] [ <code>-o</code><i> outfile</i> ] [ <i>pnmfile</i> ]</p>
<h2>DESCRIPTION</h2>
<p> This program converts Netpbm image files into Utah <code><a href="/docs/linux/man/5-rle/">RLE</a></code>(5) image files. You can include an alpha mask. If the input is a multiple image file, the output consists of several concatenated RLE images. </p>
<p> The RLE file will contain either a three channel color image (24 bits) or a single channel grayscale image (8 bits) depending upon the pnm file depth. If a converted ppm is displayed on an 8 bit display, the image must be dithered. In order to produce a better looking image (on 8 bit displays), it is recommended that the image be quantizing (to 8 bit mapped color) prior to its display. This may be done by piping the output of this program into the Utah <code><a href="/docs/linux/man/1-mcut/">mcut</a></code>(1) or <code><a href="/docs/linux/man/1-rlequant/">rlequant</a></code>(1) utilities. An example of this is shown later. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> This option will cause pnmtorle to operate in verbose mode. The header information is written to &quot;stderr&quot;. Actually, there is not much header information stored in a Netpbm file, so this information is minimal.</p>
<dt><code>-h</code></p>
<dd> This option allows the header of the Netpbm image to be dumped to &quot;stderr&quot; without converting the file. It is equivalent to using the -v option except that no file conversion takes place.</p>
<dt><code>-a</code></p>
<dd> This option causes pnmtorle to include an alpha channel in the output image. The alpha channel is based on the image: Wherever a pixel is black, the corresponding alpha value is transparent. Everywhere else, the alpha value is fully opaque.</p>
<dt><code>-o</code><i> outfile</i></p>
<dd> If specified, the output will be written to this file. If <i>outfile</i> is &quot;-&quot;, or if it is not specified, the output will be written to the standard output stream.</p>
<dt><i>pnmfile</i></p>
<dd> The name of the Netpbm image data file to be converted. If not specified, standard input is assumed.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>pnmtorle -v file.ppm -o file.rle</p>
<dd> While running in verbose mode, convert file.ppm to RLE format and store resulting data in file.rle.</p>
<dt>pnmtorle -h file.pgm</p>
<dd> Dump the header information of the Netpbm file called file.pgm.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rletopnm/">rletopnm</a></code>(1), <code><a href="/docs/linux/man/1-urt/">urt</a></code>(1), <code><a href="/docs/linux/man/5-rle/">RLE</a></code>(5).</p>
<h2>AUTHOR</h2>
<p> Wes Barris<br />
 Army High Performance Computing Research Center (AHPCRC)<br />
 Minnesota Supercomputer Center, Inc. </p>
<h2>Index</h2>
