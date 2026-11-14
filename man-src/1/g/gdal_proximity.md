---
title: "gdal_proximity(1)"
name: "gdal_proximity"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdal_proximity/"
description: "gdal_proximity – gdal_proximity.py produces a raster proximity map"
---

<h2 class="name">NAME</h2>
<p> gdal_proximity &#8211; gdal_proximity.py produces a raster proximity map </p>
<h2>SYNOPSIS</h2>
<pre><code>
gdal_proximity.py srcfile dstfile[-srcband n][-dstband n]
                                 [-of format][-co name = value] *
    [-ot Byte / Int16 / Int32 / Float32 /
        etc]
        [-values n, n, n][-distunits PIXEL / GEO]
        [-maxdist n][-nodata n][-fixed - buf - val n]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The gdal_proximity.py script generates a raster proximity map indicating the distance from the center of each pixel to the center of the nearest pixel identified as a target pixel. Target pixels are those in the source raster for which the raster pixel value is in the set of target pixel values. </p>
<dl>
<dt><i>srcfile</i></p>
<dd> The source raster file used to identify target pixels.</dl>
<dl>
<dt><i>dstfile</i></p>
<dd> The destination raster file to which the proximity map will be written. It may be a pre-existing file of the same size as srcfile. If it does not exist it will be created.</dl>
<dl>
<dt><code>-srcband</code> <i>n</i></p>
<dd> Identifies the band in the source file to use (default is 1).</dl>
<dl>
<dt><code>-dstband</code> <i>n</i></p>
<dd> Identifies the band in the destination file to use (default is 1).</dl>
<dl>
<dt><code>-of</code> <i>format</i>:</p>
<dd> Select the output format. The default is GeoTIFF (GTiff). Use the short format name.</dl>
<dl>
<dt><code>-co</code> <i>&#8216;NAME=VALUE&#8217;</i>:</p>
<dd> passes a creation option to the output format driver. Multiple <code>-co</code> options may be listed. See format specific documentation for legal creation options for each format.</dl>
<dl>
<dt><code>-ot</code> <i>datatype</i>:</p>
<dd> Force the output image bands to have a specific type. Use type names (ie. Byte, Int16,&#8230;)</dl>
<dl>
<dt><code>-values</code> <i>n,n,n</i>:</p>
<dd> A list of target pixel values in the source image to be considered target pixels. If not specified, all non-zero pixels will be considered target pixels.</dl>
<dl>
<dt><code>-distunits</code> <i>PIXEL/GEO</i>:</p>
<dd> Indicate whether distances generated should be in pixel or georeferenced coordinates (default PIXEL).</dl>
<dl>
<dt><code>-maxdist</code> <i>n</i>:</p>
<dd> The maximum distance to be generated. All pixels beyond this distance will be assigned either the nodata value, or 65535. Distance is interpreted in pixels unless -distunits GEO is specified.</dl>
<dl>
<dt><code>-nodata</code> <i>n</i>:</p>
<dd> Specify a nodata value to use for the destination proximity raster.</dl>
<dl>
<dt><code>-fixed-buf-val</code> <i>n</i>:</p>
<dd> Specify a value to be applied to all pixels that are within the -maxdist of target pixels (including the target pixels) instead of a distance value.</dl>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com </p>
<h2>Index</h2>
