---
title: "gdal_polygonize(1)"
name: "gdal_polygonize"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdal_polygonize/"
description: "gdal_polygonize – gdal_polygonize.py produces a polygon feature layer from a raster"
---

<h2 class="name">NAME</h2>
<p> gdal_polygonize &#8211; gdal_polygonize.py produces a polygon feature layer from a raster </p>
<h2>SYNOPSIS</h2>
<pre><code>
gdal_polygonize.py[-8][-nomask][-mask filename] raster_file[-b band]
                                                           [-q][-f ogr_format] out_file[layer][fieldname]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This utility creates vector polygons for all connected regions of pixels in the raster sharing a common pixel value. Each polygon is created with an attribute indicating the pixel value of that polygon. A raster mask may also be provided to determine which pixels are eligible for processing. </p>
<p> The utility will create the output vector datasource if it does not already exist, defaulting to GML format. </p>
<p> The utility is based on the GDALPolygonize() function which has additional details on the algorithm. </p>
<dl>
<dt><code>-8</code>:</p>
<dd> (GDAL &gt;= 1.10) Use 8 connectedness. Default is 4 connectedness.</dl>
<dl>
<dt><code>-nomask</code>:</p>
<dd> Do not use the default validity mask for the input band (such as nodata, or alpha masks).</dl>
<dl>
<dt><code>-mask</code> <i>filename</i>:</p>
<dd> Use the first band of the specified file as a validity mask (zero is invalid, non-zero is valid).</dl>
<dl>
<dt><i>raster_file</i></p>
<dd> The source raster file from which polygons are derived.</dl>
<dl>
<dt><code>-b</code> <i>band</i>:</p>
<dd> The band on <i>raster_file</i> to build the polygons from.</dl>
<dl>
<dt><code>-f</code> <i>ogr_format</i></p>
<dd> Select the output format of the file to be created. Default is GML.</dl>
<dl>
<dt><i>out_file</i></p>
<dd> The destination vector file to which the polygons will be written.</dl>
<dl>
<dt><i>layer</i></p>
<dd> The name of the layer created to hold the polygon features.</dl>
<dl>
<dt><i>fieldname</i></p>
<dd> The name of the field to create (defaults to &#8216;DN&#8217;).</dl>
<dl>
<dt><code>-q</code>:</p>
<dd> The script runs in quiet mode. The progress monitor is supressed and routine messages are not displayed.</dl>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com </p>
<h2>Index</h2>
