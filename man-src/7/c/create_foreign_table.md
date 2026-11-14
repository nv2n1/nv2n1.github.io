---
title: "create_foreign_table(7)"
name: "create_foreign_table"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_foreign_table/"
description: "CREATE_FOREIGN_TABLE – define a new foreign table"
---

<p>CREATE_FOREIGN_TABLE &#8211; define a new foreign table</p>
<h2>Synopsis</h2>
<pre>CREATE FOREIGN TABLE [ IF NOT EXISTS ] <i>table_name</i> ( [
 { <i>column_name</i> <i>data_type</i> [ OPTIONS ( <i>option</i> '<i>value</i>' [, ... ] ) ] [ NULL | NOT NULL ] }
 [, ... ]
] )
 SERVER <i>server_name</i>
[ OPTIONS ( <i>option</i> '<i>value</i>' [, ... ] ) ]</pre>
<h2>Description</h2>
<p><code>CREATE FOREIGN TABLE</code> will create a new foreign table in the current database. The table will be owned by the user issuing the command. </p>
<p> If a schema name is given (for example, CREATE FOREIGN TABLE myschema.mytable &#8230;) then the table is created in the specified schema. Otherwise it is created in the current schema. The name of the foreign table must be distinct from the name of any other foreign table, table, sequence, index, or view in the same schema. </p>
<p> <code>CREATE FOREIGN TABLE</code> also automatically creates a data type that represents the composite type corresponding to one row of the foreign table. Therefore, foreign tables cannot have the same name as any existing data type in the same schema. </p>
<p> To be able to create a table, you must have USAGE privilege on all column types.</p>
<h2>Parameters</h2>
<p>IF NOT EXISTS</p>
<dl>
<dd>Do not throw an error if a relation with the same name already exists. A notice is issued in this case. Note that there is no guarantee that the existing relation is anything like the one that would have been created.</dl>
<p> <i>table_name</i></p>
<dl>
<dd>The name (optionally schema-qualified) of the table to be created.</dl>
<p> <i>column_name</i></p>
<dl>
<dd>The name of a column to be created in the new table.</dl>
<p> <i>data_type</i></p>
<dl>
<dd>The data type of the column. This can include array specifiers. For more information on the data types supported by PostgreSQL, refer to Chapter 8, Data Types, in the documentation.</dl>
<p> NOT NULL</p>
<dl>
<dd>The column is not allowed to contain null values.</dl>
<p> NULL</p>
<dl>
<dd>The column is allowed to contain null values. This is the default. </p>
<p> This clause is only provided for compatibility with non-standard SQL databases. Its use is discouraged in new applications.</dl>
<p> <i>server_name</i></p>
<dl>
<dd>The name of an existing server for the foreign table.</dl>
<p> OPTIONS ( <i>option</i> &#8216;<i>value</i>&#8216; [, &#8230;] )</p>
<dl>
<dd>Options to be associated with the new foreign table or one of its columns. The allowed option names and values are specific to each foreign data wrapper and are validated using the foreign-data wrapper&#8217;s validator function. Duplicate option names are not allowed (although it&#8217;s OK for a table option and a column option to have the same name).</dl>
<h2>Examples</h2>
<p>Create foreign table films with film_server: </p>
<dl>
<dd>
<pre>CREATE FOREIGN TABLE films (
 code <a href="//www.systutorials.com/docs/linux/man/5-char/">char</a>(5) NOT NULL,
 title varchar(40) NOT NULL,
 did integer NOT NULL,
 date_prod date,
 kind varchar(10),
 len interval hour to minute
)
SERVER film_server;</pre>
</dl>
<h2>Compatibility</h2>
<p>The <code>CREATE FOREIGN TABLE</code> command largely conforms to the SQL standard; however, much as with <code>CREATE TABLE</code>, NULL constraints and zero-column foreign tables are permitted.</p>
<h2>See Also</h2>
<p>ALTER FOREIGN TABLE (<code><a href="/docs/linux/man/7-alter_foreign_table/">ALTER_FOREIGN_TABLE</a></code>(7)), DROP FOREIGN TABLE (<code><a href="/docs/linux/man/7-drop_foreign_table/">DROP_FOREIGN_TABLE</a></code>(7)), CREATE TABLE (<code><a href="/docs/linux/man/7-create_table/">CREATE_TABLE</a></code>(7)), CREATE SERVER (<code><a href="/docs/linux/man/7-create_server/">CREATE_SERVER</a></code>(7)) </p>
