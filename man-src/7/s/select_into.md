---
title: "select_into(7)"
name: "select_into"
section: "7"
letter: "s"
url: "/docs/linux/man/7-select_into/"
description: "SELECT INTO – define a new table from the results of a query"
---

<p>SELECT INTO &#8211; define a new table from the results of a query </p>
<h2>Synopsis</h2>
<pre>[ WITH [ RECURSIVE ] <i>with_query</i> [, ...] ]
SELECT [ ALL | DISTINCT [ ON ( <i>expression</i> [, ...] ) ] ]
 * | <i>expression</i> [ [ AS ] <i>output_name</i> ] [, ...]
 INTO [ TEMPORARY | TEMP ] [ TABLE ] <i>new_table</i>
 [ FROM <i>from_item</i> [, ...] ]
 [ WHERE <i>condition</i> ]
 [ GROUP BY <i>expression</i> [, ...] ]
 [ HAVING <i>condition</i> [, ...] ]
 [ WINDOW <i>window_name</i> AS ( <i>window_definition</i> ) [, ...] ]
 [ { UNION | INTERSECT | EXCEPT } [ ALL ] <i>select</i> ]
 [ ORDER BY <i>expression</i> [ ASC | DESC | USING <i>operator</i> ] [ NULLS { FIRST | LAST } ] [, ...] ]
 [ LIMIT { <i>count</i> | ALL } ]
 [ OFFSET <i>start</i> [ ROW | ROWS ] ]
 [ FETCH { FIRST | NEXT } [ <i>count</i> ] { ROW | ROWS } ONLY ]
 [ FOR { UPDATE | SHARE } [ OF <i>table_name</i> [, ...] ] [ NOWAIT ] [...] ]</pre>
<h2>Description</h2>
<p><code>SELECT INTO</code> creates a new table and fills it with data computed by a query. The data is not returned to the client, as it is with a normal <code>SELECT</code>. The new table&#8217;s columns have the names and data types associated with the output columns of the <code>SELECT</code>.</p>
<h2>Parameters</h2>
<dl>
<dt><code>TEMPORARY or TEMP</code></p>
<dd>If specified, the table is created as a temporary table. Refer to CREATE TABLE [<code><a href="/docs/linux/man/7-create_table/">create_table</a></code>(7)] for details.</p>
<dt><i>new_table</i></p>
<dd>The name (optionally schema-qualified) of the table to be created.</dl>
<p> All other parameters are described in detail under SELECT [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)].</p>
<h2>Notes</h2>
<p>CREATE TABLE AS [<code><a href="/docs/linux/man/7-create_table_as/">create_table_as</a></code>(7)] is functionally similar to <code>SELECT INTO</code>. <code>CREATE TABLE AS</code> is the recommended syntax, since this form of <code>SELECT INTO</code> is not available in <code>ECPG</code> or <code>PL/pgSQL</code>, because they interpret the INTO clause differently. Furthermore, <code>CREATE TABLE AS</code> offers a superset of the functionality provided by <code>SELECT INTO</code>. </p>
<p> Prior to PostgreSQL 8.1, the table created by <code>SELECT INTO</code> included OIDs by default. In PostgreSQL 8.1, this is not the case &#8212; to include OIDs in the new table, the default_with_oids configuration variable must be enabled. Alternatively, <code>CREATE TABLE AS</code> can be used with the WITH OIDS clause.</p>
<h2>Examples</h2>
<p>Create a new table films_recent consisting of only recent entries from the table films: </p>
<pre>SELECT * INTO films_recent FROM films WHERE date_prod &gt;= '2002-01-01';</pre>
<h2>Compatibility</h2>
<p>The SQL standard uses <code>SELECT INTO</code> to represent selecting values into scalar variables of a host program, rather than creating a new table. This indeed is the usage found in <code>ECPG</code> (see in the documentation) and <code>PL/pgSQL</code> (see in the documentation). The PostgreSQL usage of <code>SELECT INTO</code> to represent table creation is historical. It is best to use <code>CREATE TABLE AS</code> for this purpose in new code.</p>
<h2>See Also</h2>
<p>CREATE TABLE AS [<code><a href="/docs/linux/man/7-create_table_as/">create_table_as</a></code>(7)] </p>
