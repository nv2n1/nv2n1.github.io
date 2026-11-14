---
title: "gdal_grid(1)"
name: "gdal_grid"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdal_grid/"
description: "gdal_grid – gdal_grid creates regular grid from the scattered data"
---

<h2 class="name">NAME</h2>
<p> gdal_grid &#8211; gdal_grid creates regular grid from the scattered data </p>
<h2>SYNOPSIS</h2>
<pre><code>
gdal_grid[-ot{Byte / Int16 / UInt16 / UInt32 / Int32 / Float32 / Float64 /
              CInt16 / CInt32 / CFloat32 / CFloat64}]
         [-of format][-co "NAME=VALUE"]
         [-zfield field_name][-z_increase increase_value][-z_multiply multiply_value]
         [-a_srs srs_def][-spat xmin ymin xmax ymax]
         [-clipsrc&lt;xmin ymin xmax ymax&gt; | WKT | datasource | spat_extent]
         [-clipsrcsql sql_statement][-clipsrclayer layer]
         [-clipsrcwhere expression]
         [-l layername] *
    [-where expression][-sql select_statement]
                       [-txe xmin xmax][-tye ymin ymax][-outsize xsize ysize]
                       [-a algorithm[:parameter1 = value1] * ][-q]&lt;src_datasource&gt;&lt;dst_filename&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> This program creates regular grid (raster) from the scattered data read from the OGR datasource. Input data will be interpolated to fill grid nodes with values, you can choose from various interpolation methods. </p>
