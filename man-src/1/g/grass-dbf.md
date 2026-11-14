---
title: "grass-dbf(1)"
name: "grass-dbf"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grass-dbf/"
---

<h2>Defining the DBF driver</h2>

 The DBF driver is the default driver, in theory no user interaction is required. However, if the settings should be set back from a different to the DBF driver, the following step is required: 
 # keep single quotes: 
 db.connect driver=dbf database='$GISDBASE/$LOCATION_NAME/$MAPSET/dbf/' 
 db.connect -p 
 The dbf/ subdirectory in the mapset must exist or must be created by the user.

<h2>Creating a DBF table</h2>

 Usually DBF tables are created by GRASS when generating a vector map with attributes (and using DBF as default attribute driver). 

 If a DBF table has to be created manually, db.execute can be used or a spreadsheet application. Also db.copy is sometimes useful as well as db.in.ogr to import external tables.

<h2>Supported SQL commands by DBF driver</h2>

 
 
&nbsp;<wbr>&nbsp;<wbr>ALTER TABLE table ADD&nbsp;<wbr>[COLUMN]&nbsp;<wbr>columndef 
 
&nbsp;<wbr>&nbsp;<wbr>ALTER TABLE table DROP COLUMN colname 
 
&nbsp;<wbr>&nbsp;<wbr>CREATE TABLE table&nbsp;<wbr>(&nbsp;<wbr>columndefs&nbsp;<wbr>) 
 
&nbsp;<wbr>&nbsp;<wbr>DROP TABLE table 
 
&nbsp;<wbr>&nbsp;<wbr>SELECT columns FROM table 
 
&nbsp;<wbr>&nbsp;<wbr>SELECT columns FROM table WHERE condition 
 
&nbsp;<wbr>&nbsp;<wbr>DELETE FROM table 
 
&nbsp;<wbr>&nbsp;<wbr>DELETE FROM table WHERE condition 
 
&nbsp;<wbr>&nbsp;<wbr>INSERT INTO table VALUES&nbsp;<wbr>(value1[,value2,...]) 
 
&nbsp;<wbr>&nbsp;<wbr>INSERT INTO table&nbsp;<wbr>(&nbsp;<wbr>column1[,column2,...]&nbsp;<wbr>)&nbsp;<wbr>VALUES&nbsp;<wbr>(value1[,value2,...]) 
 
&nbsp;<wbr>&nbsp;<wbr>UPDATE table SET assignment1[,assignment2,...] 
 
&nbsp;<wbr>&nbsp;<wbr>UPDATE table SET assignment1[,assignment2,...]&nbsp;<wbr>WHERE condition 

<h2>Operators available in conditions</h2>

 
 
&nbsp;<wbr>&nbsp;<wbr>&quot;=&quot;&nbsp;<wbr>&nbsp;<wbr>: equal 
 
&nbsp;<wbr>&nbsp;<wbr>&quot;&lt;&quot;&nbsp;<wbr>&nbsp;<wbr>: smaller than 
 
&nbsp;<wbr>&nbsp;<wbr>&quot;&lt;=&quot;&nbsp;<wbr>: smaller/equal than 
 
&nbsp;<wbr>&nbsp;<wbr>&quot;&gt;&quot;&nbsp;<wbr>&nbsp;<wbr>: larger than 
 
&nbsp;<wbr>&nbsp;<wbr>&quot;&gt;=&quot;&nbsp;<wbr>: larger/equal than 
 
&nbsp;<wbr>&nbsp;<wbr>&quot;&lt;&gt;&quot;&nbsp;<wbr>: not equal 
 
&nbsp;<wbr>&nbsp;<wbr>&quot;~&quot;&nbsp;<wbr>&nbsp;<wbr>: Substring matching&nbsp;<wbr>&nbsp;<wbr>(non-standard SQL) 
 
&nbsp;<wbr>&nbsp;<wbr>&quot;%&quot;&nbsp;<wbr>&nbsp;<wbr>: Substring matching&nbsp;<wbr>&nbsp;<wbr>(limited functionality) 
 

 
&nbsp;<wbr>Arithmetic expressions using constants and field values are allowed&nbsp;<wbr> in condition clauses and in the RHS of assignments. Usual precedence rules and bracketing (using '(' and ')') are supported. Type conversion is performed if necessary (experimental). 

 
&nbsp;<wbr>Aggregate functions&nbsp;<wbr>(sum, count, min, max,...)&nbsp;<wbr>are NOT currently supported&nbsp;<wbr> in SELECT clauses. 

 
&nbsp;<wbr>Mathematic functions&nbsp;<wbr>(sin, cos, exp, log,...)&nbsp;<wbr>are NOT currently supported&nbsp;<wbr> in expressions. 

 
&nbsp;<wbr>Conditions allow boolean expressions using the AND, OR and NOT operators,&nbsp;<wbr> with the usual precedence rules. 

 
&nbsp;<wbr>NULLs can be tested by&nbsp;<wbr>'colname IS NULL'&nbsp;<wbr>in conditions. The negation is&nbsp;<wbr>'colname NOT NULL'.

<h2>ERROR MESSAGES</h2>

 An error message such as: 
 DBMI-DBF driver error: 
 SQL parser error: syntax error, unexpected DESC, expecting NAME processing 'DESC' 
 indicates that a column name corresponds to a reserved SQL word (here: 'DESC'). A different column name should be used. If this happens during import with <i>v.in.ogr</i>, the <i>cnames</i> parameter can be used to assign different column names on the fly.

<h2>SEE ALSO</h2>

 <i> db.connect, SQL support in GRASS GIS 
 DBF Specifications (Shapelib) </i> 

 <i>Last changed: $Date: 2007-07-18 16:10:27 +0200 (Wed, 18 Jul 2007) $</i> 
 Help Index 

<h2>Index</h2>


