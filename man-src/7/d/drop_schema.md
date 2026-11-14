---
title: "drop_schema(7)"
name: "drop_schema"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_schema/"
description: "DROP SCHEMA – remove a schema"
---

<p>DROP SCHEMA &#8211; remove a schema </p>
<h2>Synopsis</h2>
<pre>DROP SCHEMA [ IF EXISTS ] <i>name</i> [, ...] [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP SCHEMA</code> removes schemas from the database. </p>
<p> A schema can only be dropped by its owner or a superuser. Note that the owner can drop the schema (and thereby all contained objects) even if he does not own some of the objects within the schema.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the schema does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name of a schema.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects (tables, functions, etc.) that are contained in the schema.</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the schema if it contains any objects. This is the default.</dl>
<h2>Examples</h2>
<p>To remove schema mystuff from the database, along with everything it contains: </p>
<pre>DROP SCHEMA mystuff CASCADE;</pre>
<h2>Compatibility</h2>
<p><code>DROP SCHEMA</code> is fully conforming with the SQL standard, except that the standard only allows one schema to be dropped per command, and apart from the IF EXISTS option, which is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>ALTER SCHEMA [<code><a href="/docs/linux/man/7-alter_schema/">alter_schema</a></code>(7)], CREATE SCHEMA [<code><a href="/docs/linux/man/7-create_schema/">create_schema</a></code>(7)] </p>
