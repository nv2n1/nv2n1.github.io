---
title: "drop_operator_family(7)"
name: "drop_operator_family"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_operator_family/"
description: "DROP OPERATOR FAMILY – remove an operator family"
---

<p>DROP OPERATOR FAMILY &#8211; remove an operator family </p>
<h2>Synopsis</h2>
<pre>DROP OPERATOR FAMILY [ IF EXISTS ] <i>name</i> USING <i>index_method</i> [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP OPERATOR FAMILY</code> drops an existing operator family. To execute this command you must be the owner of the operator family. </p>
<p> <code>DROP OPERATOR FAMILY</code> includes dropping any operator classes contained in the family, but it does not drop any of the operators or functions referenced by the family. If there are any indexes depending on operator classes within the family, you will need to specify CASCADE for the drop to complete.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the operator family does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing operator family.</p>
<dt><i>index_method</i></p>
<dd>The name of the index access method the operator family is for.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the operator family.</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the operator family if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>Remove the B-tree operator family float_ops: </p>
<pre>DROP OPERATOR FAMILY float_ops USING btree;</pre>
<p>This command will not succeed if there are any existing indexes that use operator classes within the family. Add CASCADE to drop such indexes along with the operator family.</p>
<h2>Compatibility</h2>
<p>There is no <code>DROP OPERATOR FAMILY</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>ALTER OPERATOR FAMILY [<code><a href="/docs/linux/man/7-alter_operator_family/">alter_operator_family</a></code>(7)], CREATE OPERATOR FAMILY [<code><a href="/docs/linux/man/7-create_operator_family/">create_operator_family</a></code>(7)], ALTER OPERATOR CLASS [<code><a href="/docs/linux/man/7-alter_operator_class/">alter_operator_class</a></code>(7)], CREATE OPERATOR CLASS [<code><a href="/docs/linux/man/7-create_operator_class/">create_operator_class</a></code>(7)], DROP OPERATOR CLASS [<code><a href="/docs/linux/man/7-drop_operator_class/">drop_operator_class</a></code>(7)] </p>
