---
title: "ppm2tiff(1)"
name: "ppm2tiff"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppm2tiff/"
description: "ppm2tiff – create a TIFF file from PPM, PGM and PBM image files"
---

<h2>NAME</h2>
<p> ppm2tiff &#8211; create a <font SIZE="-1">TIFF</font> file from <font SIZE="-1">PPM, PGM</font> and <font SIZE="-1">PBM</font> image files</p>
<h2>SYNOPSIS</h2>
<p> <code>ppm2tiff</code> [ <i>options</i> ] [ <i>input.ppm</i> ] <i>output.tif</i></p>
<h2>DESCRIPTION</h2>
<p> <i>ppm2tiff</i> converts a file in the <font SIZE="-1">PPM, PGM</font> and <font SIZE="-1">PBM</font> image formats to <font SIZE="-1">TIFF.</font> By default, the <font SIZE="-1">TIFF</font> image is created with data samples packed (<i>PlanarConfiguration</i>=1), compressed with the Packbits algorithm (<i>Compression</i>=32773), and with each strip no more than 8 kilobytes. These characteristics can be overridden, or explicitly specified with the options described below </p>
<p> If the <font SIZE="-1">PPM</font> file contains greyscale data, then the <i>PhotometricInterpretation</i> tag is set to 1 (min-is-black), otherwise it is set to 2 (RGB). </p>
<p> If no <font SIZE="-1">PPM</font> file is specified on the command line, <i>ppm2tiff</i> will read from the standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Specify a compression scheme to use when writing image data: <code>none </code> for no compression, <code>packbits</code> for PackBits compression (will be used by default), <code>lzw</code> for Lempel-Ziv &amp; Welch compression, <code>jpeg</code> for baseline JPEG compression, <code>zip</code> for Deflate compression, <code>g3</code> for CCITT Group 3 (T.4) compression, and <code>g4</code> for CCITT Group 4 (T.6) compression.</p>
<dt><code>-r</code></p>
<dd> Write data with a specified number of rows per strip; by default the number of rows/strip is selected so that each strip is approximately 8 kilobytes.</p>
<dt><code>-R</code></p>
<dd> Mark the resultant image to have the specified X and Y resolution (in dots/inch).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tiffinfo/">tiffinfo</a></code>(1), <code><a href="/docs/linux/man/1-tiffcp/">tiffcp</a></code>(1), <code><a href="/docs/linux/man/1-tiffmedian/">tiffmedian</a></code>(1), <code><a href="/docs/linux/man/3-libtiff/">libtiff</a></code>(3) </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></code> </p>
<h2>Index</h2>
