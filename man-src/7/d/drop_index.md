---
title: "drop_index(7)"
name: "drop_index"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_index/"
description: "DROP INDEX – remove an index"
---

<p>DROP INDEX &#8211; remove an index </p>
<h2>Synopsis</h2>
<pre>DROP INDEX [ IF EXISTS ] <i>name</i> [, ...] [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP INDEX</code> drops an existing index from the database system. To execute this command you must be the owner of the index.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the index does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an index to remove.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the index.</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the index if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>This command will remove the index title_idx: </p>
<pre>DROP INDEX title_idx;</pre>
<h2>Compatibility</h2>
<p><code>DROP INDEX</code> is a PostgreSQL language extension. There are no provisions for indexes in the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE INDEX [<code><a href="/docs/linux/man/7-create_index/">create_index</a></code>(7)] </p>
