---
title: "drop_operator_class(7)"
name: "drop_operator_class"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_operator_class/"
description: "DROP OPERATOR CLASS – remove an operator class"
---

<p>DROP OPERATOR CLASS &#8211; remove an operator class </p>
<h2>Synopsis</h2>
<pre>DROP OPERATOR CLASS [ IF EXISTS ] <i>name</i> USING <i>index_method</i> [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP OPERATOR CLASS</code> drops an existing operator class. To execute this command you must be the owner of the operator class. </p>
<p> <code>DROP OPERATOR CLASS</code> does not drop any of the operators or functions referenced by the class. If there are any indexes depending on the operator class, you will need to specify CASCADE for the drop to complete.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the operator class does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing operator class.</p>
<dt><i>index_method</i></p>
<dd>The name of the index access method the operator class is for.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the operator class.</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the operator class if any objects depend on it. This is the default.</dl>
<h2>Notes</h2>
<p><code>DROP OPERATOR CLASS</code> will not drop the operator family containing the class, even if there is nothing else left in the family (in particular, in the case where the family was implicitly created by <code>CREATE OPERATOR CLASS</code>). An empty operator family is harmless, but for the sake of tidiness you might wish to remove the family with <code>DROP OPERATOR FAMILY</code>; or perhaps better, use <code>DROP OPERATOR FAMILY</code> in the first place.</p>
<h2>Examples</h2>
<p>Remove the B-tree operator class widget_ops: </p>
<pre>DROP OPERATOR CLASS widget_ops USING btree;</pre>
<p>This command will not succeed if there are any existing indexes that use the operator class. Add CASCADE to drop such indexes along with the operator class.</p>
<h2>Compatibility</h2>
<p>There is no <code>DROP OPERATOR CLASS</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>ALTER OPERATOR CLASS [<code><a href="/docs/linux/man/7-alter_operator_class/">alter_operator_class</a></code>(7)], CREATE OPERATOR CLASS [<code><a href="/docs/linux/man/7-create_operator_class/">create_operator_class</a></code>(7)], DROP OPERATOR FAMILY [<code><a href="/docs/linux/man/7-drop_operator_family/">drop_operator_family</a></code>(7)] </p>
