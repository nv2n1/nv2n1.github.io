---
title: "rgb2ycbcr(1)"
name: "rgb2ycbcr"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rgb2ycbcr/"
description: "rgb2ycbcr – convert non-YCbCr TIFF images to a YCbCr TIFF image"
---

<h2>NAME</h2>
<p> rgb2ycbcr &#8211; convert non-YCbCr <font SIZE="-1">TIFF</font> images to a YCbCr <font SIZE="-1">TIFF</font> image</p>
<h2>SYNOPSIS</h2>
<p> <code>rgb2ycbcr</code> [ <i>options</i> ] <i>src1.tif src2.tif &#8230; dst.tif</i></p>
<h2>DESCRIPTION</h2>
<p> <i>rgb2ycbcr</i> converts <font SIZE="-1">RGB</font> color, greyscale, or bi-level <font SIZE="-1">TIFF</font> images to YCbCr images by transforming and sampling pixel data. If multiple files are specified on the command line each source file is converted to a separate directory in the destination file. </p>
<p> By default, chrominance samples are created by sampling 2 by 2 blocks of luminance values; this can be changed with the <code>-h</code> and <code>-v</code> options. Output data are compressed with the <font SIZE="-1">PackBits</font> compression scheme, by default; an alternate scheme can be selected with the <code>-c</code> option. By default, output data are compressed in strips with the number of rows in each strip selected so that the size of a strip is never more than 8 kilobytes; the <code>-r</code> option can be used to explicitly set the number of rows per strip.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Specify a compression scheme to use when writing image data: <code>-c none</code> for no compression, <code>-c packbits</code> for the PackBits compression algorithm (the default), <code>-c jpeg</code> for the JPEG compression algorithm, <code>-c zip</code> for the deflate compression algorithm, and <code>-c lzw</code> for Lempel-Ziv &amp; Welch.</p>
<dt><code>-h</code></p>
<dd> Set the horizontal sampling dimension to one of: 1, 2 (default), or 4.</p>
<dt><code>-r</code></p>
<dd> Write data with a specified number of rows per strip; by default the number of rows/strip is selected so that each strip is approximately 8 kilobytes.</p>
<dt><code>-v</code></p>
<dd> Set the vertical sampling dimension to one of: 1, 2 (default), or 4.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tiffinfo/">tiffinfo</a></code>(1), <code><a href="/docs/linux/man/1-tiffcp/">tiffcp</a></code>(1), <code><a href="/docs/linux/man/3-libtiff/">libtiff</a></code>(3) </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff">http://www.remotesensing.org/libtiff</a></code> </p>
<h2>Index</h2>
