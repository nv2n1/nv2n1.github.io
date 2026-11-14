---
title: "drop_collation(7)"
name: "drop_collation"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_collation/"
description: "DROP_COLLATION – remove a collation"
---

<p>DROP_COLLATION &#8211; remove a collation</p>
<h2>Synopsis</h2>
<pre>DROP COLLATION [ IF EXISTS ] <i>name</i> [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP COLLATION</code> removes a previously defined collation. To be able to drop a collation, you must own the collation.</p>
<h2>Parameters</h2>
<p>IF EXISTS</p>
<dl>
<dd>Do not throw an error if the collation does not exist. A notice is issued in this case.</dl>
<p> <i>name</i></p>
<dl>
<dd>The name of the collation. The collation name can be schema-qualified.</dl>
<p> CASCADE</p>
<dl>
<dd>Automatically drop objects that depend on the collation.</dl>
<p> RESTRICT</p>
<dl>
<dd>Refuse to drop the collation if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>To drop the collation named german: </p>
<dl>
<dd>
<pre>DROP COLLATION german;</pre>
</dl>
<h2>Compatibility</h2>
<p>The <code>DROP COLLATION</code> command conforms to the SQL standard, apart from the IF EXISTS option, which is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>ALTER COLLATION (<code><a href="/docs/linux/man/7-alter_collation/">ALTER_COLLATION</a></code>(7)), CREATE COLLATION (<code><a href="/docs/linux/man/7-create_collation/">CREATE_COLLATION</a></code>(7)) </p>
