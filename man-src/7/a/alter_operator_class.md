---
title: "alter_operator_class(7)"
name: "alter_operator_class"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_operator_class/"
description: "ALTER OPERATOR CLASS – change the definition of an operator class"
---

<p>ALTER OPERATOR CLASS &#8211; change the definition of an operator class </p>
<h2>Synopsis</h2>
<pre>ALTER OPERATOR CLASS <i>name</i> USING <i>index_method</i> RENAME TO <i>newname</i>
ALTER OPERATOR CLASS <i>name</i> USING <i>index_method</i> OWNER TO <i>newowner</i></pre>
<h2>Description</h2>
<p><code>ALTER OPERATOR CLASS</code> changes the definition of an operator class. </p>
<p> You must own the operator class to use <code>ALTER OPERATOR CLASS</code>. To alter the owner, you must also be a direct or indirect member of the new owning role, and that role must have CREATE privilege on the operator class&#8217;s schema. (These restrictions enforce that altering the owner doesn&#8217;t do anything you couldn&#8217;t do by dropping and recreating the operator class. However, a superuser can alter ownership of any operator class anyway.)</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing operator class.</p>
<dt><i>index_method</i></p>
<dd>The name of the index method this operator class is for.</p>
<dt><i>newname</i></p>
<dd>The new name of the operator class.</p>
<dt><i>newowner</i></p>
<dd>The new owner of the operator class.</dl>
<h2>Compatibility</h2>
<p>There is no <code>ALTER OPERATOR CLASS</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE OPERATOR CLASS [<code><a href="/docs/linux/man/7-create_operator_class/">create_operator_class</a></code>(7)], DROP OPERATOR CLASS [<code><a href="/docs/linux/man/7-drop_operator_class/">drop_operator_class</a></code>(7)], ALTER OPERATOR FAMILY [<code><a href="/docs/linux/man/7-alter_operator_family/">alter_operator_family</a></code>(7)] </p>
