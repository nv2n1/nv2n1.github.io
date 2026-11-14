---
title: "grass-pg(1)"
name: "grass-pg"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grass-pg/"
---

The driver name is 'pg'.

<h2>Creating a PostgreSQL database</h2>

 A new database is created with 'createdb', see the PostgreSQL manual for details.

<h2>Connecting GRASS to PostgreSQL</h2>

 
 # example for connecting to a PostgreSQL server: 
 db.connect driver=pg database=&quot;host=myserver.itc.it,dbname=mydb&quot; 
 db.login user=myname pass=secret 
 db.connect -p 
 db.tables -p 

<h2>Supported SQL commands</h2>

 All SQL commands supported by PostgreSQL.

<h2>Operators available in conditions</h2>

 All SQL operators supported by PostgreSQL.

<h2>Adding an unique ID column</h2>

 Import vector module require an unique ID column which can be generated as follows in a PostgreSQL table: 
 echo &quot; 
 
&nbsp;<wbr>ALTER TABLE mytable ADD ID integer; 
 
&nbsp;<wbr>CREATE SEQUENCE mytable_seq; 
 
&nbsp;<wbr>UPDATE mytabe SET ID&nbsp;<wbr>=&nbsp;<wbr>nextval('mytable_seq'); 
 
&nbsp;<wbr>DROP SEQUENCE mytable_seq; 
 dq | db.execute 

<h2>Attribute Converters</h2>

 CSV import into PostgreSQL: 
 rsh copy 
 COPY t1 FROM 'filename' USING DELIMITERS ','; 
 pg2xbase: DBF to PostgreSQL converter. 

<h2>PostGIS: PostgreSQL with vector geometry</h2>

 PostGIS: adds geographic object support to PostgreSQL.

<h3>Example: Import from PostGIS</h3>

 In an existing PostGIS database, create the following table: 
 CREATE TABLE test 
 ( 
 
&nbsp;<wbr>id serial NOT NULL, 
 
&nbsp;<wbr>mytime timestamp DEFAULT now(), 
 
&nbsp;<wbr>text varchar, 
 
&nbsp;<wbr>wkb_geometry geometry, 
 
&nbsp;<wbr>CONSTRAINT test_pkey PRIMARY KEY&nbsp;<wbr>(id) 
 ) WITHOUT OIDS; 
 
 # insert value 
 INSERT INTO test (text, wkb_geometry) 
 
&nbsp;<wbr>VALUES&nbsp;<wbr>('Name',geometryFromText('POLYGON((600000 200000,650000 
 
&nbsp;<wbr>200000,650000 250000,600000 250000,600000 200000))',-1)); 
 
 # register the table with geometry 
 select AddGeometryColumn ('postgis', 'test', 'geometry', -1, 'GEOMETRY', 2); 
 GRASS can import this PostGIS polygon map as follows: 
 v.in.ogr dsn=&quot;PG:host=localhost dbname=postgis user=neteler&quot; layer=test rs 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>output=test type=boundary,centroid 
 v.db.select test 
 v.info -t test 

<h3>Geometry Converters</h3>

<dl>
<dt>
<dd>
<dl>
<dt>
<dd> PostGIS with shp2pgsql: 
 shp2pgsql -D lakespy2 lakespy2 test &gt; lakespy2.sql 

<dt>
<dd> e00pg: E00 to PostGIS filter, see also <i>v.in.e00</i>. 

<dt>
<dd> GDAL/OGR ogrinfo and ogr2ogr: GIS vector format converter and library, e.g. ArcInfo or SHAPE to PostGIS. 
 ogr2ogr -f &quot;PostgreSQL&quot; shapefile ?? 
</dl>
</dl>

<h2>SEE ALSO</h2>

 <i> db.connect, db.execute, 
 Database management in GRASS GIS, 
 Help pages for database modules, 
 SQL support in GRASS GIS </i> 
 <i> PostgreSQL web site, 
 pgAdmin graphical user interface 

 Book: PostgreSQL: Introduction and Concepts by Bruce Momjian 
 PostgreSQL Documentation 
 PostgreSQL Technical Documentation 
 GDAL/OGR PostgreSQL driver documentation 
 MapServer Wiki </i> 

 <i>Last changed: $Date: 2007-11-24 13:41:10 +0100 (Sat, 24 Nov 2007) $</i> 
 Help Index 

<h2>Index</h2>


