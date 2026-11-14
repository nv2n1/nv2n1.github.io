---
title: "tiff2bw(1)"
name: "tiff2bw"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tiff2bw/"
description: "tiff2bw – convert a color TIFF image to greyscale"
---

<h2>NAME</h2>
<p> tiff2bw &#8211; convert a color <font SIZE="-1">TIFF</font> image to greyscale</p>
<h2>SYNOPSIS</h2>
<p> <code>tiff2bw</code> [ <i>options</i> ] <i>input.tif</i> <i>output.tif</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Tiff2bw</i> converts an <font SIZE="-1">RGB</font> or Palette color <font SIZE="-1">TIFF</font> image to a greyscale image by combining percentages of the red, green, and blue channels. By default, output samples are created by taking 28% of the red channel, 59% of the green channel, and 11% of the blue channel. To alter these percentages, the <code>-R</code>, <code>-G</code>, and <code>-B</code> options may be used.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Specify a compression scheme to use when writing image data: <code>-c none</code> for no compression, <code>-c packbits</code> for the PackBits compression algorithm, <code>-c zip</code> for the Deflate compression algorithm, <code>-c g3</code> for the CCITT Group 3 compression algorithm, <code>-c g4</code> for the CCITT Group 4 compression algorithm, and <code>-c lzw</code> for Lempel-Ziv &amp; Welch (the default).</p>
<dt><code>-r</code></p>
<dd> Write data with a specified number of rows per strip; by default the number of rows/strip is selected so that each strip is approximately 8 kilobytes.</p>
<dt><code>-R</code></p>
<dd> Specify the percentage of the red channel to use (default 28).</p>
<dt><code>-G</code></p>
<dd> Specify the percentage of the green channel to use (default 59).</p>
<dt><code>-B</code></p>
<dd> Specify the percentage of the blue channel to use (default 11).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pal2rgb/">pal2rgb</a></code>(1), <code><a href="/docs/linux/man/1-tiffinfo/">tiffinfo</a></code>(1), <code><a href="/docs/linux/man/1-tiffcp/">tiffcp</a></code>(1), <code><a href="/docs/linux/man/1-tiffmedian/">tiffmedian</a></code>(1), <code><a href="/docs/linux/man/3-libtiff/">libtiff</a></code>(3) </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></code> </p>
<h2>Index</h2>
