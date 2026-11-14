---
title: "ogr2ogr(1)"
name: "ogr2ogr"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ogr2ogr/"
description: "ogr2ogr – ogr2ogr converts simple features data between file formats"
---

<h2 class="name">NAME</h2>
<p> ogr2ogr &#8211; ogr2ogr converts simple features data between file formats </p>
<h2>SYNOPSIS</h2>
<pre><code>
Usage : ogr2ogr[--help - general][-skipfailures][-append][-update]
               [-select field_list][-where restricted_where]
               [-progress][-sql&lt;sql statement&gt;][-dialect dialect]
               [-preserve_fid][-fid FID]
               [-spat xmin ymin xmax ymax][-geomfield field]
               [-a_srs srs_def][-t_srs srs_def][-s_srs srs_def]
               [-f format_name][-overwrite][[-dsco NAME = VALUE]...] dst_datasource_name src_datasource_name
                   [-lco NAME = VALUE][-nln name][-nlt type][-dim 2 | 3 | layer_dim][layer[layer...]] Advanced options : [-gt n]
                                                                                                                             [-clipsrc[xmin ymin xmax ymax] | WKT | datasource | spat_extent]
                                                                                                                             [-clipsrcsql sql_statement][-clipsrclayer layer]
                                                                                                                             [-clipsrcwhere expression]
                                                                                                                             [-clipdst[xmin ymin xmax ymax] | WKT | datasource]
                                                                                                                             [-clipdstsql sql_statement][-clipdstlayer layer]
                                                                                                                             [-clipdstwhere expression]
                                                                                                                             [-wrapdateline][-datelineoffset val]
                                                                                                                             [[-simplify tolerance] | [-segmentize max_dist]]
                                                                                                                             [-addfields]
                                                                                                                             [-fieldTypeToString All | (type1[, type2] *)][-unsetFieldWidth]
                                                                                                                             [-fieldmap identity | index1[, index2] * ]
                                                                                                                             [-splitlistfields][-maxsubfields val]
                                                                                                                             [-explodecollections][-zfield field_name]
                                                                                                                             [-gcp pixel line easting northing[elevation]] *
                                                                                                                         [-order n | -tps].fi
</code></pre>
<h2>DESCRIPTION</h2>
<p> This program can be used to convert simple features data between file formats performing various operations during the process such as spatial or attribute selections, reducing the set of attributes, setting the output coordinate system or even reprojecting the features during translation. </p>
<dl>
<dt><code> -f</code><i> format_name</i>:</p>
<dd> output file format name (default is ESRI Shapefile), some possible values are:</dl>
<pre>
     -f &quot;ESRI Shapefile&quot;
     -f &quot;TIGER&quot;
     -f &quot;MapInfo File&quot;
     -f &quot;GML&quot;
     -f &quot;PostgreSQL&quot;
