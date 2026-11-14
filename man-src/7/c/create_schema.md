---
title: "create_schema(7)"
name: "create_schema"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_schema/"
description: "CREATE SCHEMA – define a new schema"
---

<p>CREATE SCHEMA &#8211; define a new schema </p>
<h2>Synopsis</h2>
<pre>CREATE SCHEMA <i>schemaname</i> [ AUTHORIZATION <i>username</i> ] [ <i>schema_element</i> [ ... ] ]
CREATE SCHEMA AUTHORIZATION <i>username</i> [ <i>schema_element</i> [ ... ] ]</pre>
<h2>Description</h2>
<p><code>CREATE SCHEMA</code> enters a new schema into the current database. The schema name must be distinct from the name of any existing schema in the current database. </p>
<p> A schema is essentially a namespace: it contains named objects (tables, data types, functions, and operators) whose names can duplicate those of other objects existing in other schemas. Named objects are accessed either by &#8220;qualifying&#8221; their names with the schema name as a prefix, or by setting a search path that includes the desired schema(s). A CREATE command specifying an unqualified object name creates the object in the current schema (the one at the front of the search path, which can be determined with the function <code>current_schema</code>). </p>
<p> Optionally, <code>CREATE SCHEMA</code> can include subcommands to create objects within the new schema. The subcommands are treated essentially the same as separate commands issued after creating the schema, except that if the AUTHORIZATION clause is used, all the created objects will be owned by that user.</p>
<h2>Parameters</h2>
<dl>
<dt><i>schemaname</i></p>
<dd>The name of a schema to be created. If this is omitted, the user name is used as the schema name. The name cannot begin with pg_, as such names are reserved for system schemas.</p>
<dt><i>username</i></p>
<dd>The name of the user who will own the schema. If omitted, defaults to the user executing the command. Only superusers can create schemas owned by users other than themselves.</p>
<dt><i>schema_element</i></p>
<dd>An SQL statement defining an object to be created within the schema. Currently, only <code>CREATE TABLE</code>, <code>CREATE VIEW</code>, <code>CREATE INDEX</code>, <code>CREATE SEQUENCE</code>, <code>CREATE TRIGGER</code> and <code>GRANT</code> are accepted as clauses within <code>CREATE SCHEMA</code>. Other kinds of objects may be created in separate commands after the schema is created.</dl>
<h2>Notes</h2>
<p>To create a schema, the invoking user must have the CREATE privilege for the current database. (Of course, superusers bypass this check.)</p>
<h2>Examples</h2>
<p>Create a schema: </p>
<pre>CREATE SCHEMA myschema;</pre>
<p>Create a schema for user joe; the schema will also be named joe: </p>
<pre>CREATE SCHEMA AUTHORIZATION joe;</pre>
<p>Create a schema and create a table and view within it: </p>
<pre>CREATE SCHEMA hollywood
 CREATE TABLE films (title text, release date, awards text[])
 CREATE VIEW winners AS
 SELECT title, release FROM films WHERE awards IS NOT NULL;</pre>
<p>Notice that the individual subcommands do not end with semicolons. </p>
<p> The following is an equivalent way of accomplishing the same result: </p>
<pre>CREATE SCHEMA hollywood;
CREATE TABLE hollywood.films (title text, release date, awards text[]);
CREATE VIEW hollywood.winners AS
 SELECT title, release FROM hollywood.films WHERE awards IS NOT NULL;</pre>
<h2>Compatibility</h2>
<p>The SQL standard allows a DEFAULT CHARACTER SET clause in <code>CREATE SCHEMA</code>, as well as more subcommand types than are presently accepted by PostgreSQL. </p>
<p> The SQL standard specifies that the subcommands in <code>CREATE SCHEMA</code> can appear in any order. The present PostgreSQL implementation does not handle all cases of forward references in subcommands; it might sometimes be necessary to reorder the subcommands in order to avoid forward references. </p>
<p> According to the SQL standard, the owner of a schema always owns all objects within it. PostgreSQL allows schemas to contain objects owned by users other than the schema owner. This can happen only if the schema owner grants the CREATE privilege on his schema to someone else.</p>
<h2>See Also</h2>
<p>ALTER SCHEMA [<code><a href="/docs/linux/man/7-alter_schema/">alter_schema</a></code>(7)], DROP SCHEMA [<code><a href="/docs/linux/man/7-drop_schema/">drop_schema</a></code>(7)] </p>
