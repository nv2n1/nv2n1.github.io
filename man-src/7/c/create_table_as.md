---
title: "create_table_as(7)"
name: "create_table_as"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_table_as/"
description: "CREATE TABLE AS – define a new table from the results of a query"
---

<p>CREATE TABLE AS &#8211; define a new table from the results of a query </p>
<h2>Synopsis</h2>
<pre>CREATE [ [ GLOBAL | LOCAL ] { TEMPORARY | TEMP } ] TABLE <i>table_name</i>
 [ (<i>column_name</i> [, ...] ) ]
 [ WITH ( <i>storage_parameter</i> [= <i>value</i>] [, ... ] ) | WITH OIDS | WITHOUT OIDS ]
 [ ON COMMIT { PRESERVE ROWS | DELETE ROWS | DROP } ]
 [ TABLESPACE <i>tablespace</i> ]
 AS <i>query</i>
 [ WITH [ NO ] DATA ]</pre>
<h2>Description</h2>
<p><code>CREATE TABLE AS</code> creates a table and fills it with data computed by a <code>SELECT</code> command. The table columns have the names and data types associated with the output columns of the <code>SELECT</code> (except that you can override the column names by giving an explicit list of new column names). </p>
<p> <code>CREATE TABLE AS</code> bears some resemblance to creating a view, but it is really quite different: it creates a new table and evaluates the query just once to fill the new table initially. The new table will not track subsequent changes to the source tables of the query. In contrast, a view re-evaluates its defining <code>SELECT</code> statement whenever it is queried.</p>
<h2>Parameters</h2>
<dl>
<dt><code>GLOBAL or LOCAL</code></p>
<dd>Ignored for compatibility. Refer to CREATE TABLE [<code><a href="/docs/linux/man/7-create_table/">create_table</a></code>(7)] for details.</dl>
<dl>
<dt><code>TEMPORARY or TEMP</code></p>
<dd>If specified, the table is created as a temporary table. Refer to CREATE TABLE [<code><a href="/docs/linux/man/7-create_table/">create_table</a></code>(7)] for details.</p>
<dt><i>table_name</i></p>
<dd>The name (optionally schema-qualified) of the table to be created.</p>
<dt><i>column_name</i></p>
<dd>The name of a column in the new table. If column names are not provided, they are taken from the output column names of the query. If the table is created from an <code>EXECUTE</code> command, a column name list cannot be specified.</p>
<dt><code>WITH ( </code><i>storage_parameter</i><code> [= </code><i>value</i><code>] [, &#8230; ] )</code></p>
<dd>This clause specifies optional storage parameters for the new table; see Storage Parameters [<code><a href="/docs/linux/man/7-create_table/">create_table</a></code>(7)] for more information. The WITH clause can also include OIDS=TRUE (or just OIDS) to specify that rows of the new table should have OIDs (object identifiers) assigned to them, or OIDS=FALSE to specify that the rows should not have OIDs. See CREATE TABLE [<code><a href="/docs/linux/man/7-create_table/">create_table</a></code>(7)] for more information.</p>
<dt><code>WITH OIDS</code></p>
<dd>
<dt><code>WITHOUT OIDS</code></p>
<dd>These are obsolescent syntaxes equivalent to WITH (OIDS) and WITH (OIDS=FALSE), respectively. If you wish to give both an OIDS setting and storage parameters, you must use the WITH ( &#8230; ) syntax; see above.</p>
<dt><code>ON COMMIT</code></p>
<dd>The behavior of temporary tables at the end of a transaction block can be controlled using ON COMMIT. The three options are:</p>
<dl>
<dd>
<dl>
<dt><code>PRESERVE ROWS</code></p>
<dd>No special action is taken at the ends of transactions. This is the default behavior.</p>
<dt><code>DELETE ROWS</code></p>
<dd>All rows in the temporary table will be deleted at the end of each transaction block. Essentially, an automatic TRUNCATE [<code><a href="/docs/linux/man/7-truncate/">truncate</a></code>(7)] is done at each commit.</p>
<dt><code>DROP</code></p>
<dd>The temporary table will be dropped at the end of the current transaction block.</dl>
</dl>
</dl>
<dl>
<dt><code>TABLESPACE </code><i>tablespace</i></p>
<dd>The <i>tablespace</i> is the name of the tablespace in which the new table is to be created. If not specified, default_tablespace is consulted, or temp_tablespaces if the table is temporary.</p>
<dt><i>query</i></p>
<dd>A SELECT [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)], TABLE, or VALUES [<code><a href="/docs/linux/man/7-values/">values</a></code>(7)] command, or an EXECUTE [<code><a href="/docs/linux/man/7-execute/">execute</a></code>(7)] command that runs a prepared <code>SELECT</code>, <code>TABLE</code>, or <code>VALUES</code> query.</p>
<dt><code>WITH [ NO ] DATA</code></p>
<dd>This clause specifies whether or not the data produced by the query should be copied into the new table. If not, only the table structure is copied. The default is to copy the data.</dl>
<h2>Notes</h2>
<p>This command is functionally similar to SELECT INTO [<code><a href="/docs/linux/man/7-select_into/">select_into</a></code>(7)], but it is preferred since it is less likely to be confused with other uses of the <code>SELECT INTO</code> syntax. Furthermore, <code>CREATE TABLE AS</code> offers a superset of the functionality offered by <code>SELECT INTO</code>. </p>
<p> Prior to PostgreSQL 8.0, <code>CREATE TABLE AS</code> always included OIDs in the table it created. As of PostgreSQL 8.0, the <code>CREATE TABLE AS</code> command allows the user to explicitly specify whether OIDs should be included. If the presence of OIDs is not explicitly specified, the default_with_oids configuration variable is used. As of PostgreSQL 8.1, this variable is false by default, so the default behavior is not identical to pre-8.0 releases. Applications that require OIDs in the table created by <code>CREATE TABLE AS</code> should explicitly specify WITH (OIDS) to ensure proper behavior.</p>
<h2>Examples</h2>
<p>Create a new table films_recent consisting of only recent entries from the table films: </p>
<pre>CREATE TABLE films_recent AS
 SELECT * FROM films WHERE date_prod &gt;= '2002-01-01';</pre>
<p>To copy a table completely, the short form using the TABLE command can also be used: </p>
<pre>CREATE TABLE films2 AS
 TABLE films;</pre>
<p>Create a new temporary table films_recent, consisting of only recent entries from the table films, using a prepared statement. The new table has OIDs and will be dropped at commit: </p>
<pre>PREPARE recentfilms(date) AS
 SELECT * FROM films WHERE date_prod &gt; $1;
CREATE TEMP TABLE films_recent WITH (OIDS) ON COMMIT DROP AS
 EXECUTE recentfilms('2002-01-01');</pre>
<h2>Compatibility</h2>
<p><code>CREATE TABLE AS</code> conforms to the SQL standard. The following are nonstandard extensions:</p>
<dl>
<dt>*</p>
<dd>The standard requires parentheses around the subquery clause; in PostgreSQL, these parentheses are optional.</p>
<dt>*</p>
<dd>In the standard, the WITH [ NO ] DATA clause is required; in PostgreSQL it is optional.</p>
<dt>*</p>
<dd>PostgreSQL handles temporary tables in a way rather different from the standard; see CREATE TABLE [<code><a href="/docs/linux/man/7-create_table/">create_table</a></code>(7)] for details.</p>
<dt>*</p>
<dd>The WITH clause is a PostgreSQL extension; neither storage parameters nor OIDs are in the standard.</p>
<dt>*</p>
<dd>The PostgreSQL concept of tablespaces is not part of the standard. Hence, the clause TABLESPACE is an extension.</dl>
<h2>See Also</h2>
<p>CREATE TABLE [<code><a href="/docs/linux/man/7-create_table/">create_table</a></code>(7)], EXECUTE [<code><a href="/docs/linux/man/7-execute/">execute</a></code>(7)], SELECT [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)], SELECT INTO [<code><a href="/docs/linux/man/7-select_into/">select_into</a></code>(7)], VALUES [<code><a href="/docs/linux/man/7-values/">values</a></code>(7)] </p>
