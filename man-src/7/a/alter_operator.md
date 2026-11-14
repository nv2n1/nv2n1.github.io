---
title: "alter_operator(7)"
name: "alter_operator"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_operator/"
description: "ALTER OPERATOR – change the definition of an operator"
---

<p>ALTER OPERATOR &#8211; change the definition of an operator </p>
<h2>Synopsis</h2>
<pre>ALTER OPERATOR <i>name</i> ( { <i>lefttype</i> | NONE } , { <i>righttype</i> | NONE } ) OWNER TO <i>newowner</i></pre>
<h2>Description</h2>
<p><code>ALTER OPERATOR</code> changes the definition of an operator. The only currently available functionality is to change the owner of the operator. </p>
<p> You must own the operator to use <code>ALTER OPERATOR</code>. To alter the owner, you must also be a direct or indirect member of the new owning role, and that role must have CREATE privilege on the operator&#8217;s schema. (These restrictions enforce that altering the owner doesn&#8217;t do anything you couldn&#8217;t do by dropping and recreating the operator. However, a superuser can alter ownership of any operator anyway.)</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing operator.</p>
<dt><i>lefttype</i></p>
<dd>The data type of the operator&#8217;s left operand; write NONE if the operator has no left operand.</p>
<dt><i>righttype</i></p>
<dd>The data type of the operator&#8217;s right operand; write NONE if the operator has no right operand.</p>
<dt><i>newowner</i></p>
<dd>The new owner of the operator.</dl>
<h2>Examples</h2>
<p>Change the owner of a custom operator a @@ b for type <code>text</code>: </p>
<pre>ALTER OPERATOR @@ (text, text) OWNER TO joe;</pre>
<h2>Compatibility</h2>
<p>There is no <code>ALTER OPERATOR</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE OPERATOR [<code><a href="/docs/linux/man/7-create_operator/">create_operator</a></code>(7)], DROP OPERATOR [<code><a href="/docs/linux/man/7-drop_operator/">drop_operator</a></code>(7)] </p>
