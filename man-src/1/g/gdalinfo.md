---

title: "gdalinfo(1)"
name: "gdalinfo"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdalinfo/"
description: "gdalinfo – gdalinfo lists information about a raster dataset"
---

<pre><code>
gdalinfo[--help - general][-mm][-stats][-hist][-nogcp][-nomd]
        [-norat][-noct][-nofl][-checksum][-proj4]
        [-listmdd][-mdd domain |`all`] *
    [-sd subdataset] datasetname
</code></pre>
<p> The gdalinfo program lists various information about a GDAL supported raster dataset.</p>
<dl>
<dt><code>-mm</code></dt>
<dd> Force computation of the actual min/max values for each band in the dataset.</dd>
<dt><code>-stats</code></dt>
<dd> Read and display image statistics. Force computation if no statistics are stored in an image.</dd>
<dt><code>-approx_stats</code></dt>
<dd> Read and display image statistics. Force computation if no statistics are stored in an image. However, they may be computed based on overviews or a subset of all tiles. Useful if you are in a hurry and don&#8217;t want precise stats.</dd>
<dt><code>-hist</code></dt>
<dd> Report histogram information for all bands.</dd>
<dt><code>-nogcp</code></dt>
<dd> Suppress ground control points list printing. It may be useful for datasets with huge amount of GCPs, such as L1B AVHRR or HDF4 MODIS which contain thousands of them.</dd>
<dt><code>-nomd</code></dt>
<dd> Suppress metadata printing. Some datasets may contain a lot of metadata strings.</dd>
<dt><code>-nrat</code></dt>
<dd> Suppress printing of raster attribute table.</dd>
<dt><code>-noct</code></dt>
<dd> Suppress printing of color table.</dd>
<dt><code>-checksum</code></dt>
<dd> Force computation of the checksum for each band in the dataset.</dd>
<dt><code>-listmdd</code></dt>
<dd> (GDAL &gt;= 1.11) List all metadata domains available for the dataset.</dd>
<dt><code>-mdd domain</code></dt>
<dd> Report metadata for the specified domain. Starting with GDAL 1.11, &#8216;all&#8217; can be used to report metadata in all domains</dd>
<dt><code>-nofl</code></dt>
<dd> (GDAL &gt;= 1.9.0) Only display the first file of the file list.</dd>
<dt><code>-sd</code> <i>subdataset</i></dt>
<dd> (GDAL &gt;= 1.9.0) If the input dataset contains several subdatasets read and display a subdataset with specified number (starting from 1). This is an alternative of giving the full subdataset name.</dd>
<dt><code>-proj4</code></dt>
<dd> (GDAL &gt;= 1.9.0) Report a PROJ.4 string corresponding to the file&#8217;s coordinate system.</dd></dl>
<p> The gdalinfo will report all of the following (if known): </p>
<dl>
<dt>&bull;</dt>
<dd> The format driver used to access the file.</dd>
<dt>&bull;</dt>
<dd> Raster size (in pixels and lines).</dd>
<dt>&bull;</dt>
<dd> The coordinate system for the file (in OGC WKT).</dd>
<dt>&bull;</dt>
<dd> The geotransform associated with the file (rotational coefficients are currently not reported).</dd>
<dt>&bull;</dt>
<dd> Corner coordinates in georeferenced, and if possible lat/long based on the full geotransform (but not GCPs).</dd>
<dt>&bull;</dt>
<dd> Ground control points.</dd>
<dt>&bull;</dt>
<dd> File wide (including subdatasets) metadata.</dd>
<dt>&bull;</dt>
<dd> Band data types.</dd>
<dt>&bull;</dt>
<dd> Band color interpretations.</dd>
<dt>&bull;</dt>
<dd> Band block size.</dd>
<dt>&bull;</dt>
<dd> Band descriptions.</dd>
<dt>&bull;</dt>
<dd> Band min/max values (internally known and possibly computed).</dd>
<dt>&bull;</dt>
<dd> Band checksum (if computation asked).</dd>
<dt>&bull;</dt>
<dd> Band NODATA value.</dd>
<dt>&bull;</dt>
<dd> Band overview resolutions available.</dd>
<dt>&bull;</dt>
<dd> Band unit type (i.e.. &#8216;meters&#8217; or &#8216;feet&#8217; for elevation bands).</dd>
<dt>&bull;</dt>
<dd> Band pseudo-color tables.</dd></dl>
<h2>EXAMPLE</h2>
<pre><code>
gdalinfo ~ / openev / utm.tif Driver : GTiff / GeoTIFF Size is 512, 512 Coordinate System is : PROJCS["NAD27 / UTM zone 11N", GEOGCS["NAD27", DATUM["North_American_Datum_1927", SPHEROID["Clarke 1866", 6378206.4, 294.978698213901]], PRIMEM["Greenwich", 0], UNIT["degree", 0.0174532925199433]], PROJECTION["Transverse_Mercator"], PARAMETER["latitude_of_origin", 0], PARAMETER["central_meridian", -117], PARAMETER["scale_factor", 0.9996], PARAMETER["false_easting", 500000], PARAMETER["false_northing", 0], UNIT["metre", 1]] Origin = (440720.000000, 3751320.000000)Pixel Size = (60.000000, -60.000000)Corner Coordinates : Upper Left(440720.000, 3751320.000)(117d38'28.21 "W, 33d54'8.47" N) Lower Left(440720.000, 3720600.000)(117d38'20.79 "W, 33d37'31.04" N) Upper Right(471440.000, 3751320.000)(117d18'32.07 "W, 33d54'13.08" N) Lower Right(471440.000, 3720600.000)(117d18'28.50 "W, 33d37'35.61" N) Center(456080.000, 3735960.000)(117d28'27.39 "W, 33d45'52.46" N) Band 1 Block = 512x16 Type = Byte, ColorInterp = Gray
</code></pre>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com, Silke Reimer silke [at] intevation.de </p>
