---
title: "ogrinfo(1)"
name: "ogrinfo"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ogrinfo/"
description: "ogrinfo – ogrinfo lists information about an OGR supported data source"
---

<h2 class="name">NAME</h2>
<p> ogrinfo &#8211; ogrinfo lists information about an OGR supported data source </p>
<h2>SYNOPSIS</h2>
<pre><code>
ogrinfo[--help - general][-ro][-q][-where restricted_where]
       [-spat xmin ymin xmax ymax][-geomfield field][-fid fid]
       [-sql statement][-dialect dialect][-al][-so][-fields = {YES / NO}]
       [-geom = {YES / NO / SUMMARY}][--formats] datasource_name[layer[layer...]]
           .fi
</code></pre>
<h2>DESCRIPTION</h2>
<p> The ogrinfo program lists various information about an OGR supported data source to stdout (the terminal). </p>
<dl>
<dt><code>-ro</code>:</p>
<dd> Open the data source in read-only mode.</p>
<dt><code>-al</code>:</p>
<dd> List all features of all layers (used instead of having to give layer names as arguments).</p>
<dt><code>-so</code>:</p>
<dd> Summary Only: supress listing of features, show only the summary information like projection, schema, feature count and extents.</p>
<dt><code>-q</code>:</p>
<dd> Quiet verbose reporting of various information, including coordinate system, layer schema, extents, and feature count.</p>
<dt><code>-where</code> <i>restricted_where</i>:</p>
<dd> An attribute query in a restricted form of the queries used in the SQL WHERE statement. Only features matching the attribute query will be reported.</p>
<dt><code>-sql</code> <i>statement</i>:</p>
<dd> Execute the indicated SQL statement and return the result.</p>
<dt><code>-dialect</code> <i>dialect</i>:</p>
<dd> SQL dialect. In some cases can be used to use (unoptimized) OGR SQL instead of the native SQL of an RDBMS by passing OGRSQL. Starting with GDAL 1.10, the &#8216;SQLITE&#8217; dialect can also be used with any datasource.</p>
<dt><code>-spat</code> <i>xmin ymin xmax ymax</i>:</p>
<dd> The area of interest. Only features within the rectangle will be reported.</p>
<dt><code>-geomfield</code> <i>field</i>:</p>
<dd> (OGR &gt;= 1.11) Name of the geometry field on which the spatial filter operates on.</p>
<dt><code>-fid</code> <i>fid</i>:</p>
<dd> If provided, only the feature with this feature id will be reported. Operates exclusive of the spatial or attribute queries. Note: if you want to select several features based on their feature id, you can also use the fact the &#8216;fid&#8217; is a special field recognized by OGR SQL. So, &#8216;-where &#8216;fid in (1,3,5)&#8221; would select features 1, 3 and 5.</p>
<dt><code>-fields</code>={YES/NO}:</p>
<dd> (starting with GDAL 1.6.0) If set to NO, the feature dump will not display field values. Default value is YES.</p>
<dt><code>-geom</code>={YES/NO/SUMMARY}:</p>
<dd> (starting with GDAL 1.6.0) If set to NO, the feature dump will not display the geometry. If set to SUMMARY, only a summary of the geometry will be displayed. If set to YES, the geometry will be reported in full OGC WKT format. Default value is YES.</p>
<dt><code>&#8211;formats</code>:</p>
<dd> List the format drivers that are enabled.</p>
<dt><i>datasource_name</i>:</p>
<dd> The data source to open. May be a filename, directory or other virtual name. See the OGR Vector Formats list for supported datasources.</p>
<dt><i>layer</i>:</p>
<dd> One or more layer names may be reported.</dl>
<p> If no layer names are passed then ogrinfo will report a list of available layers (and their layerwide geometry type). If layer name(s) are given then their extents, coordinate system, feature count, geometry type, schema and all features matching query parameters will be reported to the terminal. If no query parameters are provided, all features are reported. </p>
<p> Geometries are reported in OGC WKT format.</p>
<h2>EXAMPLE</h2>
<p> Example reporting all layers in an NTF file: </p>
<pre>
% ogrinfo wrk/SHETLAND_ISLANDS.NTF
INFO: Open of `wrk/SHETLAND_ISLANDS.NTF'
using driver `UK .NTF' successful.
1: BL2000_LINK (Line String)
2: BL2000_POLY (None)
3: BL2000_COLLECTIONS (None)
4: FEATURE_CLASSES (None)
</pre>
<p> Example using an attribute query is used to restrict the output of the features in a layer: </p>
<pre><code>
% ogrinfo - ro - where 'GLOBAL_LINK_ID=185878' wrk / SHETLAND_ISLANDS.NTF BL2000_LINK INFO : Open of `wrk / SHETLAND_ISLANDS.NTF' using driver `UK.NTF' successful. Layer name : BL2000_LINK Geometry : Line String Feature Count : 1 Extent : (419794.100000, 1069031.000000) - (419927.900000, 1069153.500000)Layer SRS WKT : PROJCS["OSGB 1936 / British National Grid", GEOGCS["OSGB 1936", DATUM["OSGB_1936", SPHEROID["Airy 1830", 6377563.396, 299.3249646]], PRIMEM["Greenwich", 0], UNIT["degree", 0.0174532925199433]], PROJECTION["Transverse_Mercator"], PARAMETER["latitude_of_origin", 49], PARAMETER["central_meridian", -2], PARAMETER["scale_factor", 0.999601272], PARAMETER["false_easting", 400000], PARAMETER["false_northing", -100000], UNIT["metre", 1]] LINE_ID : Integer(6.0) GEOM_ID : Integer(6.0) FEAT_CODE : String(4.0) GLOBAL_LINK_ID : Integer(10.0) TILE_REF : String(10.0) OGRFeature(BL2000_LINK) : 2 LINE_ID(Integer) = 2 GEOM_ID(Integer) = 2 FEAT_CODE(String) = (null)
    GLOBAL_LINK_ID(Integer) = 185878 TILE_REF(String) = SHETLAND I
    LINESTRING(419832.100 1069046.300, 419820.100 1069043.800, 419808.300 1069048.800, 419805.100 1069046.000, 419805.000 1069040.600, 419809.400 1069037.400, 419827.400 1069035.600, 419842 1069031, 419859.000 1069032.800, 419879.500 1069049.500, 419886.700 1069061.400, 419890.100 1069070.500, 419890.900 1069081.800, 419896.500 1069086.800, 419898.400 1069092.900, 419896.700 1069094.800, 419892.500 1069094.300, 419878.100 1069085.600, 419875.400 1069087.300, 419875.100 1069091.100, 419872.200 1069094.600, 419890.400 1069106.400, 419907.600 1069112.800, 419924.600 1069133.800, 419927.900 1069146.300, 419927.600 1069152.400, 419922.600 1069153.500, 419917.100 1069153.500, 419911.500 1069153.000, 419908.700 1069152.500, 419903.400 1069150.800, 419898.800 1069149.400, 419894.800 1069149.300, 419890.700 1069149.400, 419890.600 1069149.400, 419880.800 1069149.800, 419876.900 1069148.900, 419873.100 1069147.500, 419870.200 1069146.400, 419862.100 1069143.000, 419860 1069142, 419854.900 1069138.600, 419850 1069135, 419848.800 1069134.100, 419843 1069130, 419836.200 1069127.600, 419824.600 1069123.800, 419820.200 1069126.900, 419815.500 1069126.900, 419808.200 1069116.500, 419798.700 1069117.600, 419794.100 1069115.100, 419796.300 1069109.100, 419801.800 1069106.800, 419805.000 1069107.300)
</code></pre>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com, Silke Reimer silke [at] intevation.de </p>
<h2>Index</h2>
