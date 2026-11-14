---
title: "ras2tiff(1)"
name: "ras2tiff"
section: "1"
letter: "r"
url: "/docs/linux/man/1-ras2tiff/"
description: "ras2tiff – create a TIFF file from a Sun rasterfile"
---

<h2>NAME</h2>
<p> ras2tiff &#8211; create a <font SIZE="-1">TIFF</font> file from a Sun rasterfile</p>
<h2>SYNOPSIS</h2>
<p> <code>ras2tiff</code> [ <i>options</i> ] <i>input.ras</i> <i>output.tif</i></p>
<h2>DESCRIPTION</h2>
<p> <i>ras2tiff</i> converts a file in the Sun rasterfile format to <font SIZE="-1">TIFF.</font> By default, the <font SIZE="-1">TIFF</font> image is created with data samples packed (<i>PlanarConfiguration</i>=1), compressed with the Lempel-Ziv &amp; Welch algorithm (<i>Compression</i>=5), and with each strip no more than 8 kilobytes. These characteristics can overridden, or explicitly specified with the options described below. </p>
<p> Any colormap information in the rasterfile is carried over to the <font SIZE="-1">TIFF</font> file by including a <i>Colormap</i> tag in the output file. If the rasterfile has a colormap, the <i>PhotometricInterpretation</i> tag is set to 3 (palette); otherwise it is set to 2 (RGB) if the depth is 24 or 1 (min-is-black) if the depth is not 24.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Specify a compression scheme to use when writing image data: <code>-c none</code> for no compression, <code>-c packbits</code> for the PackBits compression algorithm, <code>-c jpeg</code> for the baseline JPEG compression algorithm, <code>-c zip</code> for the Deflate compression algorithm, and <code>-c lzw</code> for Lempel-Ziv &amp; Welch (the default).</p>
<dt><code>-r</code></p>
<dd> Write data with a specified number of rows per strip; by default the number of rows/strip is selected so that each strip is approximately 8 kilobytes.</dl>
<h2>BUGS</h2>
<p> Does not handle all possible rasterfiles. In particular, <i>ras2tiff</i> does not handle run-length encoded images.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pal2rgb/">pal2rgb</a></code>(1), <code><a href="/docs/linux/man/1-tiffinfo/">tiffinfo</a></code>(1), <code><a href="/docs/linux/man/1-tiffcp/">tiffcp</a></code>(1), <code><a href="/docs/linux/man/1-tiffmedian/">tiffmedian</a></code>(1), <code><a href="/docs/linux/man/3-libtiff/">libtiff</a></code>(3) </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></code> </p>
<h2>Index</h2>
