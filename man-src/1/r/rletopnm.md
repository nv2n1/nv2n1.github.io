---
title: "rletopnm(1)"
name: "rletopnm"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rletopnm/"
description: "rletopnm – convert a Utah Raster Tools RLE image file into a PNM image file."
---

<h2 class="name">NAME</h2>
<p> rletopnm &#8211; convert a Utah Raster Tools RLE image file into a PNM image file. </p>
<h2>SYNOPSIS</h2>
<p> <code>rletopnm</code> [<code>&#8211;alphaout=</code>{<i>alpha-filename</i>,<code>&#8211;</code>}] [<code>&#8211;headerdump</code>|<code>-h</code>] [<code>&#8211;verbose</code>|<code>-v</code>] [<code>&#8211;plain</code>|<code>-p</code>] [<i>rlefile</i>|<i></i><code>&#8211;</code>] </p>
<p> All options may be abbreviated to their minimum unique abbreviation and options and arguments may be in any order. </p>
<h2>DESCRIPTION</h2>
<p> This program converts Utah Raster Toolkit RLE image files into PNM image files. <code>rletopnm</code> handles four types of RLE files: Grayscale (8 bit data, no color map), Pseudocolor (8 bit data with a color map), Truecolor (24 bit data with color map), and Directcolor (24 bit data, no color map). <code>rletopnm</code> generates a PPM file for all these cases except for the Grayscale file, for which <code>rletopnm</code> generates a PGM file. </p>
<p> <i>rlefile</i> is the RLE input file. If it is absent or <code>&#8211;</code>, the input comes from Standard Input. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;alphaout=</code><i>alpha-filename</i></p>
<dd> <code>rletopnm </code> creates a PGM (portable graymap) file containing the alpha channel values in the input image. If the input image doesn&#8217;t contain an alpha channel, the <i>alpha-filename</i> file contains all zero (transparent) alpha values. If you don&#8217;t specify <code>&#8211;alphaout</code>, <code>rletopnm</code> does not generate an alpha file, and if the input image has an alpha channel, <code>rletopnm</code> simply discards it. </p>
<p> If you specify <code>&#8211;</code> as the filename, <code>rletopnm</code> writes the alpha output to Standard Output and discards the image. </p>
<p> See <code><a href="/docs/linux/man/1-pnmcomp/">pnmcomp</a></code>(1) for one way to use the alpha output file.</p>
<dt><code>&#8211;verbose</code></p>
<dd> This option causes <code>rletopnm </code> to operate in verbose mode. It prints messages about what it&#8217;s doing, including the contents of the RLE image header, to Standard Error.</p>
<dt><code>&#8211;headerdump</code></p>
<dd> This option causes <code>rletopnm</code> to operate in header dump mode. It prints the contents of the RLE image header to Standard Error, but does not produce any other output.</p>
<dt><code>&#8211;plain</code></p>
<dd> This option causes the PNM output file to be in the &quot;plain&quot; (text) format, instead of the default &quot;raw&quot; (binary) format. See <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) and <code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5) for details on the difference. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>rletopnm &#8211;verbose lenna.rle &gt;lenna.ppm</code></p>
<dd> While running in verbose mode, convert lenna.rle to PPM format and store the resulting image as lenna.ppm.</p>
<dt><code>rletopnm &#8211;headerdump file.rle</code></p>
<dd> Dump the header information of the RLE file called file.rle.</p>
<dt><code>rletopnm &#8211;alphaout=dartalpha.pgm dart.rle &gt;dart.ppm</code></p>
<dd> Convert RLE file dart.rle to PPM format as dart.ppm. Store the alpha channel of dart.rle as dartalpha.pgm (if dart.rle doesn&#8217;t have an alpha channel, store a fully transparent alpha mask as dartalpha.pgm). </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmtorle/">pnmtorle</a></code>(1), <code><a href="/docs/linux/man/1-pnmconvol/">pnmconvol</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5), <code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5), <code><a href="/docs/linux/man/1-urt/">urt</a></code>(1), <code><a href="/docs/linux/man/5-rle/">RLE</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Wes Barris<br />
 Army High Performance Computing Research Center (AHPCRC)<br />
 Minnesota Supercomputer Center, Inc. </p>
<p> Modifications by Eric Haines to support raw and plain formats. </p>
<p> Modifications by Bryan Henderson to create alpha files and use mnemonic options. </p>
<h2>Index</h2>