</pre>
<p>&nbsp;<wbr>&nbsp;<wbr></p>
<dl>
<dt><code>-append</code>:</p>
<dd> Append to existing layer instead of creating new</p>
<dt><code>-overwrite</code>:</p>
<dd> Delete the output layer and recreate it empty</p>
<dt><code>-update</code>:</p>
<dd> Open existing output datasource in update mode rather than trying to create a new one</p>
<dt><code>-select</code><i> field_list</i>:</p>
<dd> Comma-delimited list of fields from input layer to copy to the new layer. A field is skipped if mentioned previously in the list even if the input layer has duplicate field names. (Defaults to all; any field is skipped if a subsequent field with same name is found.) Starting with OGR 1.11, geometry fields can also be specified in the list.</p>
<dt><code>-progress</code>:</p>
<dd> (starting with GDAL 1.7.0) Display progress on terminal. Only works if input layers have the &#8216;fast feature count&#8217; capability.</p>
<dt><code>-sql</code> <i>sql_statement</i>:</p>
<dd> SQL statement to execute. The resulting table/layer will be saved to the output.</p>
<dt><code>-dialect</code> <i>dialect</i>:</p>
<dd> SQL dialect. In some cases can be used to use (unoptimized) OGR SQL instead of the native SQL of an RDBMS by passing OGRSQL. Starting with GDAL 1.10, the &#8216;SQLITE&#8217; dialect can also be used with any datasource.</p>
<dt><code>-where</code><i> restricted_where</i>:</p>
<dd> Attribute query (like SQL WHERE)</p>
<dt><code>-skipfailures</code>:</p>
<dd> Continue after a failure, skipping the failed feature.</p>
<dt><code>-spat</code><i> xmin ymin xmax ymax</i>:</p>
<dd> spatial query extents. Only features whose geometry intersects the extents will be selected. The geometries will not be clipped unless -clipsrc is specified</p>
<dt><code>-geomfield</code> <i>field</i>:</p>
<dd> (OGR &gt;= 1.11) Name of the geometry field on which the spatial filter operates on.</p>
<dt><code>-dsco</code> <i>NAME=VALUE</i>:</p>
<dd> Dataset creation option (format specific)</p>
<dt><code>-lco</code><i> NAME=VALUE</i>:</p>
<dd> Layer creation option (format specific)</p>
<dt><code>-nln</code><i> name</i>:</p>
<dd> Assign an alternate name to the new layer</p>
<dt><code>-nlt</code><i> type</i>:</p>
<dd> Define the geometry type for the created layer. One of NONE, GEOMETRY, POINT, LINESTRING, POLYGON, GEOMETRYCOLLECTION, MULTIPOINT, MULTIPOLYGON or MULTILINESTRING. Add &#8217;25D&#8217; to the name to get 2.5D versions. Starting with GDAL 1.10, PROMOTE_TO_MULTI can be used to automatically promote layers that mix polygon or multipolygons to multipolygons, and layers that mix linestrings or multilinestrings to multilinestrings. Can be usefull when converting shapefiles to PostGIS (and other target drivers) that implements strict checks for geometry type.</p>
<dt><code>-dim</code><i> val</i>:</p>
<dd> (starting with GDAL 1.10) Force the coordinate dimension to val (valid values are 2 or 3). This affects both the layer geometry type, and feature geometries. Starting with GDAL 1.11, the value can be set to &#8216;layer_dim&#8217; to instruct feature geometries to be promoted to the coordinate dimension declared by the layer.</p>
<dt><code>-a_srs</code><i> srs_def</i>:</p>
<dd> Assign an output SRS</p>
<dt><code>-t_srs</code><i> srs_def</i>:</p>
<dd> Reproject/transform to this SRS on output</p>
<dt><code>-s_srs</code><i> srs_def</i>:</p>
<dd> Override source SRS</p>
<dt><code>-preserve_fid</code>:</p>
<dd> Use the FID of the source features instead of letting the output driver to automatically assign a new one.</p>
<dt><code>-fid</code> <i>fid</i>:</p>
<dd> If provided, only the feature with this feature id will be reported. Operates exclusive of the spatial or attribute queries. Note: if you want to select several features based on their feature id, you can also use the fact the &#8216;fid&#8217; is a special field recognized by OGR SQL. So, &#8216;-where &#8216;fid in (1,3,5)&#8221; would select features 1, 3 and 5.</dl>
<p> Srs_def can be a full WKT definition (hard to escape properly), or a well known definition (ie. EPSG:4326) or a file with a WKT definition. </p>
<p> Advanced options : </p>
<dl>
<dt><code>-gt</code> <i>n</i>:</p>
<dd> group <i>n</i> features per transaction (default 20000 in OGR 1.11, 200 in previous releases). Increase the value for better performance when writing into DBMS drivers that have transaction support.</p>
<dt><code>-clipsrc</code><i> [xmin ymin xmax ymax]|WKT|datasource|spat_extent</i>:</p>
<dd> (starting with GDAL 1.7.0) clip geometries to the specified bounding box (expressed in source SRS), WKT geometry (POLYGON or MULTIPOLYGON), from a datasource or to the spatial extent of the <code>-spat</code> option if you use the <i>spat_extent</i> keyword. When specifying a datasource, you will generally want to use it in combination of the <code>-clipsrclayer</code>, <code>-clipsrcwhere</code> or <code>-clipsrcsql</code> options</p>
<dt><code>-clipsrcsql</code> <i>sql_statement</i>:</p>
<dd> Select desired geometries using an SQL query instead.</p>
<dt><code>-clipsrclayer</code> <i>layername</i>:</p>
<dd> Select the named layer from the source clip datasource.</p>
<dt><code>-clipsrcwhere</code> <i>expression</i>:</p>
<dd> Restrict desired geometries based on attribute query.</p>
<dt><code>-clipdst</code><i> xmin ymin xmax ymax</i>:</p>
<dd> (starting with GDAL 1.7.0) clip geometries after reprojection to the specified bounding box (expressed in dest SRS), WKT geometry (POLYGON or MULTIPOLYGON) or from a datasource. When specifying a datasource, you will generally want to use it in combination of the -clipdstlayer, -clipdstwhere or -clipdstsql options</p>
<dt><code>-clipdstsql</code> <i>sql_statement</i>:</p>
<dd> Select desired geometries using an SQL query instead.</p>
<dt><code>-clipdstlayer</code> <i>layername</i>:</p>
<dd> Select the named layer from the destination clip datasource.</p>
<dt><code>-clipdstwhere</code> <i>expression</i>:</p>
<dd> Restrict desired geometries based on attribute query.</p>
<dt><code>-wrapdateline</code>:</p>
<dd> (starting with GDAL 1.7.0) split geometries crossing the dateline meridian (long. = +/- 180deg)</p>
<dt><code>-datelineoffset</code>:</p>
<dd> (starting with GDAL 1.10) offset from dateline in degrees (default long. = +/- 10deg, geometries within 170deg to -170deg will be splited)</p>
<dt><code>-simplify</code><i> tolerance</i>:</p>
<dd> (starting with GDAL 1.9.0) distance tolerance for simplification. Note: the algorithm used preserves topology per feature, in particular for polygon geometries, but not for a whole layer.</p>
<dt><code>-segmentize</code><i> max_dist</i>:</p>
<dd> (starting with GDAL 1.6.0) maximum distance between 2 nodes. Used to create intermediate points</p>
<dt><code>-fieldTypeToString</code><i> type1, &#8230;</i>:</p>
<dd> (starting with GDAL 1.7.0) converts any field of the specified type to a field of type string in the destination layer. Valid types are : Integer, Real, String, Date, Time, DateTime, Binary, IntegerList, RealList, StringList. Special value <code>All</code> can be used to convert all fields to strings. This is an alternate way to using the CAST operator of OGR SQL, that may avoid typing a long SQL query.</p>
<dt><code>-unsetFieldWidth</code>:</p>
<dd> (starting with GDAL 1.11) set field width and precision to 0.</p>
<dt><code>-splitlistfields</code>:</p>
<dd> (starting with GDAL 1.8.0) split fields of type StringList, RealList or IntegerList into as many fields of type String, Real or Integer as necessary.</p>
<dt><code>-maxsubfields</code> <i>val</i>:</p>
<dd> To be combined with -splitlistfields to limit the number of subfields created for each split field.</p>
<dt><code>-explodecollections</code>:</p>
<dd> (starting with GDAL 1.8.0) produce one feature for each geometry in any kind of geometry collection in the source file</p>
<dt><code>-zfield</code> <i>field_name</i>:</p>
<dd> (starting with GDAL 1.8.0) Uses the specified field to fill the Z coordinate of geometries</p>
<dt><code>-gcp</code> <i>ungeoref_x ungeoref_y georef_x georef_y elevation</i>:</p>
<dd> (starting with GDAL 1.10.0) Add the indicated ground control point. This option may be provided multiple times to provide a set of GCPs.</p>
<dt><code>-order</code> <i>n</i>:</p>
<dd> (starting with GDAL 1.10.0) order of polynomial used for warping (1 to 3). The default is to select a polynomial order based on the number of GCPs.</p>
<dt><code>-tps</code>:</p>
<dd> (starting with GDAL 1.10.0) Force use of thin plate spline transformer based on available GCPs.</p>
<dt><code>-fieldmap</code>:</p>
<dd> (starting with GDAL 1.10.0) Specifies the list of field indexes to be copied from the source to the destination. The (n)th value specified in the list is the index of the field in the target layer definition in which the n(th) field of the source layer must be copied. Index count starts at zero. There must be exactly as many values in the list as the count of the fields in the source layer. We can use the &#8216;identity&#8217; setting to specify that the fields should be transferred by using the same order. This setting should be used along with the -append setting.</p>
<dt><code>-addfields</code>:</p>
<dd> (starting with GDAL 1.11) This is a specialized version of -append. Contrary to -append, -addfields has the effect of adding, to existing target layers, the new fields found in source layers. This option is usefull when merging files that have non-strictly identical structures. This might not work for output formats that don&#8217;t support adding fields to existing non-empty layers.</dl>
<h2>PERFORMANCE HINTS</h2>
<p> When writing into transactional DBMS (SQLite/PostgreSQL,MySQL, etc&#8230;), it might be beneficial to increase the number of INSERT statements executed between BEGIN TRANSACTION and COMMIT TRANSACTION statements. This number is specified with the -gt option. For example, for SQLite, explicitly defining <code>-gt 65536</code> ensures optimal performance while populating some table containing many hundredth thousand or million rows. However, note that if there are failed insertions, the scope of -skipfailures is a whole transaction. </p>
<p> For PostgreSQL, the PG_USE_COPY config option can be set to YES for significantly insertion performance boot. See the PG driver documentation page. </p>
<p> More generally, consult the documentation page of the input and output drivers for performance hints.</p>
<h2>EXAMPLE</h2>
<p> Example appending to an existing layer (both flags need to be used): </p>
<pre>
% ogr2ogr -update -append -f PostgreSQL PG:dbname=warmerda abc.tab
</pre>
<p> Example reprojecting from ETRS_1989_LAEA_52N_10E to EPSG:4326 and clipping to a bounding box </p>
<pre>
% ogr2ogr -wrapdateline -t_srs EPSG:4326 -clipdst -5 40 15 55 france_4326.shp europe_laea.shp
</pre>
<p> Example for using the -fieldmap setting. The first field of the source layer is used to fill the third field (index 2 = third field) of the target layer, the second field of the source layer is ignored, the third field of the source layer used to fill the fifth field of the target layer. </p>
<pre>
% ogr2ogr -append -fieldmap 2,-1,4 dst.shp src.shp
</pre>
<p> More examples are given in the individual format pages.</p>
<h2>AUTHOR</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com, Silke Reimer silke [at] intevation.de </p>
<h2>Index</h2>
