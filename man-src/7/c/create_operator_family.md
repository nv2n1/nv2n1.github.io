---
title: "create_operator_family(7)"
name: "create_operator_family"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_operator_family/"
description: "CREATE OPERATOR FAMILY – define a new operator family"
---

<p>CREATE OPERATOR FAMILY &#8211; define a new operator family </p>
<h2>Synopsis</h2>
<pre>CREATE OPERATOR FAMILY <i>name</i> USING <i>index_method</i></pre>
<h2>Description</h2>
<p><code>CREATE OPERATOR FAMILY</code> creates a new operator family. An operator family defines a collection of related operator classes, and perhaps some additional operators and support functions that are compatible with these operator classes but not essential for the functioning of any individual index. (Operators and functions that are essential to indexes should be grouped within the relevant operator class, rather than being &#8220;loose&#8221; in the operator family. Typically, single-data-type operators are bound to operator classes, while cross-data-type operators can be loose in an operator family containing operator classes for both data types.) </p>
<p> The new operator family is initially empty. It should be populated by issuing subsequent <code>CREATE OPERATOR CLASS</code> commands to add contained operator classes, and optionally <code>ALTER OPERATOR FAMILY</code> commands to add &#8220;loose&#8221; operators and their corresponding support functions. </p>
<p> If a schema name is given then the operator family is created in the specified schema. Otherwise it is created in the current schema. Two operator families in the same schema can have the same name only if they are for different index methods. </p>
<p> The user who defines an operator family becomes its owner. Presently, the creating user must be a superuser. (This restriction is made because an erroneous operator family definition could confuse or even crash the server.) </p>
<p> Refer to in the documentation for further information.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of the operator family to be created. The name can be schema-qualified.</p>
<dt><i>index_method</i></p>
<dd>The name of the index method this operator family is for.</dl>
<h2>Compatibility</h2>
<p><code>CREATE OPERATOR FAMILY</code> is a PostgreSQL extension. There is no <code>CREATE OPERATOR FAMILY</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>ALTER OPERATOR FAMILY [<code><a href="/docs/linux/man/7-alter_operator_family/">alter_operator_family</a></code>(7)], DROP OPERATOR FAMILY [<code><a href="/docs/linux/man/7-drop_operator_family/">drop_operator_family</a></code>(7)], CREATE OPERATOR CLASS [<code><a href="/docs/linux/man/7-create_operator_class/">create_operator_class</a></code>(7)], ALTER OPERATOR CLASS [<code><a href="/docs/linux/man/7-alter_operator_class/">alter_operator_class</a></code>(7)], DROP OPERATOR CLASS [<code><a href="/docs/linux/man/7-drop_operator_class/">drop_operator_class</a></code>(7)] </p>
