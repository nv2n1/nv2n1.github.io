---
title: "grass-mysql(1)"
name: "grass-mysql"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grass-mysql/"
---

MySQL database driver in GRASS enables GRASS to store vector attributes in MySQL server. 

 Because vector attribute tables are created automaticaly when a new vector is written and the name of the table is the same as the name of the vector it is good practice to create a new database for each GRASS mapset.

<h2>Creating a MySQL database</h2>

 A new database is created within MySQL: 
 mysql&gt; CREATE DATABASE mydb; 
 See the MySQL manual for details.

<h2>Driver and database name</h2>

 GRASS modules require 2 parameters to connect to a database. Those parameters are 'driver' and 'database'. For MySQL driver the parameter 'driver' should be set to value 'mysql'. The parameter 'database' can be given in two formats:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 
&nbsp;<wbr>Database name - in case of connection from localhost
<dt>
<dd> 
&nbsp;<wbr>String of comma separated list of kye=value options.&nbsp;<wbr> Supported options are:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 
&nbsp;<wbr>dbname - database name
<dt>
<dd> 
&nbsp;<wbr>host - host name or IP address
<dt>
<dd> 
&nbsp;<wbr>port - server port number&nbsp;<wbr></dl>
</dl>
</dl>
</dl>
 Examples of connection parameters: 
 
&nbsp;<wbr>&nbsp;<wbr>db.connect driver=mysql database=mytest 
 
&nbsp;<wbr>&nbsp;<wbr>db.connect driver=mysql database='dbname=mytest,host=test.grass.org' 

<h2>Data types</h2>

 GRASS supports almost all MySQL data types with following limitations:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 
&nbsp;<wbr>Binary columns&nbsp;<wbr>(BINARY, VARBINARY, TINYBLOB, MEDIUMBLOB, BLOB, LONGBLOB) are not not supported. If a table with binary column(s) is used in GRASS a warning is printed and only the supported columns are returned in query results.
<dt>
<dd> 
&nbsp;<wbr>Columns of type SET and ENUM are represented as string&nbsp;<wbr>(VARCHAR).&nbsp;<wbr>
<dt>
<dd> 
&nbsp;<wbr>Very large integers in columns of type BIGINT can be lost&nbsp;<wbr> or corrupted because GRASS does not support 64 bin integeres on most platforms.
<dt>
<dd> 
&nbsp;<wbr>GRASS does not currently distinguish types TIMESTAMP and&nbsp;<wbr> DATETIME. Both types are in GRASS interpreted as TIMESTAMP.</dl>
</dl>

<h2>Indexes</h2>

 GRASS modules automaticaly create index on key column of vector attributes table. The index on key column is important for performance of modules which update the attribute table, for example v.to.db, v.distance and v.what.rast.

<h2>Privileges</h2>

 Because MySQL does not support groups of users and because only MySQL 'root' can grant privileges to other users GRASS cannot automaticaly grant select privileges on created tables to group of users. 

 If you want to give privilege to read data from your mapset to other users you have to ask your MySQL server administrator to grant select privilege to them on the MySQL database used for that mapset. For example, to allow everybody to read data in from your database 'mydb': 
 
 shell&gt; mysql --user=root mysql 
 mysql&gt; GRANT SELECT ON mydb.* TO ''@'%'; 

<h2>Schemas</h2>

 Because MySQL does not support database schemas the parameter cqschema' of module db.connect should never be set to any value. If you set that parameter for MySQL driver GRASS will try to write tables to the specified schema which will result in errors.

<h2>Groups</h2>

 MySQL does not support user groups. Any settings specified by 'group' parameter of module db.connect are ignored by GRASS for MySQL driver.

<h2>SEE ALSO</h2>

 <i> db.connect, SQL support in GRASS GIS</i>

<h2>Credits</h2>

 Development of the driver was sponsored by Faunalia (Italy) as part of a project for ATAC.

<h2>AUTHOR</h2>

 Radim Blazek 

 <i>Last changed: $Date: 2007-10-28 22:04:00 +0100 (Sun, 28 Oct 2007) $</i> 
 Help Index 

<h2>Index</h2>


