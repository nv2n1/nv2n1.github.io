---
title: "drop_table(7)"
name: "drop_table"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_table/"
description: "DROP TABLE – remove a table"
---

<p>DROP TABLE &#8211; remove a table </p>
<h2>Synopsis</h2>
<pre>DROP TABLE [ IF EXISTS ] <i>name</i> [, ...] [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP TABLE</code> removes tables from the database. Only its owner can drop a table. To empty a table of rows without destroying the table, use DELETE [<code><a href="/docs/linux/man/7-delete/">delete</a></code>(7)] or TRUNCATE [<code><a href="/docs/linux/man/7-truncate/">truncate</a></code>(7)]. </p>
<p> <code>DROP TABLE</code> always removes any indexes, rules, triggers, and constraints that exist for the target table. However, to drop a table that is referenced by a view or a foreign-key constraint of another table, CASCADE must be specified. (CASCADE will remove a dependent view entirely, but in the foreign-key case it will only remove the foreign-key constraint, not the other table entirely.)</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the table does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of the table to drop.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the table (such as views).</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the table if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>To destroy two tables, films and distributors: </p>
<pre>DROP TABLE films, distributors;</pre>
<h2>Compatibility</h2>
<p>This command conforms to the SQL standard, except that the standard only allows one table to be dropped per command, and apart from the IF EXISTS option, which is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>ALTER TABLE [<code><a href="/docs/linux/man/7-alter_table/">alter_table</a></code>(7)], CREATE TABLE [<code><a href="/docs/linux/man/7-create_table/">create_table</a></code>(7)] </p>
