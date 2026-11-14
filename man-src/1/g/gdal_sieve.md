---
title: "gdal_sieve(1)"
name: "gdal_sieve"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdal_sieve/"
description: "gdal_sieve – gdal_sieve.py removes small raster polygons"
---

<h2 class="name">NAME</h2>
<p> gdal_sieve &#8211; gdal_sieve.py removes small raster polygons </p>
<h2>SYNOPSIS</h2>
<pre><code>
gdal_sieve.py[-q][-st threshold][-4][-8][-o name = value] srcfile[-nomask][-mask filename][-of format][dstfile]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The gdal_sieve.py script removes raster polygons smaller than a provided threshold size (in pixels) and replaces replaces them with the pixel value of the largest neighbour polygon. The result can be written back to the existing raster band, or copied into a new file. </p>
<p> Additional details on the algorithm are available in the GDALSieveFilter() docs. </p>
<dl>
<dt><code>-q</code>:</p>
<dd> The script runs in quiet mode. The progress monitor is supressed and routine messages are not displayed.</dl>
<dl>
<dt><code>-st</code> <i>threshold</i>:</p>
<dd> Set the size threshold in pixels. Only raster polygons smaller than this size will be removed.</dl>
<dl>
<dt><code>-o</code> <i>name=value</i>:</p>
<dd> Specify a special argument to the algorithm. Currently none are supported.</dl>
<dl>
<dt><code>-4</code>:</p>
<dd> Four connectedness should be used when determining polygons. That is diagonal pixels are not considered directly connected. This is the default.</dl>
<dl>
<dt><code>-8</code>:</p>
<dd> Eight connectedness should be used when determining polygons. That is diagonal pixels are considered directly connected.</dl>
<dl>
<dt><i>srcfile</i></p>
<dd> The source raster file used to identify target pixels. Only the first band is used.</dl>
<dl>
<dt><code>-nomask</code>:</p>
<dd> Do not use the default validity mask for the input band (such as nodata, or alpha masks).</dl>
<dl>
<dt><code>-mask</code> <i>filename</i>:</p>
<dd> Use the first band of the specified file as a validity mask (zero is invalid, non-zero is valid).</dl>
<dl>
<dt><i>dstfile</i></p>
<dd> The new file to create with the filtered result. If not provided, the source band is updated in place.</dl>
<dl>
<dt><code>-of</code> <i>format</i>:</p>
<dd> Select the output format. The default is GeoTIFF (GTiff). Use the short format name.</dl>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com </p>
<h2>Index</h2>
