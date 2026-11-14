---
title: "alter_collation(7)"
name: "alter_collation"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_collation/"
description: "ALTER_COLLATION – change the definition of a collation"
---

<p>ALTER_COLLATION &#8211; change the definition of a collation</p>
<h2>Synopsis</h2>
<pre>ALTER COLLATION <i>name</i> RENAME TO <i>new_name</i>
ALTER COLLATION <i>name</i> OWNER TO <i>new_owner</i>
ALTER COLLATION <i>name</i> SET SCHEMA <i>new_schema</i></pre>
<h2>Description</h2>
<p><code>ALTER COLLATION</code> changes the definition of a collation. </p>
<p> You must own the collation to use <code>ALTER COLLATION</code>. To alter the owner, you must also be a direct or indirect member of the new owning role, and that role must have CREATE privilege on the collation&#8217;s schema. (These restrictions enforce that altering the owner doesn&#8217;t do anything you couldn&#8217;t do by dropping and recreating the collation. However, a superuser can alter ownership of any collation anyway.)</p>
<h2>Parameters</h2>
<p><i>name</i></p>
<dl>
<dd>The name (optionally schema-qualified) of an existing collation.</dl>
<p> <i>new_name</i></p>
<dl>
<dd>The new name of the collation.</dl>
<p> <i>new_owner</i></p>
<dl>
<dd>The new owner of the collation.</dl>
<p> <i>new_schema</i></p>
<dl>
<dd>The new schema for the collation.</dl>
<h2>Examples</h2>
<p>To rename the collation de_DE to german: </p>
<dl>
<dd>
<pre>ALTER COLLATION &quot;de_DE&quot; RENAME TO german;</pre>
</dl>
<p> To change the owner of the collation en_US to joe: </p>
<dl>
<dd>
<pre>ALTER COLLATION &quot;en_US&quot; OWNER TO joe;</pre>
</dl>
<h2>Compatibility</h2>
<p>There is no <code>ALTER COLLATION</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE COLLATION (<code><a href="/docs/linux/man/7-create_collation/">CREATE_COLLATION</a></code>(7)), DROP COLLATION (<code><a href="/docs/linux/man/7-drop_collation/">DROP_COLLATION</a></code>(7)) </p>
