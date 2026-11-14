---
title: "alter_foreign_table(7)"
name: "alter_foreign_table"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_foreign_table/"
description: "ALTER_FOREIGN_TABLE – change the definition of a foreign table"
---

<p>ALTER_FOREIGN_TABLE &#8211; change the definition of a foreign table</p>
<h2>Synopsis</h2>
<pre>ALTER FOREIGN TABLE [ IF EXISTS ] <i>name</i>
 <i>action</i> [, ... ]
ALTER FOREIGN TABLE [ IF EXISTS ] <i>name</i>
 RENAME [ COLUMN ] <i>column_name</i> TO <i>new_column_name</i>
ALTER FOREIGN TABLE [ IF EXISTS ] <i>name</i>
 RENAME TO <i>new_name</i>
ALTER FOREIGN TABLE [ IF EXISTS ] <i>name</i>
 SET SCHEMA <i>new_schema</i>
where <i>action</i> is one of:
 ADD [ COLUMN ] <i>column_name</i> <i>data_type</i> [ NULL | NOT NULL ]
 DROP [ COLUMN ] [ IF EXISTS ] <i>column_name</i> [ RESTRICT | CASCADE ]
 ALTER [ COLUMN ] <i>column_name</i> [ SET DATA ] TYPE <i>data_type</i>
 ALTER [ COLUMN ] <i>column_name</i> { SET | DROP } NOT NULL
 ALTER [ COLUMN ] <i>column_name</i> SET STATISTICS <i>integer</i>
 ALTER [ COLUMN ] <i>column_name</i> SET ( <i>attribute_option</i> = <i>value</i> [, ... ] )
 ALTER [ COLUMN ] <i>column_name</i> RESET ( <i>attribute_option</i> [, ... ] )
 ALTER [ COLUMN ] <i>column_name</i> OPTIONS ( [ ADD | SET | DROP ] <i>option</i> ['<i>value</i>'] [, ... ])
 OWNER TO <i>new_owner</i>
 OPTIONS ( [ ADD | SET | DROP ] <i>option</i> ['<i>value</i>'] [, ... ])</pre>
