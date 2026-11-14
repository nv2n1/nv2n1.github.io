---
title: "gdal_translate(1)"
name: "gdal_translate"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdal_translate/"
description: "gdal_translate – gdal_translate converts raster data between different formats"
---

<h2 class="name">NAME</h2>
<p> gdal_translate &#8211; gdal_translate converts raster data between different formats </p>
<h2>SYNOPSIS</h2>
<pre><code>
gdal_translate[--help - general]
              [-ot{Byte / Int16 / UInt16 / UInt32 / Int32 / Float32 / Float64 /
                   CInt16 / CInt32 / CFloat32 / CFloat64}][-strict]
              [-of format][-b band][-mask band][-expand{gray | rgb | rgba}]
              [-outsize xsize[%] ysize[%]]
              [-unscale][-scale[_bn][src_min src_max[dst_min dst_max]]] *
    [-exponent[_bn] exp_val] *
    [-srcwin xoff yoff xsize ysize][-projwin ulx uly lrx lry][-epo][-eco]
                                   [-a_srs srs_def][-a_ullr ulx uly lrx lry][-a_nodata value]
                                   [-gcp pixel line easting northing[elevation]] *
    [-mo "META-TAG=VALUE"] * [-q][-sds][-co "NAME=VALUE"] * [-stats][-norat] src_dataset dst_dataset
