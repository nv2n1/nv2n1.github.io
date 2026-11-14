---
title: "drop_view(7)"
name: "drop_view"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_view/"
description: "DROP VIEW – remove a view"
---

<p>DROP VIEW &#8211; remove a view </p>
<h2>Synopsis</h2>
<pre>DROP VIEW [ IF EXISTS ] <i>name</i> [, ...] [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP VIEW</code> drops an existing view. To execute this command you must be the owner of the view.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the view does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of the view to remove.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the view (such as other views).</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the view if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>This command will remove the view called kinds: </p>
<pre>DROP VIEW kinds;</pre>
<h2>Compatibility</h2>
<p>This command conforms to the SQL standard, except that the standard only allows one view to be dropped per command, and apart from the IF EXISTS option, which is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>ALTER VIEW [<code><a href="/docs/linux/man/7-alter_view/">alter_view</a></code>(7)], CREATE VIEW [<code><a href="/docs/linux/man/7-create_view/">create_view</a></code>(7)] </p>
