---
title: "gdaltindex(1)"
name: "gdaltindex"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdaltindex/"
description: "gdaltindex – gdaltindex Builds a shapefile as a raster tileindex"
---

<h2 class="name">NAME</h2>
<p> gdaltindex &#8211; gdaltindex Builds a shapefile as a raster tileindex </p>
<h2>SYNOPSIS</h2>
<pre><code>
gdaltindex [-f format] [-tileindex field_name] [-write_absolute_path]
           [-skip_different_projection] [-t_srs target_srs]
           [-src_srs_name field_name] [-src_srs_format [AUTO|WKT|EPSG|PROJ]
           [-lyr_name name] index_file [gdal_file]*
</code></pre>
<h2>DESCRIPTION</h2>
<p> This program builds a shapefile with a record for each input raster file, an attribute containing the filename, and a polygon geometry outlining the raster. This output is suitable for use with MapServer as a raster tileindex. </p>
<dl>
<dt><code>-f</code> format:</p>
<dd> (GDAL &gt;= 1.11)</dl>
<p> The OGR format of the output tile index file. Default is Esri Shapefile. </p>
<dl>
<dt><code>-tileindex</code> field_name:</p>
<dd></dl>
<p> The output field name to hold the file path/location to the indexed rasters. The default tile index field name is location. </p>
<dl>
<dt><code>-write_absolute_path</code>:</p>
<dd></dl>
<p> The absolute path to the raster files is stored in the tile index file. By default the raster filenames will be put in the file exactly as they are specified on the command line. </p>
<dl>
<dt><code>-skip_different_projection</code>:</p>
<dd></dl>
<p> Only files with same projection as files already inserted in the tileindex will be inserted (unless -t_srs is specified). Default does not check projection and accepts all inputs. </p>
<dl>
<dt><code>-t_srs</code> target_srs:</p>
<dd></dl>
<p> Geometries of input files will be transformed to the desired target coordinate reference system. Using this option generates files that are not compatible with MapServer &lt; 6.4. Default creates simple rectangular polygons in the same coordinate reference system as the input rasters. </p>
<dl>
<dt><code>-src_srs_name</code> field_name:</p>
<dd> (GDAL &gt;= 1.11)</dl>
<p> The name of the field to store the SRS of each tile. This field name can be used as the value of the TILESRS keyword in MapServer &gt;= 6.4. </p>
<dl>
<dt><code>-src_srs_format</code> type:</p>
<dd> (GDAL &gt;= 1.11)</dl>
<p> The format in which the SRS of each tile must be written. Types can be AUTO, WKT, EPSG, PROJ. </p>
<dl>
<dt><code>-lyr_name</code> name:</p>
<dd></dl>
<p> Layer name to create/append to in the output tile index file. </p>
<dl>
<dt><code>index_file</code>:</p>
<dd></dl>
<p> The name of the output file to create/append to. The default shapefile will be created if it doesn&#8217;t already exist, otherwise it will append to the existing file. </p>
<dl>
<dt><code>gdal_file</code>:</p>
<dd></dl>
<p> The input GDAL raster files, can be multiple files separated by spaces. Wildcards my also be used. Stores the file locations in the same style as specified here, unless -write_absolute_path option is also used. </p>
<h2>EXAMPLES</h2>
<p> Produce a shapefile (doq_index.shp) with a record for every image that the utility found in the doq folder. Each record holds information that points to the location of the image and also a bounding rectangle shape showing the bounds of the image: </p>
<pre>
gdaltindex doq_index.shp doq/*.tif
</pre>
<p> The -t_srs option can also be used to transform all input rasters into the same output projection: </p>
<pre>
gdaltindex -t_srs EPSG:4326 -src_srs_name src_srs tile_index_mixed_srs.shp *.tif
</pre>
<h2>AUTHOR</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com </p>
<h2>Index</h2>
