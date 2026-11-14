---
title: "vectorintro(1)"
name: "vectorintro"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vectorintro/"
---

<h2>Vector data processing in GRASS GIS</h2>
<h3>Vector data import and export</h3>
<p> The v.in.ogr module offers a common interface for many different vector formats. Additionally, it offers options such as on-the-fly creation of new locations or extension of the default region to match the extent of the imported vector map. For special cases, other import modules are available, e.g. v.in.ascii for input from a text file containing coordinate and attribute data, and v.in.db for input from a database containing coordinate and attribute data. With v.external external maps can be virtually linked into a mapset, only pseudo-topology is generated but the vector geometry is not imported. The <i>v.out.*</i> set of commands exports to various formats.</p>
<h3>Metadata</h3>
<p> The v.info display general information such as metadata and attribute columns about a vector map including the history how it was generated. Each map generating command stores the command history into the metadata (query with v.info -h mapname). Metadata such as map title, scale, organization etc. can be updated with v.support.</p>
<h3>Vector map operations</h3>
<p> GRASS vector map processing is always performed on the full map. If this is not desired, the input map has to be clipped to the current region beforehand (v.in.region, v.select).</p>
<h3>Vector model and topology</h3>
<p> GRASS is a topological GIS. This means that adjacent geographic components in a single vector map are related. For example in a non-topological GIS if two areas shared a common border that border would be digitized two times and also stored in duplicate. In a topological GIS this border exists once and is shared between two areas. Topological represenation of vector data helps to produce and maintain vector maps with clean geometry as well as enables certain analyses that can not be conducted with non-topological or spaghetti data. In GRASS topological data are refered to as level 2 data and spaghetti data is referred to as level 1. </p>
<p> Sometimes topology is not necessary and the additional memory and space requirements are burdensome to a particular task. Therefore two modules allow for working level 1 (non-topological) data within GRASS. The v.in.ascii module allows users to input points without building topology. This is very useful for large files where memory restrictions may cause difficulties. The other module which works with level 1 data is v.surf.rst which enables spatial approximation and topographic analysis from a point or isoline file. </p>
<p>&nbsp;<wbr>In GRASS, the following vector objects are defined:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
&nbsp;<wbr>point: a point;&nbsp;<wbr></p>
<dt>
<dd>
&nbsp;<wbr>line: a directed sequence of connected vertices with two endpoints called nodes;&nbsp;<wbr></p>
<dt>
<dd>
&nbsp;<wbr>boundary: the border line to describe an area;&nbsp;<wbr></p>
<dt>
<dd>
&nbsp;<wbr>centroid: a point within a closed boundary;&nbsp;<wbr></p>
<dt>
<dd>
&nbsp;<wbr>area: the topological composition of centroid and boundary;&nbsp;<wbr></p>
<dt>
<dd>
&nbsp;<wbr>face: a 3D area;&nbsp;<wbr></p>
<dt>
<dd>
&nbsp;<wbr>kernel: a 3D centroid in a volume&nbsp;<wbr>(not yet implemented);&nbsp;<wbr></p>
<dt>
<dd>
&nbsp;<wbr>volume: a 3D corpus, the topological composition of faces and kernel&nbsp;<wbr>(not yet implemented).&nbsp;<wbr></dl>
</dl>
<p> Note that all lines and boundaries can be polylines (with nodes in between). </p>
<p> The v.type module can be used to convert between vector types if possible. The v.build module is used to generate topology. It optionally allows to extract the erroneous vector objects into a separate map. Topological errors can be corrected either manually within v.digit or, to some extent, automatically in v.clean. Adjacent polygons can be found by v.to.db (see &#8216;sides&#8217; option). </p>
<p> Many operations including extraction, queries, overlay, and export will only act on features which have been assigned a category number. Typically a centroid will hold the attribute data for the area between it and its boundary. Boundaries are not typically given a category ID as it would be ambiguous as to which area either side of it the attribute data would belong to. An exception might be when the boundary between two crop-fields is the center-line of a road, and the category information is an index to the road name. For everyday use boundaries and centroids can be treated as internal data types and the user can work directly and more simply with the &quot;area&quot; meta-feature type.</p>
<h3>Attribute management</h3>
<p> GRASS can be linked to one or many database management systems (DBMS). The <i>db.*</i> set of commands provides basic SQL support for attribute management, while the <i>v.db.*</i> set of commands operates on the vector map.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>Categories:</code> The category number is the vector ID. It is used to link attribute(s) to each vector object. A vector object can have zero, one, two, or more categories. Category numbers are stored both within the geometry file and within the attribute table(s) for each vector object (usually the &quot;cat&quot; column). Using v.category, category numbers can be printed or maintained. In order to link one vector object to several attribute tables, several category numbers per vector object are needed.</p>
<dt>
<dd> <code>Layers:</code> It is possible to link the geographic objects in a vector map to one or more tables. Each link to a distinct attribute table is called a layer. A link defines which database driver, database and table is to be used. Each category numbers in a geometry file corresponds to a row in the attribute table (the linking column is usually the &quot;cat&quot; key column). Using v.db.connect layers can be listed or maintained.<br />
 GRASS layers do not contain any geographic objects, but they consist of links to attribute tables in which vector objects can have zero, one or more categories. If a vector object has zero categories in a layer, then it does not appear in that layer. In this fashion some vector objects may appear in some layers but not in others. The practical benefit of this system is that it allows placement of thematically distinct but topologically related objects into a single map (e.g. forests and lakes). These virtual layers are also useful for linking time series attribute data to a series of locations that did not change over time. By default the first layer is active, i.e. the first table corresponds to the first layer. Further tables are linked to subsequent layers.</p>
<dt>
<dd> <code>SQL support:</code> The DBF driver provides only very limited SQL support (as DBF is not an SQL DB) while the other DBMS backends (such as PostgreSQL, MySQL etc) provide full SQL support since the SQL commands are sent directly to the DBMI. SQL commands can be directly executed with db.execute, db.select and the other db.* modules.</dl>
</dl>
<p> When creating vector maps from scratch, in general an attribute table must be created and the table must be populated with one row per category (using v.to.db). However, this can be performed in a single step using v.db.addtable along with the definition of table column types. Column adding and dropping can be done with v.db.addcol and v.db.dropcol. A table column can be renamed with v.db.renamecol. To drop a table from a map, use v.db.droptable. Values in a table can be updated with v.db.update. Tables can be joined with with v.db.join.</p>
<h3>Editing vector attributes</h3>
<p> To manually edit attributes of a table, the map has to be queried in &#8216;edit mode&#8217; using d.what.vect. To bulk process attributes, it is recommended to use SQL (db.execute).</p>
<h3>Geometry operations</h3>
<p> The module v.in.region saves the current region boundary into a vector area. Split vector lines can be changes to polylines by v.build.polylines. Long lines can be split by v.split and v.segment. Buffer and circles can be generated with v.buffer and v.parallel. v.generalize is module for generalization of GRASS vector maps. 2D vector maps can be changed to 3D using v.extrude. If needed, the spatial position of vector points can be perturbed by v.perturb. The v.type command changes between vector types (see list above). Projected vector maps can be reprojected with v.proj. Unprojected maps can be geocoded with v.transform. Triangulation and point-to-polygon conversions can be done with &lt;a href=&quot;v.delaunay.html&quot;&gt;v.delaunay, v.hull, and v.voronoi. The v.random command generated random points.</p>
<h3>Vector overlays and selections</h3>
<p> Geometric overlay of vector maps is done with v.patch, v.select, depending on the combination of vector types. Vectors can be extracted with v.extract and reclassified with v.reclass.</p>
<h3>Vector statistics</h3>
<p> Statistics can be generated by v.qcount, v.normal, and v.univar. Distances between vector objects are calculated with v.distance.</p>
<h3>Vector-Raster-DB conversion</h3>
<p> The v.to.db transfers vector information into database tables. With v.to.points, v.to.rast3 conversions are performed.</p>
<h3>Vector queries</h3>
<p> Vector maps can be queried with v.what and v.what.vect.</p>
<h3>Vector-Raster queries</h3>
<p> Raster values can be transferred to vector maps with v.what.rast and v.rast.stats.</p>
<h3>Vector network analysis</h3>
<p> GRASS provides support for vector network analysis. The following algorithms are implemented:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
&nbsp;<wbr>Vector maintenance: v.net</p>
<dt>
<dd>
&nbsp;<wbr>Shortest path: d.path and&nbsp;<wbr> v.net.path</p>
<dt>
<dd>
&nbsp;<wbr>Traveling salesman&nbsp;<wbr>(round trip): v.net.salesman</p>
<dt>
<dd>
&nbsp;<wbr>Allocation of sources&nbsp;<wbr>(create subnetworks, e.g. police station zones): v.net.alloc</p>
<dt>
<dd>
&nbsp;<wbr>Minimum Steiner trees&nbsp;<wbr>(star-like connections, e.g. broadband cable&nbsp;<wbr> connections): v.net.steiner</p>
<dt>
<dd>
&nbsp;<wbr>Iso-distances&nbsp;<wbr>(from centers): v.net.iso</dl>
</dl>
<p> &#8211;b). Both directions are supported, network modules provide parameters to assign attribute columns to the forward and backward direction.</p>
<h3>Vector networks: Linear referencing system (LRS)</h3>
<p> LRS uses linear features and distance measured along those features to positionate objects. There are the commands v.lrs.create to create a linear reference system, v.lrs.label to create stationing on the LRS, v.lrs.segment to create points/segments on LRS, and v.lrs.where to find line id and real km+offset for given points in vector map using linear reference system. </p>
<p> The LRS tutorial explains further details.</p>
<h3>Interpolation and approximation</h3>
<p> Some of the vector modules deal with spatial or volumetric approximation (also called interpolation): v.kernel, v.surf.idw, v.surf.rst, and v.vol.rst.</p>
<h3>Lidar data processing</h3>
<p> Lidar point clouds (first and last return) are imported with &lt;a href=&quot;v.in.ascii.html&quot;&gt;v.in.ascii (-b flag to not build the topology). Outlier detection is done with v.outlier on both first and last return data. Then, with v.lidar.edgedetection, edges are detected from last return data. The building are generated by v.lidar.growing from detected edges. The resulting data are post-processed with v.lidar.correction. Finally, the DTM and DSM are generated with v.surf.bspline (DTM: uses the &#8216;v.lidar.correction&#8217; output; DSM: uses last return output from outlier detection).</p>
<h3>See also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Introduction to GRASS database management</p>
<dt>
<dd> Introduction to GRASS raster map processing</p>
<dt>
<dd> Introduction to GRASS 3D raster map (voxel) processing</dl>
</dl>
<p> full index </p>
<h2>Index</h2>
