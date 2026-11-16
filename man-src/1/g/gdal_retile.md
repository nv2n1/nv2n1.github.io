---
title: "gdal_retile(1)"
name: "gdal_retile"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdal_retile/"
description: "gdal_retile – gdal_retile.py gdal_retile.py retiles a set of tiles and/or build tiled pyramid levels"
---

<h2 class="name">NAME</h2>
<p> gdal_retile &#8211; gdal_retile.py gdal_retile.py retiles a set of tiles and/or build tiled pyramid levels </p>
<h2>SYNOPSIS</h2>
<pre><code>
gdal_retile.py[-v][-co NAME = VALUE] * [-of out_format][-ps pixelWidth pixelHeight]
                                                       [-ot{Byte / Int16 / UInt16 / UInt32 / Int32 / Float32 / Float64 /
                                                            CInt16 / CInt32 / CFloat32 / CFloat64}]'
                                                           [-tileIndex tileIndexName[-tileIndexField tileIndexFieldName]]
                                                           [-csv fileName[-csvDelim delimiter]]
                                                           [-s_srs srs_def][-pyramidOnly]
                                                           [-r{near / bilinear / cubic / cubicspline / lanczos}] -
    levels numberoflevels
        [-useDirForEachRow] -
    targetDir TileDirectory input_files.fi
</code></pre>
<h2>DESCRIPTION</h2>
<p> This utility will retile a set of input tile(s). All the input tile(s) must be georeferenced in the same coordinate system and have a matching number of bands. Optionally pyramid levels are generated. It is possible to generate shape file(s) for the tiled output. </p>
<p> If your number of input tiles exhausts the command line buffer, use the general &#8211;optfile option </p>
<dl>
<dt><code>-targetDir</code> <i>directory</i>:</dt>
<dd> The directory where the tile result is created. Pyramids are stored in subdirectories numbered from 1. Created tile names have a numbering schema and contain the name of the source tiles(s)</dd>
<dt><code>-of</code> <i>format</i>:</dt>
<dd> Output format, defaults to GeoTIFF (GTiff).</dd>
<dt><code>-co</code> <i>NAME=VALUE</i>:</dt>
<dd> Creation option for output file. Multiple options can be specified.</dd>
<dt><code>-ot</code> <i>datatype</i>:</dt>
<dd> Force the output image bands to have a specific type. Use type names (ie. Byte, Int16,&#8230;)</dd>
<dt><code>-ps</code> <i>pixelsize_x pixelsize_y</i>:</dt>
<dd> Pixel size to be used for the output file. If not specified, 256 x 256 is the default</dd>
<dt><code>-levels</code> <i>numberOfLevels</i>:</dt>
<dd> Number of pyramids levels to build.</dd>
<dt><code>-v</code>:</dt>
<dd> Generate verbose output of tile operations as they are done.</dd>
<dt><code>-pyramidOnly</code>:</dt>
<dd> No retiling, build only the pyramids</dd>
<dt><code>-r</code> <i>algorithm</i>:</dt>
<dd> Resampling algorithm, default is near</dd>
<dt><code>-s_srs</code> <i>srs_def</i>:</dt>
<dd> Source spatial reference to use. The coordinate systems that can be passed are anything supported by the OGRSpatialReference.SetFro‐mUserInput() call, which includes EPSG PCS and GCSes (ie.EPSG:4296), PROJ.4 declarations (as above), or the name of a .prf file containing well known text. If no srs_def is given, the srs_def of the source tiles is used (if there is any). The srs_def will be propagated to created tiles (if possible) and to the optional shape file(s)</dd>
<dt><code>-tileIndex</code> <i>tileIndexName</i>:</dt>
<dd> The name of shape file containing the result tile(s) index</dd>
<dt><code>-tileIndexField</code> <i>tileIndexFieldName</i>:</dt>
<dd> The name of the attribute containing the tile name</dd>
<dt><code>-csv</code> <i>csvFileName</i>:</dt>
<dd> The name of the csv file containing the tile(s) georeferencing information. The file contains 5 columns: tilename,minx,maxx,miny,maxy</dd>
<dt><code>-csvDelim</code> <i>column delimiter</i>:</dt>
<dd> The column delimter used in the csv file, default value is a semicolon &#8216;;&#8217;</dd>
<dt><code>-useDirForEachRow</code>:</dt>
<dd> Normally the tiles of the base image are stored as described in <code>-targetDir</code>. For large images, some file systems have performance problems if the number of files in a directory is to big, causing gdal_retile not to finish in reasonable time. Using this parameter creates a different output structure. The tiles of the base image are stored in a subdirectory called 0, the pyramids in subdirectories numbered 1,2,&#8230;. Within each of these directories another level of subdirectories is created, numbered from 0&#8230;n, depending of how many tile rows are needed for each level. Finally, a directory contains only the the tiles for one row for a specific level. For large images a performance improvement of a factor N could be achieved.</dd></dl>
<p> NOTE: gdal_retile.py is a Python script, and will only work if GDAL was built with Python support.</p>
<h2>AUTHORS</h2>
<p> Christian Mueller christian.mueller [at] nvoe.at </p>
<h2>Index</h2>
