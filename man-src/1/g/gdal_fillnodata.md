---
title: "gdal_fillnodata(1)"
name: "gdal_fillnodata"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdal_fillnodata/"
description: "gdal_fillnodata – gdal_fillnodata.py fill raster regions by interpolation from edges"
---

<h2 class="name">NAME</h2>
<p> gdal_fillnodata &#8211; gdal_fillnodata.py fill raster regions by interpolation from edges </p>
<h2>SYNOPSIS</h2>
<pre><code>
gdal_fillnodata.py[-q][-md max_distance][-si smooth_iterations]
                  [-o name = value][-b band] srcfile[-nomask][-mask filename][-of format][dstfile]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The gdal_fillnodata.py script fills selection regions (usually nodata areas) by interpolating from valid pixels around the edges of the area. </p>
<p> Additional details on the algorithm are available in the GDALFillNodata() docs. </p>
<dl>
<dt><code>-q</code>:</p>
<dd> The script runs in quiet mode. The progress monitor is supressed and routine messages are not displayed.</dl>
<dl>
<dt><code>-md</code> <i>max_distance</i>:</p>
<dd> The maximum distance (in pixels) that the algorithm will search out for values to interpolate.</dl>
<dl>
<dt><code>-si</code> <i>smooth_iterations</i>:</p>
<dd> The number of 3&#215;3 average filter smoothing iterations to run after the interpolation to dampen artifacts. The default is zero smoothing iterations.</dl>
<dl>
<dt><code>-o</code> <i>name=value</i>:</p>
<dd> Specify a special argument to the algorithm. Currently none are supported.</dl>
<dl>
<dt><code>-b</code> <i>band</i>:</p>
<dd> The band to operate on, by default the first band is operated on.</dl>
<dl>
<dt><i>srcfile</i></p>
<dd> The source raster file used to identify target pixels. Only one band is used.</dl>
<dl>
<dt><code>-nomask</code>:</p>
<dd> Do not use the default validity mask for the input band (such as nodata, or alpha masks).</dl>
<dl>
<dt><code>-mask</code> <i>filename</i>:</p>
<dd> Use the first band of the specified file as a validity mask (zero is invalid, non-zero is valid).</dl>
<dl>
<dt><i>dstfile</i></p>
<dd> The new file to create with the interpolated result. If not provided, the source band is updated in place.</dl>
<dl>
<dt><code>-of</code> <i>format</i>:</p>
<dd> Select the output format. The default is GeoTIFF (GTiff). Use the short format name.</dl>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com </p>
<h2>Index</h2>
