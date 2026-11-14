---
title: "osm2pgsql(1)"
name: "osm2pgsql"
section: "1"
letter: "o"
url: "/docs/linux/man/1-osm2pgsql/"
description: "osm2pgsql – Openstreetmap data to PostgreSQL converter."
---

<h2 class="name">NAME</h2>
<p> osm2pgsql &#8211; Openstreetmap data to PostgreSQL converter. </p>
<h2>SYNOPSIS</h2>
<p> <code>osm2pgsql</code> [<i>options</i>]<i> planet.osm</i><br />
 <code>osm2pgsql</code> [<i>options</i>]<i> planet.osm.{gz,bz2,pbf}</i><br />
 <code>osm2pgsql</code> [<i>options</i>]<i> file1.osm file2.osm file3.osm</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>osm2pgsql</code> command. </p>
<p> <code>osm2pgsql</code> imports data from OSM file(s) into a PostgreSQL database suitable for use by the Mapnik renderer or the Nominatim geocoder.<br />
 OSM planet snapshots can be downloaded from <a rel="nofollow" href="http://planet.openstreetmap.org/.">http://planet.openstreetmap.org/.</a> Partial planet files (&quot;extracts&quot;) for various countries are available, see <a rel="nofollow" href="http://wiki.openstreetmap.org/wiki/Planet.osm.">http://wiki.openstreetmap.org/wiki/Planet.osm.</a> </p>
