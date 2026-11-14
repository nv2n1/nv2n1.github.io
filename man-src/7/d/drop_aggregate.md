---
title: "drop_aggregate(7)"
name: "drop_aggregate"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_aggregate/"
description: "DROP AGGREGATE – remove an aggregate function"
---

<p>DROP AGGREGATE &#8211; remove an aggregate function </p>
<h2>Synopsis</h2>
<pre>DROP AGGREGATE [ IF EXISTS ] <i>name</i> ( <i>type</i> [ , ... ] ) [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP AGGREGATE</code> removes an existing aggregate function. To execute this command the current user must be the owner of the aggregate function.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the aggregate does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing aggregate function.</p>
<dt><i>type</i></p>
<dd>An input data type on which the aggregate function operates. To reference a zero-argument aggregate function, write * in place of the list of input data types.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the aggregate function.</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the aggregate function if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>To remove the aggregate function myavg for type <code>integer</code>: </p>
<pre>DROP AGGREGATE myavg(integer);</pre>
<h2>Compatibility</h2>
<p>There is no <code>DROP AGGREGATE</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>ALTER AGGREGATE [<code><a href="/docs/linux/man/7-alter_aggregate/">alter_aggregate</a></code>(7)], CREATE AGGREGATE [<code><a href="/docs/linux/man/7-create_aggregate/">create_aggregate</a></code>(7)] </p>