</code></pre>
<h2>DESCRIPTION</h2>
<p> The gdal_translate utility can be used to convert raster data between different formats, potentially performing some operations like subsettings, resampling, and rescaling pixels in the process. </p>
<dl>
<dt><code>-ot</code>: <i>type</i></p>
<dd> For the output bands to be of the indicated data type.</p>
<dt><code>-strict</code>:</p>
<dd> Don&#8217;t be forgiving of mismatches and lost data when translating to the output format.</p>
<dt><code>-of</code> <i>format</i>:</p>
<dd> Select the output format. The default is GeoTIFF (GTiff). Use the short format name.</p>
<dt><code>-b</code> <i>band</i>:</p>
<dd> Select an input band <i>band</i> for output. Bands are numbered from 1. Multiple <code>-b</code> switches may be used to select a set of input bands to write to the output file, or to reorder bands. Starting with GDAL 1.8.0, <i>band</i> can also be set to &#8216;mask,1&#8217; (or just &#8216;mask&#8217;) to mean the mask band of the first band of the input dataset.</p>
<dt><code>-mask</code> <i>band</i>:</p>
<dd> (GDAL &gt;= 1.8.0) Select an input band <i>band</i> to create output dataset mask band. Bands are numbered from 1. <i>band</i> can be set to &#8216;none&#8217; to avoid copying the global mask of the input dataset if it exists. Otherwise it is copied by default (&#8216;auto&#8217;), unless the mask is an alpha channel, or if it is explicitly used to be a regular band of the output dataset (&#8216;-b mask&#8217;). <i>band</i> can also be set to &#8216;mask,1&#8217; (or just &#8216;mask&#8217;) to mean the mask band of the 1st band of the input dataset.</p>
<dt><code>-expand</code> <i>gray|rgb|rgba</i>:</p>
<dd> (From GDAL 1.6.0) To expose a dataset with 1 band with a color table as a dataset with 3 (RGB) or 4 (RGBA) bands. Useful for output drivers such as JPEG, JPEG2000, MrSID, ECW that don&#8217;t support color indexed datasets. The &#8216;gray&#8217; value (from GDAL 1.7.0) enables to expand a dataset with a color table that only contains gray levels to a gray indexed dataset.</p>
<dt><code>-outsize</code> <i>xsize[%] ysize[%]</i>:</p>
<dd> Set the size of the output file. Outsize is in pixels and lines unless &#8216;%&#8217; is attached in which case it is as a fraction of the input image size.</p>
<dt><code>-scale</code> <i>[src_min src_max [dst_min dst_max]]</i>:</p>
<dd> Rescale the input pixels values from the range <i>src_min</i> to <i>src_max</i> to the range <i>dst_min</i> to <i>dst_max</i>. If omitted the output range is 0 to 255. If omitted the input range is automatically computed from the source data. Before GDAL 1.11, it can be specified only once, and in that case, it applies to all bands of the output dataset. Starting with GDAL 1.11, -scale can be repeated several times (if specified only once, it also applies to all bands of the output dataset), so as to specify per band parameters. It is also possible to use the &#8216;-scale_bn&#8217; syntax where bn is a band number (e.g. &#8216;-scale_2&#8217; for the 2nd band of the output dataset) to specify the parameters of one or several specific bands.</p>
<dt><code>-exponent</code> <i> exp_val</i>:</p>
<dd> (From GDAL 1.11) To apply non-linear scaling with a power function. exp_val is the exponent of the power function (must be postive). This option must be used with the -scale option. If specified only once, -exponent applies to all bands of the output image. It can be repeated several times so as to specify per band parameters. It is also possible to use the &#8216;-exponent_bn&#8217; syntax where bn is a band number (e.g. &#8216;-exponent_2&#8217; for the 2nd band of the output dataset) to specify the parameters of one or several specific bands.</p>
<dt><code>-unscale</code>:</p>
<dd> Apply the scale/offset metadata for the bands to convert scaled values to unscaled values. It is also often necessary to reset the output datatype with the <code>-ot</code> switch.</p>
<dt><code>-srcwin</code> <i>xoff yoff xsize ysize</i>:</p>
<dd> Selects a subwindow from the source image for copying based on pixel/line location.</p>
<dt><code>-projwin</code> <i>ulx uly lrx lry</i>:</p>
<dd> Selects a subwindow from the source image for copying (like <code>-srcwin</code>) but with the corners given in georeferenced coordinates.</p>
<dt><code>-epo</code>: (Error when Partially Outside)</p>
<dd> (GDAL &gt;= 1.10) If this option is set, <code>-srcwin</code> or <code>-projwin</code> values that falls partially outside the source raster extent will be considered as an error. The default behaviour starting with GDAL 1.10 is to accept such requests, when they were considered as an error before.</p>
<dt><code>-eco</code>: (Error when Completely Outside)</p>
<dd> (GDAL &gt;= 1.10) Same as <code>-epo</code>, except that the criterion for erroring out is when the request falls completely outside the source raster extent.</p>
<dt><code>-a_srs</code> <i>srs_def</i>:</p>
<dd> Override the projection for the output file. The <i>srs_def</i> may be any of the usual GDAL/OGR forms, complete WKT, PROJ.4, EPSG:n or a file containing the WKT.</p>
<dt><code>-a_ullr</code> <i>ulx uly lrx lry</i>:</p>
<dd> Assign/override the georeferenced bounds of the output file. This assigns georeferenced bounds to the output file, ignoring what would have been derived from the source file.</p>
<dt><code>-a_nodata</code> <i>value</i>:</p>
<dd> Assign a specified nodata value to output bands. Starting with GDAL 1.8.0, can be set to <i>none</i> to avoid setting a nodata value to the output file if one exists for the source file</p>
<dt><code>-mo</code> <i>&#8216;META-TAG=VALUE&#8217;</i>:</p>
<dd> Passes a metadata key and value to set on the output dataset if possible.</p>
<dt><code>-co</code> <i>&#8216;NAME=VALUE&#8217;</i>:</p>
<dd> Passes a creation option to the output format driver. Multiple <code>-co</code> options may be listed. See format specific documentation for legal creation options for each format.</p>
<dt><code>-gcp</code> <i>pixel line easting northing elevation</i>:</p>
<dd> Add the indicated ground control point to the output dataset. This option may be provided multiple times to provide a set of GCPs.</p>
<dt><code>-q</code>:</p>
<dd> Suppress progress monitor and other non-error output.</p>
<dt><code>-sds</code>:</p>
<dd> Copy all subdatasets of this file to individual output files. Use with formats like HDF or OGDI that have subdatasets. The output file naming scheme has changed in GDAL 1.11 (e.g. ofile_1.tif, ofile_2.tif).</p>
<dt><code>-stats</code>:</p>
<dd> (GDAL &gt;= 1.8.0) Force (re)computation of statistics.</p>
<dt><code>-norat</code></p>
<dd> (GDAL &gt;= 1.11) Do not copy source RAT into destination dataset.</p>
<dt><i>src_dataset</i>:</p>
<dd> The source dataset name. It can be either file name, URL of data source or subdataset name for multi-dataset files.</p>
<dt><i>dst_dataset</i>:</p>
<dd> The destination file name.</dl>
<h2>EXAMPLE</h2>
<pre>
gdal_translate -of GTiff -co &quot;TILED=YES&quot; utm.tif utm_tiled.tif
</pre>
<p> Starting with GDAL 1.8.0, to create a JPEG-compressed TIFF with internal mask from a RGBA dataset : </p>
<pre>
gdal_translate rgba.tif withmask.tif -b 1 -b 2 -b 3 -mask 4 -co COMPRESS=JPEG -co PHOTOMETRIC=YCBCR --config GDAL_TIFF_INTERNAL_MASK YES
</pre>
<p> Starting with GDAL 1.8.0, to create a RGBA dataset from a RGB dataset with a mask : </p>
<pre>
gdal_translate withmask.tif rgba.tif -b 1 -b 2 -b 3 -b mask
</pre>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com, Silke Reimer silke [at] intevation.de </p>
<h2>Index</h2>
