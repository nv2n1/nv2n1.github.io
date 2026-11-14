---
title: "grass-mesql(1)"
name: "grass-mesql"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grass-mesql/"
---

MySQL database driver in GRASS enables GRASS to store vector attributes in MySQL embedded database without necessity to run MySQL server. 

<h2>Driver and database name</h2>

 GRASS modules require 2 parameters to connect to a database. Those parameters are 'driver' and 'database'. For MySQL embedded driver the parameter 'driver' should be set to value 'mesql'. The parameter 'database' is a full path to the directory where database tables are stored. The best place is a directory in the mapset. The directory must be created before use of the driver. In the name of database it is possible to use 3 variables:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 
&nbsp;<wbr>$GISDBASE - path to current GISBASE
<dt>
<dd> 
&nbsp;<wbr>$LOCATION_NAME - name of current location
<dt>
<dd> 
&nbsp;<wbr>$MAPSET - name of current mapset</dl>
</dl>
 

 Examples of connection parameters: 
 
&nbsp;<wbr>&nbsp;<wbr>db.connect driver=mesql database='$GISDBASE/$LOCATION_NAME/$MAPSET/mysql' 
 
&nbsp;<wbr>&nbsp;<wbr>db.connect driver=mesql database=/home/user1/db 

<h2>Data types, indexes</h2>

 For more informations about supported data types and indexes see the documentation for MySQL (mysql) driver

<h2>Database type</h2>

 Because database closing was found very slow if InnoDB was used, the InnoDB storage is disabled by default (hardcoded cq--skip-innodb' server option).

<h2>Note</h2>

 The embedded server is started with hardcoded '--bootstrap' option to avoid warning about missing mysql.time_zone_leap_second table. This can be fixed in future.

<h2>SEE ALSO</h2>

 <i> db.connect, SQL support in GRASS GIS</i>

<h2>Credits</h2>

 Development of the driver was sponsored by Faunalia (Italy) as part of a project for ATAC.

<h2>AUTHOR</h2>

 Radim Blazek 

 <i>Last changed: $Date: 2007-10-28 22:04:00 +0100 (Sun, 28 Oct 2007) $</i> 
 Help Index 

<h2>Index</h2>


