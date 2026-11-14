---
title: "nearblack(1)"
name: "nearblack"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nearblack/"
description: "nearblack – nearblack convert nearly black/white borders to black"
---

<h2 class="name">NAME</h2>
<p> nearblack &#8211; nearblack convert nearly black/white borders to black </p>
<h2>SYNOPSIS</h2>
<pre><code>
nearblack[-of format][-white | [ -color c1, c2, c3... cn ] * ][-near dist][-nb non_black_pixels]
         [-setalpha][-setmask][-o outfile][-q][-co "NAME=VALUE"] *
    infile
</code></pre>
<h2>DESCRIPTION</h2>
<p> This utility will scan an image and try to set all pixels that are nearly or exactly black, white or one or more custom colors around the collar to black or white. This is often used to &#8216;fix up&#8217; lossy compressed airphotos so that color pixels can be treated as transparent when mosaicking. </p>
<dl>
<dt><code>-o</code> <i>outfile</i>:</p>
<dd> The name of the output file to be created. Newly created files are created with the HFA driver by default (Erdas Imagine &#8211; .img)</p>
<dt><code>-of</code> <i>format</i>:</p>
<dd> (GDAL 1.8.0 or later) Select the output format. Use the short format name (GTiff for GeoTIFF for examle).</p>
<dt><code>-co</code> <i>&#8216;NAME=VALUE&#8217;</i>:</p>
<dd> (GDAL 1.8.0 or later) Passes a creation option to the output format driver. Multiple <code>-co</code> options may be listed. See format specific documentation for legal creation options for each format. Only valid when creating a new file</p>
<dt><code>-white</code>:</p>
<dd> Search for nearly white (255) pixels instead of nearly black pixels.</p>
<dt><code>-color</code> <i>c1,c2,c3&#8230;cn</i>:</p>
<dd> (GDAL &gt;= 1.9.0) Search for pixels near the specified color. May be specified multiple times. When -color is specified, the pixels that are considered as the collar are set to 0.</p>
<dt><code>-near</code> <i>dist</i>:</p>
<dd> Select how far from black, white or custom colors the pixel values can be and still considered near black, white or custom color. Defaults to 15.</p>
<dt><code>-nb</code> <i>non_black_pixels</i>:</p>
<dd> number of non-black pixels that can be encountered before the giving up search inwards. Defaults to 2.</p>
<dt><code>-setalpha</code>:</p>
<dd> (GDAL 1.8.0 or later) Adds an alpha band if the output file is specified and the input file has 3 bands, or sets the alpha band of the output file if it is specified and the input file has 4 bands, or sets the alpha band of the input file if it has 4 bands and no output file is specified. The alpha band is set to 0 in the image collar and to 255 elsewhere.</p>
<dt><code>-setmask</code>:</p>
<dd> (GDAL 1.8.0 or later) Adds a mask band to the output file, or adds a mask band to the input file if it does not already have one and no output file is specified. The mask band is set to 0 in the image collar and to 255 elsewhere.</p>
<dt><code>-q</code>:</p>
<dd> (GDAL 1.8.0 or later) Suppress progress monitor and other non-error output.</p>
<dt><i>infile</i>:</p>
<dd> The input file. Any GDAL supported format, any number of bands, normally 8bit Byte bands.</dl>
<p> The algorithm processes the image one scanline at a time. A scan &#8216;in&#8217; is done from either end setting pixels to black or white until at least &#8216;non_black_pixels&#8217; pixels that are more than &#8216;dist&#8217; gray levels away from black, white or custom colors have been encountered at which point the scan stops. The nearly black, white or custom color pixels are set to black or white. The algorithm also scans from top to bottom and from bottom to top to identify indentations in the top or bottom. </p>
<p> The processing is all done in 8bit (Bytes). </p>
<p> If the output file is omitted, the processed results will be written back to the input file &#8211; which must support update.</p>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com </p>
<h2>Index</h2>
