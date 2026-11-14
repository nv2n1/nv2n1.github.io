---
title: "databaseintro(1)"
name: "databaseintro"
section: "1"
letter: "d"
url: "/docs/linux/man/1-databaseintro/"
---

<h2>Database management in GRASS GIS</h2>
<h3>Attribute management in general</h3>
<p> GRASS can be linked to one or many database management systems (DBMS). The <i>db.*</i> set of commands provides basic SQL support for attribute management, while the <i>v.db.*</i> set of commands operates on the vector map (see Vector introduction).</p>
<h3>Available drivers</h3>
<p> Available drivers are listed in SQL support in GRASS GIS. </p>
<p> <code>Notes</code>:<br />
 The default DBF driver provides only very limited SQL support (as DBF is not an SQL DB) while the other DBMS backends (such as PostgreSQL, MySQL etc) provide full SQL support since the SQL commands are sent directly to the DBMS.</p>
<h3>DB connection management</h3>
<p> The current database management settings are shown or modified with db.connect for current mapset. Available DBMI drivers are listed with db.drivers. Some DBMI backends require a user/password for driver/database to be set with db.login. In order to test a driver, run db.test.</p>
<h3>Attribute data import and export</h3>
<p> Attribute data can be imported with db.in.ogr from various formats and exported with db.out.ogr. To internally copy a a full table or selectively parts of it, use db.copy. </p>
<p> Further conversion tools:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> MDB Tools: Convert MS-Access data to SQL, DBF, etc.</p>
<dt>
<dd> Openoffice.org with SQL Databases</dl>
</dl>
<h3>SQL commands</h3>
<p> GRASS supports to main SQL operations, execution of an SQL statement (db.execute) and selection of data from a table (db.select). See the SQL help page for examples.</p>
<h3>Managing the default DBMI settings</h3>
<p> Per default vector map attributes are stored in DBF table files. This default definition can be modified with db.connect. If an external DBMS is used, db.login may be required.</p>
<h3>Creating a database</h3>
<p> Specific commands are explained on the individual driver pages (these pages are only available if driver was compiled in this installation):</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> DBF: see DBF page</p>
<dt>
<dd> SQLite: SQLite page</p>
<dt>
<dd> mySQL: meSQL pages</p>
<dt>
<dd> ODBC: ODBC page (connect to Oracle, etc.)</p>
<dt>
<dd> PostgreSQL: PostgreSQL and PostGIS page</dl>
</dl>
<h3>Metadata</h3>
<p> All columns for a given table are listed with db.columns. The command db.describe describes a table in detail. To list all available tables for a given database, run db.tables.</p>
<h3>Table maintenance</h3>
<p> To drop a column from a selected attribute table, use db.dropcol. With db.droptable an attribute table can be deleted.</p>
<h3>Database Schema</h3>
<p> Currently schema support only works for PostgreSQL connections. Default schema can be set with db.connect. Note that the default schema will be used by all db.* modules. </p>
<p> db.tables returns &#8216;schema.table&#8217; if schemas are available in the database.</p>
<h3>See also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Introduction to GRASS vector map processing</p>
<dt>
<dd> Introduction to GRASS raster map processing</dl>
</dl>
<p> Main index &#8211; database index &#8211; full index </p>
<p> <i>Last changed: $Date: 2008-02-10 18:09:01 +0100 (Sun, 10 Feb 2008) $</i> </p>
<h2>Index</h2>
