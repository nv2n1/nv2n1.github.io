---
title: "grass-odbc(1)"
name: "grass-odbc"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grass-odbc/"
description: "Communication between GRASS and ODBC database for attribute management:"
---

<p>Communication between GRASS and ODBC database for attribute management: </p>
<p> | GRASS module | | ODBC Interface | | RDBMS<br />
 | <i></i><code>GRASS</code> | <i></i><code>DBMI driver</code> | <i></i><code>unixODBC</code> | <i></i><code>ODBC driver</code> | <i></i><code>PostgreSQL</code><br />
 | <i></i><code>Oracle</code><br />
 | <i></i><code>&#8230;</code></p>
<h2>Supported SQL commands</h2>
<p> All SQL commands supported by ODBC.</p>
<h2>Operators available in conditions</h2>
<p> All SQL operators supported by ODBC.</p>
<h2>EXAMPLE</h2>
<p> In this example we copy the dbf file of a SHAPE map into ODBC, then connect GRASS to the ODBC DBMS. Usually the table will be already present in the DBMS.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Configure ODBC driver for selected database (manually or with &#8216;ODBCConfig&#8217;). ODBC drivers are defined in /etc/odbcinst.ini. Here is example: </p>
<p>&nbsp;<wbr>[PostgreSQL] </p>
<p>&nbsp;<wbr>Description&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>ODBC for PostgreSQL </p>
<p>&nbsp;<wbr>Driver&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>/usr/lib/libodbcpsql.so </p>
<p>&nbsp;<wbr>Setup&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>/usr/lib/libodbcpsqlS.so<br />
 FileUsage = 1</p>
<dt>
<dd>
&nbsp;<wbr>Create DSN&nbsp;<wbr>(data source name). The DSN is used as database name in db.* modules. Then DSN must be defined in $HOME/.odbc.ini (for this user only) or in /etc/odbc.ini for (for all users) [watch out for the database name which appears twice and also for the PostgreSQL protocol version]. Omit blanks at the beginning of lines: </p>
<p>&nbsp;<wbr>[grass6test] </p>
<p>&nbsp;<wbr>Description&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>PostgreSQL </p>
<p>&nbsp;<wbr>Driver&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>PostgreSQL </p>
<p>&nbsp;<wbr>Trace&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>No </p>
<p>&nbsp;<wbr>TraceFile&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>= </p>
<p>&nbsp;<wbr>Database&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>grass6test </p>
<p>&nbsp;<wbr>Servername&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>localhost </p>
<p>&nbsp;<wbr>UserName&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>neteler </p>
<p>&nbsp;<wbr>Password&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>= </p>
<p>&nbsp;<wbr>Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>5432 </p>
<p>&nbsp;<wbr>Protocol&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>8.0&nbsp;<wbr> </p>
<p>&nbsp;<wbr>ReadOnly&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>No </p>
<p>&nbsp;<wbr>RowVersioning&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>No </p>
<p>&nbsp;<wbr>ShowSystemTables&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>No </p>
<p>&nbsp;<wbr>ShowOidColumn&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>No </p>
<p>&nbsp;<wbr>FakeOidIndex&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>No<br />
 ConnSettings = Configuration of an DSN without GUI is described on <a rel="nofollow" href="http://www.unixodbc.org/odbcinst.html,">http://www.unixodbc.org/odbcinst.html,</a> but odbc.ini and .odbc.ini may be created by the &#8216;ODBCConfig&#8217; tool. You can easily view your DSN structure by &#8216;DataManager&#8217;. Configuration with GUI is described on <a rel="nofollow" href="http://www.unixodbc.org/doc/UserManual/">http://www.unixodbc.org/doc/UserManual/</a></dl>
<p> To find out about your PostgreSQL protocol, run: </p>
<p> psql -V </p>
<dl>
<dt>
<dd> Now create a new database if not yet existing:<br />
 db.createdb driver=odbc database=grass6test </p>
<dt>
<dd> Now store the table &#8216;mytable.dbf&#8217; (here: in current directory) into PostgreSQL through ODBC:<br />
 db.connect driver=odbc database=grass6test<br />
 db.copy from_driver=dbf from_database=./ from_table=mytable rs </p>
<p>&nbsp;<wbr>&nbsp;<wbr>to_driver=odbc to_database=grass6test to_table=mytable </p>
<dt>
<dd>
&nbsp;<wbr>Next link map to attribute table&nbsp;<wbr>(now the ODBC table is used, not the dbf file):<br />
 v.db.connect map=mytable.shp table=mytable key=ID rs </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>database=grass6test driver=odbc<br />
 v.db.connect -p </p>
<dt>
<dd> Finally a test: Here we should see the table columns (if the ODBC connection works):<br />
 db.tables -p<br />
 db.columns table=mytable </p>
<p> Now the table name &#8216;mytable&#8217; should appear.</dl>
<p> Doesn&#8217;t work? Check with &#8216;isql &#8216; if the ODBC-PostgreSQL connection is really established.</dl>
<p> Note that you can also connect mySQL, Oracle etc. through ODBC to GRASS. You can also check the vector map itself concerning a current link to a table:<br />
 v.db.connect -p mytable.shp<br />
 which should print the database connection through ODBC to the defined RDBMS.</p>
<h2>SEE ALSO</h2>
<p> <i> db.connect, v.db.connect, unixODBC web site, SQL support in GRASS GIS</i> </p>
<p> <i>Last changed: $Date: 2007-07-18 16:10:27 +0200 (Wed, 18 Jul 2007) $</i><br />
 Help Index </p>
<h2>Index</h2>
