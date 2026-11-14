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
<dt><code>-targetDir</code> <i>directory</i>:</p>
<dd> The directory where the tile result is created. Pyramids are stored in subdirectories numbered from 1. Created tile names have a numbering schema and contain the name of the source tiles(s)</p>
<dt><code>-of</code> <i>format</i>:</p>
<dd> Output format, defaults to GeoTIFF (GTiff).</p>
<dt><code>-co</code> <i>NAME=VALUE</i>:</p>
<dd> Creation option for output file. Multiple options can be specified.</p>
<dt><code>-ot</code> <i>datatype</i>:</p>
<dd> Force the output image bands to have a specific type. Use type names (ie. Byte, Int16,&#8230;)</p>
<dt><code>-ps</code> <i>pixelsize_x pixelsize_y</i>:</p>
<dd> Pixel size to be used for the output file. If not specified, 256 x 256 is the default</p>
<dt><code>-levels</code> <i>numberOfLevels</i>:</p>
<dd> Number of pyramids levels to build.</p>
<dt><code>-v</code>:</p>
<dd> Generate verbose output of tile operations as they are done.</p>
<dt><code>-pyramidOnly</code>:</p>
<dd> No retiling, build only the pyramids</p>
<dt><code>-r</code> <i>algorithm</i>:</p>
<dd> Resampling algorithm, default is near</p>
<dt><code>-s_srs</code> <i>srs_def</i>:</p>
<dd> Source spatial reference to use. The coordinate systems that can be passed are anything supported by the OGRSpatialReference.SetFro‐mUserInput() call, which includes EPSG PCS and GCSes (ie.EPSG:4296), PROJ.4 declarations (as above), or the name of a .prf file containing well known text. If no srs_def is given, the srs_def of the source tiles is used (if there is any). The srs_def will be propagated to created tiles (if possible) and to the optional shape file(s)</p>
<dt><code>-tileIndex</code> <i>tileIndexName</i>:</p>
<dd> The name of shape file containing the result tile(s) index</p>
<dt><code>-tileIndexField</code> <i>tileIndexFieldName</i>:</p>
<dd> The name of the attribute containing the tile name</p>
<dt><code>-csv</code> <i>csvFileName</i>:</p>
<dd> The name of the csv file containing the tile(s) georeferencing information. The file contains 5 columns: tilename,minx,maxx,miny,maxy</p>
<dt><code>-csvDelim</code> <i>column delimiter</i>:</p>
<dd> The column delimter used in the csv file, default value is a semicolon &#8216;;&#8217;</p>
<dt><code>-useDirForEachRow</code>:</p>
<dd> Normally the tiles of the base image are stored as described in <code>-targetDir</code>. For large images, some file systems have performance problems if the number of files in a directory is to big, causing gdal_retile not to finish in reasonable time. Using this parameter creates a different output structure. The tiles of the base image are stored in a subdirectory called 0, the pyramids in subdirectories numbered 1,2,&#8230;. Within each of these directories another level of subdirectories is created, numbered from 0&#8230;n, depending of how many tile rows are needed for each level. Finally, a directory contains only the the tiles for one row for a specific level. For large images a performance improvement of a factor N could be achieved.</dl>
<p> NOTE: gdal_retile.py is a Python script, and will only work if GDAL was built with Python support.</p>
<h2>AUTHORS</h2>
<p> Christian Mueller christian.mueller [at] nvoe.at </p>
<h2>Index</h2>
