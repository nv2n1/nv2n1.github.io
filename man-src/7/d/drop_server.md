---
title: "drop_server(7)"
name: "drop_server"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_server/"
description: "DROP SERVER – remove a foreign server descriptor"
---

<p>DROP SERVER &#8211; remove a foreign server descriptor </p>
<h2>Synopsis</h2>
<pre>DROP SERVER [ IF EXISTS ] <i>servername</i> [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP SERVER</code> removes an existing foreign server descriptor. To execute this command, the current user must be the owner of the server.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the server does not exist. A notice is issued in this case.</p>
<dt><i>servername</i></p>
<dd>The name of an existing server.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the server (such as user mappings).</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the server if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>Drop a server foo if it exists: </p>
<pre>DROP SERVER IF EXISTS foo;</pre>
<h2>Compatibility</h2>
<p><code>DROP SERVER</code> conforms to ISO/IEC 9075-9 (SQL/MED). The IF EXISTS clause is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>CREATE SERVER [<code><a href="/docs/linux/man/7-create_server/">create_server</a></code>(7)], ALTER SERVER [<code><a href="/docs/linux/man/7-alter_server/">alter_server</a></code>(7)] </p>
