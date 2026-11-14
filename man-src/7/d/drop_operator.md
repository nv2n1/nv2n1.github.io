---
title: "drop_operator(7)"
name: "drop_operator"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_operator/"
description: "DROP OPERATOR – remove an operator"
---

<p>DROP OPERATOR &#8211; remove an operator </p>
<h2>Synopsis</h2>
<pre>DROP OPERATOR [ IF EXISTS ] <i>name</i> ( { <i>lefttype</i> | NONE } , { <i>righttype</i> | NONE } ) [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP OPERATOR</code> drops an existing operator from the database system. To execute this command you must be the owner of the operator.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the operator does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing operator.</p>
<dt><i>lefttype</i></p>
<dd>The data type of the operator&#8217;s left operand; write NONE if the operator has no left operand.</p>
<dt><i>righttype</i></p>
<dd>The data type of the operator&#8217;s right operand; write NONE if the operator has no right operand.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the operator.</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the operator if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>Remove the power operator a^b for type <code>integer</code>: </p>
<pre>DROP OPERATOR ^ (integer, integer);</pre>
<p>Remove the left unary bitwise complement operator ~b for type <code>bit</code>: </p>
<pre>DROP OPERATOR ~ (none, bit);</pre>
<p>Remove the right unary factorial operator x! for type <code>bigint</code>: </p>
<pre>DROP OPERATOR ! (bigint, none);</pre>
<h2>Compatibility</h2>
<p>There is no <code>DROP OPERATOR</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE OPERATOR [<code><a href="/docs/linux/man/7-create_operator/">create_operator</a></code>(7)], ALTER OPERATOR [<code><a href="/docs/linux/man/7-alter_operator/">alter_operator</a></code>(7)] </p>
