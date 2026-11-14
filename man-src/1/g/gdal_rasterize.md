---
title: "gdal_rasterize(1)"
name: "gdal_rasterize"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdal_rasterize/"
description: "gdal_rasterize – gdal_rasterize burns vector geometries into a raster"
---

<h2 class="name">NAME</h2>
<p> gdal_rasterize &#8211; gdal_rasterize burns vector geometries into a raster </p>
<h2>SYNOPSIS</h2>
<pre><code>
Usage : gdal_rasterize[-b band] * [-i][-at][-burn value] * | [-a attribute_name][-3d]
                                                                                [-l layername] *
                                                                 [-where expression][-sql select_statement]
                                                                                    [-of format][-a_srs srs_def][-co "NAME=VALUE"] *
                                                                 [-a_nodata value][-init value] *
                                                                 [-te xmin ymin xmax ymax][-tr xres yres][-tap][-ts width height]
                                                                                          [-ot{Byte / Int16 / UInt16 / UInt32 / Int32 / Float32 / Float64 /
                                                                                               CInt16 / CInt32 / CFloat32 / CFloat64}][-q]&lt;src_datasource&gt;&lt;dst_filename&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> This program burns vector geometries (points, lines and polygons) into the raster band(s) of a raster image. Vectors are read from OGR supported vector formats. </p>
<p> Note that the vector data must in the same coordinate system as the raster data; on the fly reprojection is not provided. </p>
<p> Since GDAL 1.8.0, the target GDAL file can be created by gdal_rasterize. One of -tr or -ts option must be used in that case. </p>
<dl>
<dt><code>-b</code> <i>band</i>:</p>
<dd> The band(s) to burn values into. Multiple -b arguments may be used to burn into a list of bands. The default is to burn into band 1.</dl>
<dl>
<dt><code>-i</code>:</p>
<dd> Invert rasterization. Burn the fixed burn value, or the burn value associated with the first feature into all parts of the image <i>not</i> inside the provided a polygon.</dl>
<dl>
<dt><code>-at</code>:</p>
<dd> Enables the ALL_TOUCHED rasterization option so that all pixels touched by lines or polygons will be updated not just those one the line render path, or whose center point is within the polygon. Defaults to disabled for normal rendering rules.</dl>
<dl>
<dt><code>-burn</code> <i>value</i>:</p>
<dd> A fixed value to burn into a band for all objects. A list of -burn options can be supplied, one per band being written to.</dl>
<dl>
<dt><code>-a</code> <i>attribute_name</i>:</p>
<dd> Identifies an attribute field on the features to be used for a burn in value. The value will be burned into all output bands.</dl>
<dl>
<dt><code>-3d</code>:</p>
<dd> Indicates that a burn value should be extracted from the &#8216;Z&#8217; values of the feature. These values are adjusted by the burn value given by &#8216;-burn value&#8217; or &#8216;-a attribute_name&#8217; if provided. As of now, only points and lines are drawn in 3D.</dl>
<dl>
<dt><code>-l</code> <i>layername</i>:</p>
<dd> Indicates the layer(s) from the datasource that will be used for input features. May be specified multiple times, but at least one layer name or a -sql option must be specified.</dl>
<dl>
<dt><code>-where</code> <i>expression</i>:</p>
<dd> An optional SQL WHERE style query expression to be applied to select features to burn in from the input layer(s).</dl>
<dl>
<dt><code>-sql</code> <i>select_statement</i>:</p>
<dd> An SQL statement to be evaluated against the datasource to produce a virtual layer of features to be burned in.</dl>
<dl>
<dt><code>-of</code> <i>format</i>:</p>
<dd> (GDAL &gt;= 1.8.0) Select the output format. The default is GeoTIFF (GTiff). Use the short format name.</dl>
<dl>
<dt><code>-a_nodata</code> <i>value</i>:</p>
<dd> (GDAL &gt;= 1.8.0) Assign a specified nodata value to output bands.</dl>
<dl>
<dt><code>-init</code> <i>value</i>:</p>
<dd> (GDAL &gt;= 1.8.0) Pre-initialize the output image bands with these values. However, it is not marked as the nodata value in the output file. If only one value is given, the same value is used in all the bands.</dl>
<dl>
<dt><code>-a_srs</code> <i>srs_def</i>:</p>
<dd> (GDAL &gt;= 1.8.0) Override the projection for the output file. If not specified, the projection of the input vector file will be used if available. If incompatible projections between input and output files, no attempt will be made to reproject features. The <i>srs_def</i> may be any of the usual GDAL/OGR forms, complete WKT, PROJ.4, EPSG:n or a file containing the WKT.</dl>
<dl>
<dt><code>-co</code> <i>&#8216;NAME=VALUE&#8217;</i>:</p>
<dd> (GDAL &gt;= 1.8.0) Passes a creation option to the output format driver. Multiple <code>-co</code> options may be listed. See format specific documentation for legal creation options for each format.</dl>
<dl>
<dt><code>-te</code> <i>xmin ymin xmax ymax</i> :</p>
<dd> (GDAL &gt;= 1.8.0) set georeferenced extents. The values must be expressed in georeferenced units. If not specified, the extent of the output file will be the extent of the vector layers.</dl>
<dl>
<dt><code>-tr</code> <i>xres yres</i> :</p>
<dd> (GDAL &gt;= 1.8.0) set target resolution. The values must be expressed in georeferenced units. Both must be positive values.</dl>
<dl>
<dt><code>-tap</code>:</p>
<dd> (GDAL &gt;= 1.8.0) (target aligned pixels) align the coordinates of the extent of the output file to the values of the -tr, such that the aligned extent includes the minimum extent.</dl>
<dl>
<dt><code>-ts</code> <i>width height</i>:</p>
<dd> (GDAL &gt;= 1.8.0) set output file size in pixels and lines. Note that -ts cannot be used with -tr</dl>
<dl>
<dt><code>-ot</code> <i>type</i>:</p>
<dd> (GDAL &gt;= 1.8.0) For the output bands to be of the indicated data type. Defaults to Float64</dl>
<dl>
<dt><code>-q</code>:</p>
<dd> (GDAL &gt;= 1.8.0) Suppress progress monitor and other non-error output.</dl>
<dl>
<dt><i>src_datasource</i>:</p>
<dd> Any OGR supported readable datasource.</dl>
<dl>
<dt><i>dst_filename</i>:</p>
<dd> The GDAL supported output file. Must support update mode access. Before GDAL 1.8.0, gdal_rasterize could not create new output files.</dl>
<h2>EXAMPLE</h2>
<p> The following would burn all polygons from mask.shp into the RGB TIFF file work.tif with the color red (RGB = 255,0,0). </p>
<pre>
gdal_rasterize -b 1 -b 2 -b 3 -burn 255 -burn 0 -burn 0 -l mask mask.shp work.tif
</pre>
<p> The following would burn all &#8216;class A&#8217; buildings into the output elevation file, pulling the top elevation from the ROOF_H attribute. </p>
<pre>
gdal_rasterize -a ROOF_H -where 'class=&quot;A&quot;' -l footprints footprints.shp city_dem.tif
</pre>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com </p>
<h2>Index</h2>
