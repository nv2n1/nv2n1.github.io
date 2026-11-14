---
title: "tiffdither(1)"
name: "tiffdither"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tiffdither/"
description: "tiffdither – convert a greyscale image to bilevel using dithering"
---

<h2>NAME</h2>
<p> tiffdither &#8211; convert a greyscale image to bilevel using dithering</p>
<h2>SYNOPSIS</h2>
<p> <code>tiffdither</code> [ <i>options</i> ] <i>input.tif</i> <i>output.tif</i></p>
<h2>DESCRIPTION</h2>
<p> <i>tiffdither</i> converts a single channel 8-bit greyscale image to a bilevel image using Floyd-Steinberg error propagation with thresholding.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Specify the compression to use for data written to the output file: <code>none </code> for no compression, <code>packbits</code> for PackBits compression, <code>lzw</code> for Lempel-Ziv &amp; Welch compression, <code>zip</code> for Deflate compression, <code>g3</code> for CCITT Group 3 (T.4) compression, and <code>g4</code> for CCITT Group 4 (T.6) compression. By default <i>tiffdither</i> will compress data according to the value of the <i>Compression</i> tag found in the source file.</p>
<dt>
<dd> The <font SIZE="-1">CCITT</font> Group 3 and Group 4 compression algorithms can only be used with bilevel data.</p>
<dt>
<dd> Group 3 compression can be specified together with several T.4-specific options: <code>1d</code> for 1-dimensional encoding, <code>2d</code> for 2-dimensional encoding, and <code>fill</code> to force each encoded scanline to be zero-filled so that the terminating EOL code lies on a byte boundary. Group 3-specific options are specified by appending a &#8220;:&#8221;-separated list to the &#8220;g3&#8221; option; e.g. <code>-c g3:2d:fill</code> to get 2D-encoded data with byte-aligned EOL codes.</p>
<dt>
<dd> <font SIZE="-1">LZW</font> compression can be specified together with a <i>predictor</i> value. A predictor value of 2 causes each scanline of the output image to undergo horizontal differencing before it is encoded; a value of 1 forces each scanline to be encoded without differencing. LZW-specific options are specified by appending a &#8220;:&#8221;-separated list to the &#8220;lzw&#8221; option; e.g. <code>-c lzw:2</code> for <font SIZE="-1">LZW</font> compression with horizontal differencing.</p>
<dt><code>-f</code></p>
<dd> Specify the bit fill order to use in writing output data. By default, <i>tiffdither</i> will create a new file with the same fill order as the original. Specifying <code>-f lsb2msb</code> will force data to be written with the <i>FillOrder</i> tag set to <font SIZE="-1">LSB2MSB ,</font> while <code>-f msb2lsb</code> will force data to be written with the <i>FillOrder</i> tag set to <font SIZE="-1">MSB2LSB .</font></p>
<dt><code>-t</code></p>
<dd> Set the threshold value for dithering. By default the threshold value is 128.</dl>
<h2>NOTES</h2>
<p> The dither algorithm is taken from the <code><a href="/docs/linux/man/1-tiffmedian/">tiffmedian</a></code>(1) program (written by Paul Heckbert).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pal2rgb/">pal2rgb</a></code>(1), <code><a href="/docs/linux/man/1-fax2tiff/">fax2tiff</a></code>(1), <code><a href="/docs/linux/man/1-tiffinfo/">tiffinfo</a></code>(1), <code><a href="/docs/linux/man/1-tiffcp/">tiffcp</a></code>(1), <code><a href="/docs/linux/man/1-tiff2bw/">tiff2bw</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/3TIFF-libtiff/">libtiff</a></code>(3TIFF) </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></code> </p>
<h2>Index</h2>
