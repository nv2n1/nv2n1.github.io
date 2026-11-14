---
title: "tiff2rgba(1)"
name: "tiff2rgba"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tiff2rgba/"
description: "tiff2rgba – convert a TIFF image to RGBA color space"
---

<h2>NAME</h2>
<p> tiff2rgba &#8211; convert a <font SIZE="-1">TIFF</font> image to RGBA color space</p>
<h2>SYNOPSIS</h2>
<p> <code>tiff2rgba</code> [ <i>options</i> ] <i>input.tif</i> <i>output.tif</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Tiff2rgba</i> converts a wide variety of TIFF images into an RGBA TIFF image. This includes the ability to translate different color spaces and photometric interpretation into RGBA, support for alpha blending, and translation of many different bit depths into a 32bit RGBA image. </p>
<p> Internally this program is implemented using the <i>TIFFReadRGBAImage()</i> function, and it suffers any limitations of that image. This includes limited support for &gt; 8 BitsPerSample images, and flaws with some esoteric combinations of BitsPerSample, photometric interpretation, block organization and planar configuration. </p>
<p> The generated images are stripped images with four samples per pixel (red, green, blue and alpha) or if the <code>-n</code> flag is used, three samples per pixel (red, green, and blue). The resulting images are always planar configuration contiguous. For this reason, this program is a useful utility for transform exotic TIFF files into a form ingestible by almost any TIFF supporting software.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Specify a compression scheme to use when writing image data: <code>-c none</code> for no compression (the default), <code>-c packbits</code> for the PackBits compression algorithm, <code>-c zip</code> for the Deflate compression algorithm, <code>-c jpeg</code> for the JPEG compression algorithm, and <code>-c lzw</code> for Lempel-Ziv &amp; Welch.</p>
<dt><code>-r</code></p>
<dd> Write data with a specified number of rows per strip; by default the number of rows/strip is selected so that each strip is approximately 8 kilobytes.</p>
<dt><code>-b</code></p>
<dd> Process the image one block (strip/tile) at a time instead of by reading the whole image into memory at once. This may be necessary for very large images on systems with limited RAM.</p>
<dt><code>-n</code></p>
<dd> Drop the alpha component from the output file, producing a pure RGB file. Currently this does not work if the <code>-b</code> flag is also in effect.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tiff2bw/">tiff2bw</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/3t-TIFFReadRGBAImage/">TIFFReadRGBAImage</a></code>(3t), <code><a href="/docs/linux/man/3-libtiff/">libtiff</a></code>(3) </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></code> </p>
<h2>Index</h2>
