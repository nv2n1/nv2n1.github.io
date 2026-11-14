---
title: "gdalinfo(1)"
name: "gdalinfo"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdalinfo/"
description: "gdalinfo – gdalinfo lists information about a raster dataset"
---

<h2 class="name">NAME</h2>
<p> gdalinfo &#8211; gdalinfo lists information about a raster dataset </p>
<h2>SYNOPSIS</h2>
<pre><code>
gdalinfo[--help - general][-mm][-stats][-hist][-nogcp][-nomd]
        [-norat][-noct][-nofl][-checksum][-proj4]
        [-listmdd][-mdd domain |`all`] *
    [-sd subdataset] datasetname
</code></pre>
<h2>DESCRIPTION</h2>
<p> The gdalinfo program lists various information about a GDAL supported raster dataset.</p>
<dl>
<dt><code>-mm</code></p>
<dd> Force computation of the actual min/max values for each band in the dataset.</p>
<dt><code>-stats</code></p>
<dd> Read and display image statistics. Force computation if no statistics are stored in an image.</p>
<dt><code>-approx_stats</code></p>
<dd> Read and display image statistics. Force computation if no statistics are stored in an image. However, they may be computed based on overviews or a subset of all tiles. Useful if you are in a hurry and don&#8217;t want precise stats.</p>
<dt><code>-hist</code></p>
<dd> Report histogram information for all bands.</p>
<dt><code>-nogcp</code></p>
<dd> Suppress ground control points list printing. It may be useful for datasets with huge amount of GCPs, such as L1B AVHRR or HDF4 MODIS which contain thousands of them.</p>
<dt><code>-nomd</code></p>
<dd> Suppress metadata printing. Some datasets may contain a lot of metadata strings.</p>
<dt><code>-nrat</code></p>
<dd> Suppress printing of raster attribute table.</p>
<dt><code>-noct</code></p>
<dd> Suppress printing of color table.</p>
<dt><code>-checksum</code></p>
<dd> Force computation of the checksum for each band in the dataset.</p>
<dt><code>-listmdd</code></p>
<dd> (GDAL &gt;= 1.11) List all metadata domains available for the dataset.</p>
<dt><code>-mdd domain</code></p>
<dd> Report metadata for the specified domain. Starting with GDAL 1.11, &#8216;all&#8217; can be used to report metadata in all domains</p>
<dt><code>-nofl</code></p>
<dd> (GDAL &gt;= 1.9.0) Only display the first file of the file list.</p>
<dt><code>-sd</code> <i>subdataset</i></p>
<dd> (GDAL &gt;= 1.9.0) If the input dataset contains several subdatasets read and display a subdataset with specified number (starting from 1). This is an alternative of giving the full subdataset name.</p>
<dt><code>-proj4</code></p>
<dd> (GDAL &gt;= 1.9.0) Report a PROJ.4 string corresponding to the file&#8217;s coordinate system.</dl>
<p> The gdalinfo will report all of the following (if known): </p>
<dl>
<dt>&bull;</p>
<dd> The format driver used to access the file.</p>
<dt>&bull;</p>
<dd> Raster size (in pixels and lines).</p>
<dt>&bull;</p>
<dd> The coordinate system for the file (in OGC WKT).</p>
<dt>&bull;</p>
<dd> The geotransform associated with the file (rotational coefficients are currently not reported).</p>
<dt>&bull;</p>
<dd> Corner coordinates in georeferenced, and if possible lat/long based on the full geotransform (but not GCPs).</p>
<dt>&bull;</p>
<dd> Ground control points.</p>
<dt>&bull;</p>
<dd> File wide (including subdatasets) metadata.</p>
<dt>&bull;</p>
<dd> Band data types.</p>
<dt>&bull;</p>
<dd> Band color interpretations.</p>
<dt>&bull;</p>
<dd> Band block size.</p>
<dt>&bull;</p>
<dd> Band descriptions.</p>
<dt>&bull;</p>
<dd> Band min/max values (internally known and possibly computed).</p>
<dt>&bull;</p>
<dd> Band checksum (if computation asked).</p>
<dt>&bull;</p>
<dd> Band NODATA value.</p>
<dt>&bull;</p>
<dd> Band overview resolutions available.</p>
<dt>&bull;</p>
<dd> Band unit type (i.e.. &#8216;meters&#8217; or &#8216;feet&#8217; for elevation bands).</p>
<dt>&bull;</p>
<dd> Band pseudo-color tables.</dl>
<h2>EXAMPLE</h2>
<pre><code>
gdalinfo ~ / openev / utm.tif Driver : GTiff / GeoTIFF Size is 512, 512 Coordinate System is : PROJCS["NAD27 / UTM zone 11N", GEOGCS["NAD27", DATUM["North_American_Datum_1927", SPHEROID["Clarke 1866", 6378206.4, 294.978698213901]], PRIMEM["Greenwich", 0], UNIT["degree", 0.0174532925199433]], PROJECTION["Transverse_Mercator"], PARAMETER["latitude_of_origin", 0], PARAMETER["central_meridian", -117], PARAMETER["scale_factor", 0.9996], PARAMETER["false_easting", 500000], PARAMETER["false_northing", 0], UNIT["metre", 1]] Origin = (440720.000000, 3751320.000000)Pixel Size = (60.000000, -60.000000)Corner Coordinates : Upper Left(440720.000, 3751320.000)(117d38'28.21 "W, 33d54'8.47" N) Lower Left(440720.000, 3720600.000)(117d38'20.79 "W, 33d37'31.04" N) Upper Right(471440.000, 3751320.000)(117d18'32.07 "W, 33d54'13.08" N) Lower Right(471440.000, 3720600.000)(117d18'28.50 "W, 33d37'35.61" N) Center(456080.000, 3735960.000)(117d28'27.39 "W, 33d45'52.46" N) Band 1 Block = 512x16 Type = Byte, ColorInterp = Gray
</code></pre>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com, Silke Reimer silke [at] intevation.de </p>
<h2>Index</h2>
