---
title: "sql(1)"
name: "sql"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sql/"
---

<h2>SQL support in GRASS GIS</h2>

 GRASS can use various RDBMS and embedded databases. SQL queries are directly passed to the underlying database system. The set of supported SQL commands depends on the RDMBS and driver selected.

<h2>Drivers</h2>

 The list of available drivers can vary in various binary distributions of GRASS. 

 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| dbf<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| DBF files. Data are stored in DBF files.
 | <a rel="nofollow" HREF="http://shapelib.maptools.org/dbf_api.html">http://shapelib.maptools.org/dbf_api.html</a> 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| sqlite<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| SQLite embedded database.
 | <a rel="nofollow" HREF="http://sqlite.org/">http://sqlite.org/</a> 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| pg<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| PostgreSQL RDBMS.
 | <a rel="nofollow" HREF="http://postgresql.org/">http://postgresql.org/</a> 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| mysql<tt>&nbsp;<wbr></tt>| MySQL RDBMS.
 | <a rel="nofollow" HREF="http://mysql.org/">http://mysql.org/</a> 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| mesql<tt>&nbsp;<wbr></tt>| MySQL embedded database.
 | <a rel="nofollow" HREF="http://mysql.org/">http://mysql.org/</a> 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| odbc<tt>&nbsp;<wbr>&nbsp;<wbr></tt>| UnixODBC. (PostgreSQL, Oracle, etc.)
 | <a rel="nofollow" HREF="http://www.unixodbc.org/">http://www.unixodbc.org/</a>

<h2>NOTES</h2>

<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 
&nbsp;<wbr>SQL does not support&nbsp;<wbr>'.'&nbsp;<wbr>(dots)&nbsp;<wbr>in table names.
<dt>
<dd> 
&nbsp;<wbr>Supported table name characters are only: 
 [A-Za-z][A-Za-z0-9_]*
<dt>
<dd> 
&nbsp;<wbr>A table name must start with a character, not a number.
<dt>
<dd> 
&nbsp;<wbr>Text-string matching requires the text part to be&nbsp;<wbr>'single quoted'. When run from the command line multiple queries should be contained in &quot;double quotes&quot;. e.g. 
 
 d.vect map where=&quot;individual='juvenile' and area='beach'&quot; 

<dt>
<dd> 
&nbsp;<wbr>An error message such as&nbsp;<wbr>&quot;dbmi: Protocol error&quot;&nbsp;<wbr>either indicates an invalid column name or an unsupported column type (then the GRASS SQL parser needs to be extended).
<dt>
<dd> 
&nbsp;<wbr>DBF column names are limited to 10 characters&nbsp;<wbr>(DBF API definition)</dl>
</dl>

<h2>EXAMPLES</h2>

 Display all vector points except for LAMAR valley and <i>extensive trapping</i> (brackets are superfluous in this example): 
 d.vect trapping_sites_points fcol=black icon=basic/diamond col=white size=13 rs 
 
&nbsp;<wbr>where=&quot;valley&nbsp;<wbr>&lt;&gt;&nbsp;<wbr>'LAMAR'&nbsp;<wbr>OR&nbsp;<wbr>(valley&nbsp;<wbr>=&nbsp;<wbr>'LAMAR'&nbsp;<wbr>AND description&nbsp;<wbr>=&nbsp;<wbr>'extensive trapping')&quot; 
 

 Select all attributes from table where str1 column values are not 'No Name': 
 echo &quot;SELECT * FROM archsites WHERE str1 &lt;&gt; 'No Name'&quot; | db.select 
 

 

 Example of subquery expressions from a list (does not work for DBF driver): 
 v.db.select mysites where=&quot;id IN ('P04', 'P05')&quot; 
 

 Example of pattern matching: 
 # match exactly number of characters (here: 2), does not work for DBF driver: 
 v.db.select mysites where=&quot;id LIKE 'P__'&quot; 
 
 #define wildcard: 
 v.db.select mysites where=&quot;id LIKE 'P%'&quot; 
 

 Example of null handling: 
 v.db.addcol map=roads col=&quot;nulltest int&quot; 
 v.db.update map=roads col=nulltest value=1 where=&quot;cat &gt; 2&quot; 
 d.vect roads where=&quot;nulltest is null&quot; 
 v.db.update map=roads col=nulltest value=2 where=&quot;cat &lt;= 2&quot; 
 

 Examples of complex expressions in updates (using v.db.* modules): 
 v.db.addcol map=roads col=&quot;exprtest double precision&quot; 
 v.db.update map=roads col=exprtest value=cat/nulltest 
 v.db.update map=roads col=exprtest value=cat/nulltest+cat where=cat=1 
 

 Examples of complex expressions in updates (using db.* modules): 
 echo &quot;UPDATE roads SET exprtest=null&quot; 
 echo &quot;UPDATE roads SET exprtest=cat/2&quot; | db.execute 
 echo &quot;UPDATE roads SET exprtest=cat/2+cat/3&quot; | db.execute 
 echo &quot;UPDATE roads SET exprtest=NULL WHERE cat&gt;2&quot; | db.execute 
 echo &quot;UPDATE roads SET exprtest=cat/3*(cat+1) WHERE exprtest IS NULL&quot; | db.execute&quot; 
 

 Instead of creating and updating new columns with an expression, you can use the expression directly in a command: 
 d.vect roads where=&quot;(cat/3*(cat+1))&gt;8&quot; 
 d.vect roads where=&quot;cat&gt;exprtest&quot; 

<h2>SEE ALSO</h2>

 Database management in GRASS GIS, 
 Help pages for database modules, 
 SQL Guide and Reference (Red Hat) 

 <i>Last changed: $Date: 2007-01-28 15:33:29 +0100 (Sun, 28 Jan 2007) $</i> 
 Help Index 

<h2>Index</h2>


