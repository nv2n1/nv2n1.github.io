---
title: "bmp2tiff(1)"
name: "bmp2tiff"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bmp2tiff/"
description: "bmp2tiff – create a TIFF file from a Microsoft Windows Device Independent Bitmap image file"
---

<h2>NAME</h2>
<p> bmp2tiff &#8211; create a <font SIZE="-1">TIFF</font> file from a Microsoft Windows Device Independent Bitmap image file</p>
<h2>SYNOPSIS</h2>
<p> <code>bmp2tiff</code> [ <i>options</i> ] <i>input.bmp</i> [ <i>input2.bmp &#8230;</i> ] <i>output.tiff</i></p>
<h2>DESCRIPTION</h2>
<p> <i>bmp2tiff</i> converts a Microsoft Windows Device Independent Bitmap image file to <font SIZE="-1">TIFF.</font> If several input BMP files are being specified the multipage <font SIZE="-1">TIFF</font> output file will be created. By default, the <font SIZE="-1">TIFF</font> image is created with data samples packed (<i>PlanarConfiguration</i>=1), compressed with the PackBits algorithm (<i>Compression</i>=32773), and with each strip no more than 8 kilobytes. These characteristics can overridden, or explicitly specified with the options described below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Specify a compression scheme to use when writing image data: <code>-c none</code> for no compression, <code>-c packbits</code> for the PackBits compression algorithm (the default), <code>-c jpeg</code> for the baseline JPEG compression algorithm, <code>-c zip</code> for the Deflate compression algorithm, and <code>-c lzw</code> for Lempel-Ziv &amp; Welch.</p>
<dt><code>-r</code><i> number</i></p>
<dd> Write data with a specified number of rows per strip; by default the number of rows/strip is selected so that each strip is approximately 8 kilobytes.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gif2tiff/">gif2tiff</a></code>(1), <code><a href="/docs/linux/man/1-pal2rgb/">pal2rgb</a></code>(1), <code><a href="/docs/linux/man/1-ppm2tiff/">ppm2tiff</a></code>(1), <code><a href="/docs/linux/man/1-raw2tiff/">raw2tiff</a></code>(1), <code><a href="/docs/linux/man/1-ras2tiff/">ras2tiff</a></code>(1), <code><a href="/docs/linux/man/1-sgi2tiff/">sgi2tiff</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/3TIFF-libtiff/">libtiff</a></code>(3TIFF) </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></code> </p>
<h2>Index</h2>
