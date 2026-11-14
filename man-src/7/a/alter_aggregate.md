---
title: "alter_aggregate(7)"
name: "alter_aggregate"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_aggregate/"
description: "ALTER AGGREGATE – change the definition of an aggregate function"
---

<p>ALTER AGGREGATE &#8211; change the definition of an aggregate function </p>
<h2>Synopsis</h2>
<pre>ALTER AGGREGATE <i>name</i> ( <i>type</i> [ , ... ] ) RENAME TO <i>new_name</i>
ALTER AGGREGATE <i>name</i> ( <i>type</i> [ , ... ] ) OWNER TO <i>new_owner</i>
ALTER AGGREGATE <i>name</i> ( <i>type</i> [ , ... ] ) SET SCHEMA <i>new_schema</i></pre>
<h2>Description</h2>
<p><code>ALTER AGGREGATE</code> changes the definition of an aggregate function. </p>
<p> You must own the aggregate function to use <code>ALTER AGGREGATE</code>. To change the schema of an aggregate function, you must also have CREATE privilege on the new schema. To alter the owner, you must also be a direct or indirect member of the new owning role, and that role must have CREATE privilege on the aggregate function&#8217;s schema. (These restrictions enforce that altering the owner doesn&#8217;t do anything you couldn&#8217;t do by dropping and recreating the aggregate function. However, a superuser can alter ownership of any aggregate function anyway.)</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing aggregate function.</p>
<dt><i>type</i></p>
<dd>An input data type on which the aggregate function operates. To reference a zero-argument aggregate function, write * in place of the list of input data types.</p>
<dt><i>new_name</i></p>
<dd>The new name of the aggregate function.</p>
<dt><i>new_owner</i></p>
<dd>The new owner of the aggregate function.</p>
<dt><i>new_schema</i></p>
<dd>The new schema for the aggregate function.</dl>
<h2>Examples</h2>
<p>To rename the aggregate function myavg for type <code>integer</code> to my_average: </p>
<pre>ALTER AGGREGATE myavg(integer) RENAME TO my_average;</pre>
<p>To change the owner of the aggregate function myavg for type <code>integer</code> to joe: </p>
<pre>ALTER AGGREGATE myavg(integer) OWNER TO joe;</pre>
<p>To move the aggregate function myavg for type <code>integer</code> into schema myschema: </p>
<pre>ALTER AGGREGATE myavg(integer) SET SCHEMA myschema;</pre>
<h2>Compatibility</h2>
<p>There is no <code>ALTER AGGREGATE</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE AGGREGATE [<code><a href="/docs/linux/man/7-create_aggregate/">create_aggregate</a></code>(7)], DROP AGGREGATE [<code><a href="/docs/linux/man/7-drop_aggregate/">drop_aggregate</a></code>(7)] </p>