<p> Starting with GDAL 1.10, it is possible to set the <code>GDAL_NUM_THREADS</code> configuration option to parallelize the processing. The value to specify is the number of worker threads, or <i>ALL_CPUS</i> to use all the cores/CPUs of the computer. </p>
<dl>
<dt><code>-ot</code> <i>type</i>:</p>
<dd> For the output bands to be of the indicated data type.</dl>
<dl>
<dt><code>-of</code> <i>format</i>:</p>
<dd> Select the output format. The default is GeoTIFF (GTiff). Use the short format name.</dl>
<dl>
<dt><code>-txe</code> <i>xmin xmax</i>:</p>
<dd> Set georeferenced X extents of output file to be created.</dl>
<dl>
<dt><code>-tye</code> <i>ymin ymax</i>:</p>
<dd> Set georeferenced Y extents of output file to be created.</dl>
<dl>
<dt><code>-outsize</code> <i>xsize ysize</i>:</p>
<dd> Set the size of the output file in pixels and lines.</dl>
<dl>
<dt><code>-a_srs</code> <i>srs_def</i>:</p>
<dd> Override the projection for the output file. The <i>srs_def</i> may be any of the usual GDAL/OGR forms, complete WKT, PROJ.4, EPSG:n or a file containing the WKT.</dl>
<dl>
<dt><code>-zfield</code> <i>field_name</i>:</p>
<dd> Identifies an attribute field on the features to be used to get a Z value from. This value overrides Z value read from feature geometry record (naturally, if you have a Z value in geometry, otherwise you have no choice and should specify a field name containing Z value).</dl>
<dl>
<dt><code>-z_increase</code> <i>increase_value</i>:</p>
<dd> Addition to the attribute field on the features to be used to get a Z value from. The addition should be the same unit as Z value. The result value will be Z value + Z increase value. The default value is 0.</dl>
<dl>
<dt><code>-z_multiply</code> <i>multiply_value</i>:</p>
<dd> This is multiplication ratio for Z field. This can be used for shift from e.g. foot to meters or from elevation to deep. The result value will be (Z value + Z increase value) * Z multiply value. The default value is 1.</dl>
<dl>
<dt><code>-a</code> <i>[algorithm[:parameter1=value1][:parameter2=value2]&#8230;]</i>:</p>
<dd> Set the interpolation algorithm or data metric name and (optionally) its parameters. See <code>INTERPOLATION ALGORITHMS</code> and <code>DATA METRICS</code> sections for further discussion of available options.</dl>
<dl>
<dt><code>-spat</code> <i>xmin ymin xmax ymax</i>:</p>
<dd> Adds a spatial filter to select only features contained within the bounding box described by (xmin, ymin) &#8211; (xmax, ymax).</dl>
<dl>
<dt><code>-clipsrc</code><i> [xmin ymin xmax ymax]|WKT|datasource|spat_extent</i>:</p>
<dd> Adds a spatial filter to select only features contained within the specified bounding box (expressed in source SRS), WKT geometry (POLYGON or MULTIPOLYGON), from a datasource or to the spatial extent of the <code>-spat</code> option if you use the <i>spat_extent</i> keyword. When specifying a datasource, you will generally want to use it in combination of the <code>-clipsrclayer</code>, <code>-clipsrcwhere</code> or <code>-clipsrcsql</code> options.</dl>
<dl>
<dt><code>-clipsrcsql</code> <i>sql_statement</i>:</p>
<dd> Select desired geometries using an SQL query instead.</dl>
<dl>
<dt><code>-clipsrclayer</code> <i>layername</i>:</p>
<dd> Select the named layer from the source clip datasource.</dl>
<dl>
<dt><code>-clipsrcwhere</code> <i>expression</i>:</p>
<dd> Restrict desired geometries based on attribute query.</dl>
<dl>
<dt><code>-l</code> <i>layername</i>:</p>
<dd> Indicates the layer(s) from the datasource that will be used for input features. May be specified multiple times, but at least one layer name or a <code>-sql</code> option must be specified.</dl>
<dl>
<dt><code>-where</code> <i>expression</i>:</p>
<dd> An optional SQL WHERE style query expression to be applied to select features to process from the input layer(s).</dl>
<dl>
<dt><code>-sql</code> <i>select_statement</i>:</p>
<dd> An SQL statement to be evaluated against the datasource to produce a virtual layer of features to be processed.</dl>
<dl>
<dt><code>-co</code> <i>&#8216;NAME=VALUE&#8217;</i>:</p>
<dd> Passes a creation option to the output format driver. Multiple <code>-co</code> options may be listed. See format specific documentation for legal creation options for each format.</dl>
<dl>
<dt><code>-q</code>:</p>
<dd> Suppress progress monitor and other non-error output.</dl>
<dl>
<dt><i>src_datasource</i>:</p>
<dd> Any OGR supported readable datasource.</dl>
<dl>
<dt><i>dst_filename</i>:</p>
<dd> The GDAL supported output file.</dl>
<h2>INTERPOLATION ALGORITHMS</h2>
<p> There are number of interpolation algorithms to choose from.</p>
<h3>invdist</h3>
<p> Inverse distance to a power. This is default algorithm. It has following parameters: </p>
<dl>
<dt><i>power</i>:</p>
<dd> Weighting power (default 2.0).</p>
<dt><i>smoothing</i>:</p>
<dd> Smoothing parameter (default 0.0).</p>
<dt><i>radius1</i>:</p>
<dd> The first radius (X axis if rotation angle is 0) of search ellipse. Set this parameter to zero to use whole point array. Default is 0.0.</p>
<dt><i>radius2</i>:</p>
<dd> The second radius (Y axis if rotation angle is 0) of search ellipse. Set this parameter to zero to use whole point array. Default is 0.0.</p>
<dt><i>angle</i>:</p>
<dd> Angle of search ellipse rotation in degrees (counter clockwise, default 0.0).</p>
<dt><i>max_points</i>:</p>
<dd> Maximum number of data points to use. Do not search for more points than this number. This is only used if search ellipse is set (both radii are non-zero). Zero means that all found points should be used. Default is 0.</p>
<dt><i>min_points</i>:</p>
<dd> Minimum number of data points to use. If less amount of points found the grid node considered empty and will be filled with NODATA marker. This is only used if search ellipse is set (both radii are non-zero). Default is 0.</p>
<dt><i>nodata</i>:</p>
<dd> NODATA marker to fill empty points (default 0.0).</dl>
<h3>average</h3>
<p> Moving average algorithm. It has following parameters: </p>
<dl>
<dt><i>radius1</i>:</p>
<dd> The first radius (X axis if rotation angle is 0) of search ellipse. Set this parameter to zero to use whole point array. Default is 0.0.</p>
<dt><i>radius2</i>:</p>
<dd> The second radius (Y axis if rotation angle is 0) of search ellipse. Set this parameter to zero to use whole point array. Default is 0.0.</p>
<dt><i>angle</i>:</p>
<dd> Angle of search ellipse rotation in degrees (counter clockwise, default 0.0).</p>
<dt><i>min_points</i>:</p>
<dd> Minimum number of data points to use. If less amount of points found the grid node considered empty and will be filled with NODATA marker. Default is 0.</p>
<dt><i>nodata</i>:</p>
<dd> NODATA marker to fill empty points (default 0.0).</dl>
<p> Note, that it is essential to set search ellipse for moving average method. It is a window that will be averaged when computing grid nodes values.</p>
<h3>nearest</h3>
<p> Nearest neighbor algorithm. It has following parameters: </p>
<dl>
<dt><i>radius1</i>:</p>
<dd> The first radius (X axis if rotation angle is 0) of search ellipse. Set this parameter to zero to use whole point array. Default is 0.0.</p>
<dt><i>radius2</i>:</p>
<dd> The second radius (Y axis if rotation angle is 0) of search ellipse. Set this parameter to zero to use whole point array. Default is 0.0.</p>
<dt><i>angle</i>:</p>
<dd> Angle of search ellipse rotation in degrees (counter clockwise, default 0.0).</p>
<dt><i>nodata</i>:</p>
<dd> NODATA marker to fill empty points (default 0.0).</dl>
<h2>DATA METRICS</h2>
<p> Besides the interpolation functionality <code>gdal_grid</code> can be used to compute some data metrics using the specified window and output grid geometry. These metrics are: </p>
<dl>
<dt><i>minimum</i>:</p>
<dd> Minimum value found in grid node search ellipse.</dl>
<dl>
<dt><i>maximum</i>:</p>
<dd> Maximum value found in grid node search ellipse.</dl>
<dl>
<dt><i>range</i>:</p>
<dd> A difference between the minimum and maximum values found in grid node search ellipse.</dl>
<dl>
<dt><i>count</i>:</p>
<dd> A number of data points found in grid node search ellipse.</dl>
<dl>
<dt><i>average_distance</i>:</p>
<dd> An average distance between the grid node (center of the search ellipse) and all of the data points found in grid node search ellipse.</dl>
<dl>
<dt><i>average_distance_pts</i>:</p>
<dd> An average distance between the data points found in grid node search ellipse. The distance between each pair of points within ellipse is calculated and average of all distances is set as a grid node value.</dl>
<p> All the metrics have the same set of options: </p>
<dl>
<dt><i>radius1</i>:</p>
<dd> The first radius (X axis if rotation angle is 0) of search ellipse. Set this parameter to zero to use whole point array. Default is 0.0.</p>
<dt><i>radius2</i>:</p>
<dd> The second radius (Y axis if rotation angle is 0) of search ellipse. Set this parameter to zero to use whole point array. Default is 0.0.</p>
<dt><i>angle</i>:</p>
<dd> Angle of search ellipse rotation in degrees (counter clockwise, default 0.0).</p>
<dt><i>min_points</i>:</p>
<dd> Minimum number of data points to use. If less amount of points found the grid node considered empty and will be filled with NODATA marker. This is only used if search ellipse is set (both radii are non-zero). Default is 0.</p>
<dt><i>nodata</i>:</p>
<dd> NODATA marker to fill empty points (default 0.0).</dl>
<h2>READING COMMA SEPARATED VALUES</h2>
<p> Often you have a text file with a list of comma separated XYZ values to work with (so called CSV file). You can easily use that kind of data source in <code>gdal_grid</code>. All you need is create a virtual dataset header (VRT) for you CSV file and use it as input datasource for <code>gdal_grid</code>. You can find details on VRT format at Virtual Format description page. </p>
<p> Here is a small example. Let we have a CSV file called <i>dem.csv</i> containing </p>
<pre>
Easting,Northing,Elevation
86943.4,891957,139.13
87124.3,892075,135.01
86962.4,892321,182.04
87077.6,891995,135.01
</pre>
<p> For above data we will create <i>dem.vrt</i> header with the following content: </p>
<pre>
&lt;OGRVRTDataSource&gt;
    &lt;OGRVRTLayer name=&quot;dem&quot;&gt;
        &lt;SrcDataSource&gt;dem.csv&lt;/SrcDataSource&gt; 
        &lt;GeometryType&gt;wkbPoint&lt;/GeometryType&gt; 
        &lt;GeometryField encoding=&quot;PointFromColumns&quot; x=&quot;Easting&quot; y=&quot;Northing&quot; z=&quot;Elevation&quot;/&gt; 
    &lt;/OGRVRTLayer&gt;
&lt;/OGRVRTDataSource&gt;
</pre>
<p> This description specifies so called 2.5D geometry with three coordinates X, Y and Z. Z value will be used for interpolation. Now you can use <i>dem.vrt</i> with all OGR programs (start with <code>ogrinfo</code> to test that everything works fine). The datasource will contain single layer called <i>&#8216;dem&#8217;</i> filled with point features constructed from values in CSV file. Using this technique you can handle CSV files with more than three columns, switch columns, etc. </p>
<p> If your CSV file does not contain column headers then it can be handled in the following way: </p>
<pre>
&lt;GeometryField encoding=&quot;PointFromColumns&quot; x=&quot;field_1&quot; y=&quot;field_2&quot; z=&quot;field_3&quot;/&gt;
</pre>
<p> Comma Separated Value description page contains details on CSV format supported by GDAL/OGR.</p>
<h2>EXAMPLE</h2>
<p> The following would create raster TIFF file from VRT datasource described in <code>READING COMMA SEPARATED VALUES</code> section using the inverse distance to a power method. Values to interpolate will be read from Z value of geometry record. </p>
<pre>
gdal_grid -a invdist:power=2.0:smoothing=1.0 -txe 85000 89000 -tye 894000 890000 -outsize 400 400 -of GTiff -ot Float64 -l dem dem.vrt dem.tiff
</pre>
<p> The next command does the same thing as the previous one, but reads values to interpolate from the attribute field specified with <code>-zfield</code> option instead of geometry record. So in this case X and Y coordinates are being taken from geometry and Z is being taken from the <i>&#8216;Elevation&#8217;</i> field. The GDAL_NUM_THREADS is also set to parallelize the computation. </p>
<pre>
gdal_grid -zfield &quot;Elevation&quot; -a invdist:power=2.0:smoothing=1.0 -txe 85000 89000 -tye 894000 890000 -outsize 400 400 -of GTiff -ot Float64 -l dem dem.vrt dem.tiff --config GDAL_NUM_THREADS ALL_CPUS
</pre>
<h2>AUTHORS</h2>
<p> Andrey Kiselev dron [at] ak4719.spb.edu </p>
<h2>Index</h2>
