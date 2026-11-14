---
title: "alter_schema(7)"
name: "alter_schema"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_schema/"
description: "ALTER SCHEMA – change the definition of a schema"
---

<p>ALTER SCHEMA &#8211; change the definition of a schema </p>
<h2>Synopsis</h2>
<pre>ALTER SCHEMA <i>name</i> RENAME TO <i>newname</i>
ALTER SCHEMA <i>name</i> OWNER TO <i>newowner</i></pre>
<h2>Description</h2>
<p><code>ALTER SCHEMA</code> changes the definition of a schema. </p>
<p> You must own the schema to use <code>ALTER SCHEMA</code>. To rename a schema you must also have the CREATE privilege for the database. To alter the owner, you must also be a direct or indirect member of the new owning role, and you must have the CREATE privilege for the database. (Note that superusers have all these privileges automatically.)</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of an existing schema.</p>
<dt><i>newname</i></p>
<dd>The new name of the schema. The new name cannot begin with pg_, as such names are reserved for system schemas.</p>
<dt><i>newowner</i></p>
<dd>The new owner of the schema.</dl>
<h2>Compatibility</h2>
<p>There is no <code>ALTER SCHEMA</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE SCHEMA [<code><a href="/docs/linux/man/7-create_schema/">create_schema</a></code>(7)], DROP SCHEMA [<code><a href="/docs/linux/man/7-drop_schema/">drop_schema</a></code>(7)] </p>
