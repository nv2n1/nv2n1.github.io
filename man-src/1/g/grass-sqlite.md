---
title: "grass-sqlite(1)"
name: "grass-sqlite"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grass-sqlite/"
---

<h2>Creating a SQLite database</h2>

 GRASS is automatically creating the SQLite database if it is not yet existing. It is sufficient to define the connection (see next step).

<h2>Connecting GRASS to SQLite</h2>

 The database name 'sqlite.db' is at user's choice. Also the file storage location can be freely chosen. If the database does not exist, it will be automatically created: 
 # example for storing DB in mapset directory (keep single quotes): 
 db.connect driver=sqlite database='$GISDBASE/$LOCATION_NAME/$MAPSET/sqlite.db' 
 db.connect -p 

<h2>Supported SQL commands</h2>

 All SQL commands supported by SQLite (for limitations, see SQLite help page: SQL As Understood By SQLite).

<h2>Operators available in conditions</h2>

 All SQL operators supported by SQLite.

<h2>Browsing table data in DB</h2>

 A convenient SQLite front-end is sqlitebrowser. To open a DB file stored within the current mapset, the following way is suggested (corresponds to above database connection): 
 eval `g.gisenv` 
 # use double quotes: 
 sqlitebrowser &quot;$GISDBASE/$LOCATION_NAME/$MAPSET&quot;/sqlite.db 
 
 
 
 
 
 
 

<h2>SEE ALSO</h2>

 <i>SQLite web site, SQLite manual, db.connect, db.execute, SQL support in GRASS GIS, sqlite - Management Tools </i> 

 <i>Last changed: $Date: 2007-07-18 16:10:27 +0200 (Wed, 18 Jul 2007) $</i> 
 Help Index 

<h2>Index</h2>


