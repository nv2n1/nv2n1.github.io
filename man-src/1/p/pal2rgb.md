---
title: "pal2rgb(1)"
name: "pal2rgb"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pal2rgb/"
description: "pal2rgb – convert a palette color TIFF image to a full color image"
---

<h2>NAME</h2>
<p> pal2rgb &#8211; convert a palette color <font SIZE="-1">TIFF</font> image to a full color image</p>
<h2>SYNOPSIS</h2>
<p> <code>pal2rgb</code> [ <i>options</i> ] <i>input.tif</i> <i>output.tif</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Pal2rgb</i> converts a palette color <font SIZE="-1">TIFF</font> image to a full color image by applying the colormap of the palette image to each sample to generate a full color <font SIZE="-1">RGB</font> image.</p>
<h2>OPTIONS</h2>
<p> Options that affect the interpretation of input data are:</p>
<dl>
<dt><code>-C</code></p>
<dd> This option overrides the default behavior of <i>pal2rgb</i> in determining whether or not colormap entries contain 16-bit or 8-bit values. By default the colormap is inspected and if no colormap entry greater than 255 is found, the colormap is assumed to have only 8-bit values; otherwise 16-bit values (as required by the <font SIZE="-1">TIFF</font> specification) are assumed. The <code>-C</code> option can be used to explicitly specify the number of bits for colormap entries: <code>-C 8</code> for 8-bit values, <code>-C 16</code> for 16-bit values.</dl>
<p> Options that affect the output file format are:</p>
<dl>
<dt><code>-p</code></p>
<dd> Explicitly select the planar configuration used in organizing data samples in the output image: <code>-p contig</code> for samples packed contiguously, and <code>-p separate</code> for samples stored separately. By default samples are packed.</p>
<dt><code>-c</code></p>
<dd> Use the specific compression algorithm to encoded image data in the output file: <code>-c packbits</code> for Macintosh Packbits, <code>-c lzw</code> for Lempel-Ziv &amp; Welch, <code>-c zip</code> for Deflate, <code>-c none</code> for no compression. If no compression-related option is specified, the input file&#8217;s compression algorithm is used.</p>
<dt><code>-r</code></p>
<dd> Explicitly specify the number of rows in each strip of the output file. If the <code>-r</code> option is not specified, a number is selected such that each output strip has approximately 8 kilobytes of data in it.</dl>
<h2>BUGS</h2>
<p> Only 8-bit images are handled.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tiffinfo/">tiffinfo</a></code>(1), <code><a href="/docs/linux/man/1-tiffcp/">tiffcp</a></code>(1), <code><a href="/docs/linux/man/1-tiffmedian/">tiffmedian</a></code>(1), <code><a href="/docs/linux/man/3-libtiff/">libtiff</a></code>(3) </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></code> </p>
<h2>Index</h2>