<p> Extracts in PBF (ProtoBufBinary) format are also available from <a rel="nofollow" href="http://download.geofabrik.de/osm/.">http://download.geofabrik.de/osm/.</a> </p>
<p> When operating in &quot;slim&quot; mode (and on a database created in &quot;slim&quot; mode!), <code>osm2pgsql</code> can also process OSM change files (osc files), thereby bringing an existing database up to date. </p>
<h2>OPTIONS</h2>
<p> These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-a</code>|&#8211;append</p>
<dd> Add the OSM file into the database without removing existing data.</p>
<dt><code>-b</code>|&#8211;bbox</p>
<dd> Apply a bounding box filter on the imported data. Must be specified as: minlon,minlat,maxlon,maxlat e.g. <code>&#8211;bbox</code> <code>-0.5,51.25,0.5,51.75</code></p>
<dt><code>-c</code>|&#8211;create</p>
<dd> Remove existing data from the database. This is the default if <code>&#8211;append</code> is not specified.</p>
<dt><code>-d</code>|&#8211;database name</p>
<dd> The name of the PostgreSQL database to connect to (default: gis).</p>
<dt><code>-i</code>|&#8211;tablespace-index tablespacename</p>
<dd> Store all indices in a separate PostgreSQL tablespace named by this parameter. This allows one to e.g. store the indices on faster storage like SSDs.</p>
<dt><code>&nbsp;<wbr></code>&#8211;tablespace-main-data tablespacename</p>
<dd> Store the data tables (non slim) in the given tablespace.</p>
<dt><code>&nbsp;<wbr></code>&#8211;tablespace-main-index tablespacename</p>
<dd> Store the indices of the main tables (non slim) in the given tablespace.</p>
<dt><code>&nbsp;<wbr></code>&#8211;tablespace-slim-data tablespacename</p>
<dd> Store the slim mode tables in the given tablespace.</p>
<dt><code>&nbsp;<wbr></code>&#8211;tablespace-slim-index tablespacename</p>
<dd> Store the indices of the slim mode tables in the given tablespace.</p>
<dt><code>-l</code>|&#8211;latlong</p>
<dd> Store data in degrees of latitude &amp; longitude.</p>
<dt><code>-m</code>|&#8211;merc</p>
<dd> Store data in proper spherical Mercator (the default).</p>
<dt><code>-E</code>|&#8211;proj num</p>
<dd> Use projection EPSG:num</p>
<dt><code>-p</code>|&#8211;prefix prefix_string</p>
<dd> Prefix for table names (default: planet_osm).</p>
<dt><code>-r</code>|&#8211;input-reader format</p>
<dd> Select format of the input file. Available choices are <code>auto</code> (default) for autodetecting the format, <code>xml</code> for OSM XML format files, <code>o5m</code> for o5m formatted files and <code>pbf</code> for OSM PBF binary format.</p>
<dt><code>-s</code>|&#8211;slim</p>
<dd> Store temporary data in the database. Without this mode, all temporary data is stored in RAM and if you do not have enough the import will not work successfully. With slim mode, you should be able to import the data even on a system with limited RAM, although if you do not have enough RAM to cache at least all of the nodes, the time to import the data will likely be greatly increased.</p>
<dt><code>&nbsp;<wbr> </code>&#8211;drop</p>
<dd> Drop the slim mode tables from the database once the import is complete. This can greatly reduce the size of the database, as the slim mode tables typically are the same size, if not slightly bigger than the main tables. It does not, however, reduce the maximum spike of disk usage during import. It can furthermore increase the import speed, as no indices need to be created for the slim mode tables, which (depending on hardware) can nearly halve import time. Slim mode tables however have to be persistent if you want to be able to update your database, as these tables are needed for diff processing.</p>
<dt><code>-S</code>|&#8211;style /path/to/style</p>
<dd> Location of the osm2pgsql style file. This specifies which tags from the data get imported into database columns and which tags get dropped. Defaults to /usr/share/osm2pgsql/default.style.</p>
<dt><code>-C</code>|&#8211;cache num</p>
<dd> Only for slim mode: Use up to num many MB of RAM for caching nodes. Giving osm2pgsql sufficient cache to store all imported nodes typically greatly increases the speed of the import. Each cached node requires 8 bytes of cache, plus about 10% &#8211; 30% overhead. For a current OSM full planet import with its ~ 3 billion nodes, a good value would be 27000 if you have enough RAM. If you don&#8217;t have enough RAM, it is likely beneficial to give osm2pgsql close to the full available amount of RAM. Defaults to 800.</p>
<dt><code>&nbsp;<wbr> </code>&#8211;cache-strategy strategy</p>
<dd> There are a number of different modes in which osm2pgsql can organize its node cache in RAM. These are optimized for different assumptions of the data and the hardware resources available. Currently available strategies are <code>dense</code>, <code>chunked</code>, <code>sparse</code> and <code>optimized</code>. <code>dense</code> assumes that the node id numbers are densely packed, i.e. only a few IDs in the range are missing / deleted. For planet extracts this is usually not the case, making the cache very inefficient and wasteful of RAM. <code>sparse</code> assumes node IDs in the data are not densely packed, greatly increasing caching efficiency in these cases. If node IDs are densely packed, like in the full planet, this strategy has a higher overhead for indexing the cache. <code>optimized</code> uses both dense and sparse strategies for different ranges of the ID space. On a block by block basis it tries to determine if it is more effective to store the block of IDs in sparse or dense mode. This is the default and should be typically used.</p>
<dt><code>-U</code>|&#8211;username name</p>
<dd> Postgresql user name.</p>
<dt><code>-W</code>|&#8211;password</p>
<dd> Force password prompt.</p>
<dt><code>-H</code>|&#8211;host hostname</p>
<dd> Database server hostname or socket location.</p>
<dt><code>-P</code>|&#8211;port num</p>
<dd> Database server port.</p>
<dt><code>-e</code>|&#8211;expire-tiles [min_zoom-]max-zoom</p>
<dd> Create a tile expiry list.</p>
<dt><code>-o</code>|&#8211;expire-output /path/to/expire.list</p>
<dd> Output file name for expired tiles list.</p>
<dt><code>-O</code>|&#8211;output</p>
<dd> Specifies the output back-end or database schema to use. Currently osm2pgsql supports <code>pgsql</code>, <code>gazetteer</code> and <code>null</code>. <code>pgsql</code> is the default output back-end / schema and is optimized for rendering with Mapnik. <code>gazetteer</code> is a db schema optimized for geocoding and is used by Nominatim. <code>null</code> does not write any output and is only useful for testing or with &#8211;slim for creating slim tables.</p>
<dt><code>-x</code>|&#8211;extra-attributes</p>
<dd> Include attributes for each object in the database. This includes the username, userid, timestamp and version. Note: this option also requires additional entries in your style file.</p>
<dt><code>-k</code>|&#8211;hstore</p>
<dd> Add tags without column to an additional hstore (key/value) column to PostgreSQL tables.</p>
<dt><code>-j</code>|&#8211;hstore-all</p>
<dd> Add all tags to an additional hstore (key/value) column in PostgreSQL tables.</p>
<dt><code>-z</code>|&#8211;hstore-column key_name</p>
<dd> Add an additional hstore (key/value) column containing all tags that start with the specified string, eg &#8211;hstore-column &quot;name:&quot; will produce an extra hstore column that contains all name:xx tags</p>
<dt><code>&nbsp;<wbr> </code>&#8211;hstore-match-only</p>
<dd> Only keep objects that have a value in one of the columns (normal action with &#8211;hstore is to keep all objects).</p>
<dt><code>&nbsp;<wbr> </code>&#8211;hstore-add-index</p>
<dd> Create indices for the hstore columns during import.</p>
<dt><code>-G</code>|&#8211;multi-geometry</p>
<dd> Normally osm2pgsql splits multi-part geometries into separate database rows per part. A single OSM id can therefore have several rows. With this option, PostgreSQL instead generates multi-geometry features in the PostgreSQL tables.</p>
<dt><code>-K</code>|&#8211;keep-coastlines</p>
<dd> Keep coastline data rather than filtering it out. By default natural=coastline tagged data will be discarded based on the assumption that post-processed Coastline Checker shape files will be used.</p>
<dt><code>&nbsp;<wbr> </code>&#8211;exclude-invalid-polygon</p>
<dd> OpenStreetMap data is defined in terms of nodes, ways and relations and not in terms of actual geometric features. Osm2pgsql therefore tries to build postgis geometries out of this data representation. However not all ways and relations correspond to valid PostGIS geometries (e.g. self intersecting polygons). By default osm2pgsql tries to fix these geometries using buffer(0) around the invalid polygons. With this option, invalid polygons are instead simply dropped from the database. Even without this option, all polygons in the database should be valid.</p>
<dt><code>&nbsp;<wbr> </code>&#8211;unlogged</p>
<dd> Use postgresql&#8217;s unlogged tables for storing data. This requires PostgreSQL 9.1 or above. Data written to unlogged tables is not written to PostgreSQL&#8217;s write-ahead log, which makes them considerably faster than ordinary tables. However, they are not crash-safe: an unlogged table is automatically truncated after a crash or unclean shutdown.</p>
<dt><code>&nbsp;<wbr> </code>&#8211;number-processes num</p>
<dd> Specifies the number of parallel processes used for certain operations. If disks are fast enough e.g. if you have an SSD, then this can greatly increase speed of the &quot;going over pending ways&quot; and &quot;going over pending relations&quot; stages on a multi-core server.</p>
<dt><code>-I</code>|&#8211;disable-parallel-indexing</p>
<dd> By default osm2pgsql initiates the index building on all tables in parallel to increase performance. This can be disadvantages on slow disks, or if you don&#8217;t have enough RAM for PostgreSQL to perform up to 7 parallel index building processes (e.g. because maintenance_work_mem is set high).</p>
<dt><code>&nbsp;<wbr> </code>&#8211;flat-nodes /path/to/nodes.cache</p>
<dd> The flat-nodes mode is a separate method to store slim mode node information on disk. Instead of storing this information in the main PostgreSQL database, this mode creates its own separate custom database to store the information. As this custom database has application level knowledge about the data to store and is not general purpose, it can store the data much more efficiently. Storing the node information for the full planet requires about 100GB in PostgreSQL, the same data is stored in only ~16GB using the flat-nodes mode. This can also increase the speed of applying diff files. This option activates the flat-nodes mode and specifies the location of the database file. It is a single large &gt; 16GB file. This mode is only recommended for full planet imports as it doesn&#8217;t work well with small imports. The default is disabled.</p>
<dt><code>-h</code>|&#8211;help</p>
<dd> Help information.<br />
 Add <code>-v</code> to display supported projections.</p>
<dt><code>-v</code>|&#8211;verbose</p>
<dd> Verbose output.</dl>
<h2>SUPPORTED PROJECTIONS</h2>
<p> Latlong (-l) SRS: 4326 (none)<br />
 Spherical Mercator (-m) SRS:3857 +proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +no_defs +over<br />
 EPSG-defined (-E) SRS: +init=epsg:(as given in parameter) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-proj/">proj</a></code>(1), <code><a href="/docs/linux/man/1-postgres/">postgres</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> osm2pgsql was written by Jon Burgess, Artem Pavlenko, and other OpenStreetMap project members. </p>
<p> This manual page was written by Andreas Putzo &lt;andreas [at] putzo.net&gt; for the Debian project, and amended by OpenStreetMap authors. </p>
<h2>Index</h2>