<h2>Description</h2>
<p><code>ALTER FOREIGN TABLE</code> changes the definition of an existing foreign table. There are several subforms: </p>
<p> ADD COLUMN</p>
<dl>
<dd>This form adds a new column to the foreign table, using the same syntax as CREATE FOREIGN TABLE (<code><a href="/docs/linux/man/7-create_foreign_table/">CREATE_FOREIGN_TABLE</a></code>(7)).</dl>
<p> DROP COLUMN [ IF EXISTS ]</p>
<dl>
<dd>This form drops a column from a foreign table. You will need to say CASCADE if anything outside the table depends on the column; for example, views. If IF EXISTS is specified and the column does not exist, no error is thrown. In this case a notice is issued instead.</dl>
<p> IF EXISTS</p>
<dl>
<dd>Do not throw an error if the foreign table does not exist. A notice is issued in this case.</dl>
<p> SET DATA TYPE</p>
<dl>
<dd>This form changes the type of a column of a foreign table.</dl>
<p> SET/DROP NOT NULL</p>
<dl>
<dd>Mark a column as allowing, or not allowing, null values.</dl>
<p> SET STATISTICS</p>
<dl>
<dd>This form sets the per-column statistics-gathering target for subsequent <code><a href="/docs/linux/man/7-analyze/">ANALYZE</a></code>(7) operations. See the similar form of ALTER TABLE (<code><a href="/docs/linux/man/7-alter_table/">ALTER_TABLE</a></code>(7)) for more details.</dl>
<p> SET ( <i>attribute_option</i> = <i>value</i> [, &#8230; ] ), RESET ( <i>attribute_option</i> [, &#8230; ] )</p>
<dl>
<dd>This form sets or resets per-attribute options. See the similar form of ALTER TABLE (<code><a href="/docs/linux/man/7-alter_table/">ALTER_TABLE</a></code>(7)) for more details.</dl>
<p> OWNER</p>
<dl>
<dd>This form changes the owner of the foreign table to the specified user.</dl>
<p> RENAME</p>
<dl>
<dd>The RENAME forms change the name of a foreign table or the name of an individual column in a foreign table.</dl>
<p> SET SCHEMA</p>
<dl>
<dd>This form moves the foreign table into another schema.</dl>
<p> OPTIONS ( [ ADD | SET | DROP ] <i>option</i> [&#8216;<i>value</i>&#8216;] [, &#8230; ] )</p>
<dl>
<dd>Change options for the foreign table or one of its columns. ADD, SET, and DROP specify the action to be performed. ADD is assumed if no operation is explicitly specified. Duplicate option names are not allowed (although it&#8217;s OK for a table option and a column option to have the same name). Option names and values are also validated using the foreign data wrapper library.</dl>
<p> All the actions except RENAME and SET SCHEMA can be combined into a list of multiple alterations to apply in parallel. For example, it is possible to add several columns and/or alter the type of several columns in a single command. </p>
<p> You must own the table to use <code>ALTER FOREIGN TABLE</code>. To change the schema of a foreign table, you must also have CREATE privilege on the new schema. To alter the owner, you must also be a direct or indirect member of the new owning role, and that role must have CREATE privilege on the table&#8217;s schema. (These restrictions enforce that altering the owner doesn&#8217;t do anything you couldn&#8217;t do by dropping and recreating the table. However, a superuser can alter ownership of any table anyway.) To add a column or alter a column type, you must also have USAGE privilege on the data type.</p>
<h2>Parameters</h2>
<p><i>name</i></p>
<dl>
<dd>The name (possibly schema-qualified) of an existing foreign table to alter.</dl>
<p> <i>column_name</i></p>
<dl>
<dd>Name of a new or existing column.</dl>
<p> <i>new_column_name</i></p>
<dl>
<dd>New name for an existing column.</dl>
<p> <i>new_name</i></p>
<dl>
<dd>New name for the table.</dl>
<p> <i>data_type</i></p>
<dl>
<dd>Data type of the new column, or new data type for an existing column.</dl>
<p> CASCADE</p>
<dl>
<dd>Automatically drop objects that depend on the dropped column (for example, views referencing the column).</dl>
<p> RESTRICT</p>
<dl>
<dd>Refuse to drop the column if there are any dependent objects. This is the default behavior.</dl>
<p> <i>new_owner</i></p>
<dl>
<dd>The user name of the new owner of the table.</dl>
<p> <i>new_schema</i></p>
<dl>
<dd>The name of the schema to which the table will be moved.</dl>
<h2>Notes</h2>
<p>The key word COLUMN is noise and can be omitted. </p>
<p> Consistency with the foreign server is not checked when a column is added or removed with ADD COLUMN or DROP COLUMN, a NOT NULL constraint is added, or a column type is changed with SET DATA TYPE. It is the user&#8217;s responsibility to ensure that the table definition matches the remote side. </p>
<p> Refer to CREATE FOREIGN TABLE (<code><a href="/docs/linux/man/7-create_foreign_table/">CREATE_FOREIGN_TABLE</a></code>(7)) for a further description of valid parameters.</p>
<h2>Examples</h2>
<p>To mark a column as not-null: </p>
<dl>
<dd>
<pre>ALTER FOREIGN TABLE distributors ALTER COLUMN street SET NOT NULL;</pre>
</dl>
<p> To change options of a foreign table: </p>
<dl>
<dd>
<pre>ALTER FOREIGN TABLE myschema.distributors OPTIONS (ADD opt1 'value', SET opt2, 'value2', DROP opt3 'value3');</pre>
</dl>
<h2>Compatibility</h2>
<p>The forms ADD, DROP, and SET DATA TYPE conform with the SQL standard. The other forms are PostgreSQL extensions of the SQL standard. Also, the ability to specify more than one manipulation in a single <code>ALTER FOREIGN TABLE</code> command is an extension. </p>
<p> <code>ALTER FOREIGN TABLE DROP COLUMN</code> can be used to drop the only column of a foreign table, leaving a zero-column table. This is an extension of SQL, which disallows zero-column foreign tables.</p>
