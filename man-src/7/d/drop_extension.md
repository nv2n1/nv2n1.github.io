---
title: "drop_extension(7)"
name: "drop_extension"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_extension/"
description: "DROP_EXTENSION – remove an extension"
---

<p>DROP_EXTENSION &#8211; remove an extension</p>
<h2>Synopsis</h2>
<pre>DROP EXTENSION [ IF EXISTS ] <i>name</i> [, ...] [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP EXTENSION</code> removes extensions from the database. Dropping an extension causes its component objects to be dropped as well. </p>
<p> You must own the extension to use <code>DROP EXTENSION</code>.</p>
<h2>Parameters</h2>
<p>IF EXISTS</p>
<dl>
<dd>Do not throw an error if the extension does not exist. A notice is issued in this case.</dl>
<p> <i>name</i></p>
<dl>
<dd>The name of an installed extension.</dl>
<p> CASCADE</p>
<dl>
<dd>Automatically drop objects that depend on the extension.</dl>
<p> RESTRICT</p>
<dl>
<dd>Refuse to drop the extension if any objects depend on it (other than its own member objects and other extensions listed in the same <code>DROP</code> command). This is the default.</dl>
<h2>Examples</h2>
<p>To remove the extension hstore from the current database: </p>
<dl>
<dd>
<pre>DROP EXTENSION hstore;</pre>
</dl>
<p> This command will fail if any of hstore&#8217;s objects are in use in the database, for example if any tables have columns of the hstore type. Add the CASCADE option to forcibly remove those dependent objects as well.</p>
<h2>Compatibility</h2>
<p><code>DROP EXTENSION</code> is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>CREATE EXTENSION (<code><a href="/docs/linux/man/7-create_extension/">CREATE_EXTENSION</a></code>(7)), ALTER EXTENSION (<code><a href="/docs/linux/man/7-alter_extension/">ALTER_EXTENSION</a></code>(7)) </p>
