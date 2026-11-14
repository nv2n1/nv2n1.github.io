---
title: "drop_foreign_data_wrapper(7)"
name: "drop_foreign_data_wrapper"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_foreign_data_wrapper/"
description: "DROP FOREIGN DATA WRAPPER – remove a foreign-data wrapper"
---

<p>DROP FOREIGN DATA WRAPPER &#8211; remove a foreign-data wrapper </p>
<h2>Synopsis</h2>
<pre>DROP FOREIGN DATA WRAPPER [ IF EXISTS ] <i>name</i> [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP FOREIGN DATA WRAPPER</code> removes an existing foreign-data wrapper. To execute this command, the current user must be the owner of the foreign-data wrapper.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the foreign-data wrapper does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name of an existing foreign-data wrapper.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the foreign-data wrapper (such as servers).</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the foreign-data wrappers if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>Drop the foreign-data wrapper dbi: </p>
<pre>DROP FOREIGN DATA WRAPPER dbi;</pre>
<h2>Compatibility</h2>
<p><code>DROP FOREIGN DATA WRAPPER</code> conforms to ISO/IEC 9075-9 (SQL/MED). The IF EXISTS clause is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>CREATE FOREIGN DATA WRAPPER [<code><a href="/docs/linux/man/7-create_foreign_data_wrapper/">create_foreign_data_wrapper</a></code>(7)], ALTER FOREIGN DATA WRAPPER [<code><a href="/docs/linux/man/7-alter_foreign_data_wrapper/">alter_foreign_data_wrapper</a></code>(7)] </p>
