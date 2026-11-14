---
title: "gif2tiff(1)"
name: "gif2tiff"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gif2tiff/"
description: "gif2tiff – create a TIFF file from a GIF87 format image file"
---

<h2>NAME</h2>
<p> gif2tiff &#8211; create a <font SIZE="-1">TIFF</font> file from a GIF87 format image file</p>
<h2>SYNOPSIS</h2>
<p> <code>gif2tiff</code> [ <i>options</i> ] <i>input.gif</i> <i>output.tif</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Gif2tiff</i> converts a file in the GIF87 format to <font SIZE="-1">TIFF.</font> The <font SIZE="-1">TIFF</font> image is created as a palette image, with samples compressed with the Lempel-Ziv &amp; Welch algorithm (<i>Compression</i>=5). These characteristics can overridden, or explicitly specified with the options described below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Specify a compression scheme to use when writing image data: <code>-c none</code> for no compression, <code>-c packbits</code> for the PackBits compression algorithm, <code>-c zip</code> for the Deflate compression algorithm, and <code>-c lzw</code> for Lempel-Ziv &amp; Welch (the default).</p>
<dt><code>-r</code></p>
<dd> Write data with a specified number of rows per strip; by default the number of rows/strip is selected so that each strip is approximately 8 kilobytes.</dl>
<h2>NOTES</h2>
<p> The program is based on Paul Haeberli&#8217;s <i>fromgif</i> program which, in turn, is based on Marcel J.E. Mol&#8217;s GIF reader.</p>
<h2>BUGS</h2>
<p> Should have more options to control output format.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pal2rgb/">pal2rgb</a></code>(1), <code><a href="/docs/linux/man/1-tiffinfo/">tiffinfo</a></code>(1), <code><a href="/docs/linux/man/1-tiffcp/">tiffcp</a></code>(1), <code><a href="/docs/linux/man/1-tiffmedian/">tiffmedian</a></code>(1), <code><a href="/docs/linux/man/3-libtiff/">libtiff</a></code>(3) </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></code> </p>
<h2>Index</h2>
