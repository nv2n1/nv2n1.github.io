---
title: "gdal_merge(1)"
name: "gdal_merge"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdal_merge/"
description: "gdal_merge – gdal_merge.py mosaics a set of images"
---

<h2 class="name">NAME</h2>
<p> gdal_merge &#8211; gdal_merge.py mosaics a set of images </p>
<h2>SYNOPSIS</h2>
<pre><code>
gdal_merge.py[-o out_filename][-of out_format][-co NAME = VALUE] *
    [-ps pixelsize_x pixelsize_y][-tap][-separate][-v][-pct]
                                 [-ul_lr ulx uly lrx lry][-n nodata_value][-init "value [value...]"]
                                 [-ot datatype][-createonly] input_files
</code></pre>
<h2>DESCRIPTION</h2>
<p> This utility will automatically mosaic a set of images. All the images must be in the same coordinate system and have a matching number of bands, but they may be overlapping, and at different resolutions. In areas of overlap, the last image will be copied over earlier ones. </p>
<dl>
<dt><code>-o</code> <i>out_filename</i>:</dt>
<dd> The name of the output file, which will be created if it does not already exist (defaults to &#8216;out.tif&#8217;).</dd>
<dt><code>-of</code> <i>format</i>:</dt>
<dd> Output format, defaults to GeoTIFF (GTiff).</dd>
<dt><code>-co</code> <i>NAME=VALUE</i>:</dt>
<dd> Creation option for output file. Multiple options can be specified.</dd>
<dt><code>-ot</code> <i>datatype</i>:</dt>
<dd> Force the output image bands to have a specific type. Use type names (ie. Byte, Int16,&#8230;)</dd>
<dt><code>-ps</code> <i>pixelsize_x pixelsize_y</i>:</dt>
<dd> Pixel size to be used for the output file. If not specified the resolution of the first input file will be used.</dd></dl>
<dl>
<dt><code>-tap</code>:</dt>
<dd> (GDAL &gt;= 1.8.0) (target aligned pixels) align the coordinates of the extent of the output file to the values of the -tr, such that the aligned extent includes the minimum extent.</dd></dl>
<dl>
<dt><code>-ul_lr</code> <i>ulx uly lrx lry</i>:</dt>
<dd> The extents of the output file. If not specified the aggregate extents of all input files will be used.</dd>
<dt><code>-v</code>:</dt>
<dd> Generate verbose output of mosaicing operations as they are done.</dd>
<dt><code>-separate</code>:</dt>
<dd> Place each input file into a separate <i>stacked</i> band.</dd>
<dt><code>-pct</code>:</dt>
<dd> Grab a pseudocolor table from the first input image, and use it for the output. Merging pseudocolored images this way assumes that all input files use the same color table.</dd>
<dt><code>-n</code> <i>nodata_value</i>:</dt>
<dd> Ignore pixels from files being merged in with this pixel value.</dd>
<dt><code>-a_nodata</code> <i>output_nodata_value</i>:</dt>
<dd> (GDAL &gt;= 1.9.0) Assign a specified nodata value to output bands.</dd>
<dt><code>-init</code> <i>&#8216;value(s)&#8217;</i>:</dt>
<dd> Pre-initialize the output image bands with these values. However, it is not marked as the nodata value in the output file. If only one value is given, the same value is used in all the bands.</dd>
<dt><code>-createonly</code>:</dt>
<dd> The output file is created (and potentially pre-initialized) but no input image data is copied into it.</dd></dl>
<p> NOTE: gdal_merge.py is a Python script, and will only work if GDAL was built with Python support.</p>
<h2>EXAMPLE</h2>
<p> Create an image with the pixels in all bands initialized to 255. </p>
<pre>
% gdal_merge.py -init 255 -o out.tif in1.tif in2.tif
</pre>
<p> Create an RGB image that shows blue in pixels with no data. The first two bands will be initialized to 0 and the third band will be initalized to 255. </p>
<pre>
% gdal_merge.py -init &quot;0 0 255&quot; -o out.tif in1.tif in2.tif
</pre>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com, Silke Reimer silke [at] intevation.de </p>
