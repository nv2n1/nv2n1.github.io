---
title: "drop_type(7)"
name: "drop_type"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_type/"
description: "DROP TYPE – remove a data type"
---

<p>DROP TYPE &#8211; remove a data type </p>
<h2>Synopsis</h2>
<pre>DROP TYPE [ IF EXISTS ] <i>name</i> [, ...] [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP TYPE</code> removes a user-defined data type. Only the owner of a type can remove it.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the type does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of the data type to remove.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the type (such as table columns, functions, operators).</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the type if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>To remove the data type <code>box</code>: </p>
<pre>DROP TYPE box;</pre>
<h2>Compatibility</h2>
<p>This command is similar to the corresponding command in the SQL standard, apart from the IF EXISTS option, which is a PostgreSQL extension. But note that the <code>CREATE TYPE</code> command and the data type extension mechanisms in PostgreSQL differ from the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE TYPE [<code><a href="/docs/linux/man/7-create_type/">create_type</a></code>(7)], ALTER TYPE [<code><a href="/docs/linux/man/7-alter_type/">alter_type</a></code>(7)] </p>
