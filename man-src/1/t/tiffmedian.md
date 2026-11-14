---
title: "tiffmedian(1)"
name: "tiffmedian"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tiffmedian/"
description: "tiffmedian – apply the median cut algorithm to data in a TIFF file"
---

<h2>NAME</h2>
<p> tiffmedian &#8211; apply the median cut algorithm to data in a <font SIZE="-1">TIFF</font> file</p>
<h2>SYNOPSIS</h2>
<p> <code>tiffmedian</code> [ <i>options</i> ] <i>input.tif</i> <i>output.tif</i></p>
<h2>DESCRIPTION</h2>
<p> <i>tiffmedian</i> applies the median cut algorithm to an <font SIZE="-1">RGB</font> image in <i>input.tif</i> to generate a palette image that is written to <i>output.tif</i>. The generated colormap has, by default, 256 entries. The image data is quantized by mapping each pixel to the closest color values in the colormap.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Specify the compression to use for data written to the output file: <code>none </code> for no compression, <code>packbits</code> for PackBits compression, <code>lzw</code> for Lempel-Ziv &amp; Welch compression, and <code>zip</code> for Deflate compression. By default <i>tiffmedian</i> will compress data according to the value of the <i>Compression</i> tag found in the source file.</p>
<dt>
<dd> <font SIZE="-1">LZW</font> compression can be specified together with a <i>predictor</i> value. A predictor value of 2 causes each scanline of the output image to undergo horizontal differencing before it is encoded; a value of 1 forces each scanline to be encoded without differencing. LZW-specific options are specified by appending a &#8220;:&#8221;-separated list to the &#8220;lzw&#8221; option; e.g. <code>-c lzw:2</code> for <font SIZE="-1">LZW</font> compression with horizontal differencing.</p>
<dt><code>-C</code></p>
<dd> Specify the number of entries to use in the generated colormap. By default all 256 entries/colors are used.</p>
<dt><code>-f</code></p>
<dd> Apply Floyd-Steinberg dithering before selecting a colormap entry.</p>
<dt><code>-r</code></p>
<dd> Specify the number of rows (scanlines) in each strip of data written to the output file. By default, <i>tiffmedian</i> attempts to set the rows/strip that no more than 8 kilobytes of data appear in a strip.</dl>
<h2>NOTES</h2>
<p> This program is derived from Paul Heckbert&#8217;s <i>median</i> program.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pal2rgb/">pal2rgb</a></code>(1), <code><a href="/docs/linux/man/1-tiffinfo/">tiffinfo</a></code>(1), <code><a href="/docs/linux/man/1-tiffcp/">tiffcp</a></code>(1), <code><a href="/docs/linux/man/1-tiffcmp/">tiffcmp</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/3TIFF-libtiff/">libtiff</a></code>(3TIFF) </p>
<p> <code>Color Image Quantization for Frame Buffer Display,</code> Paul Heckbert, SIGGRAPH proceedings, 1982, pp. 297-307. </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></code> </p>
<h2>Index</h2>
