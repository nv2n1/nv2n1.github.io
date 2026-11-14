---
title: "alter_tablespace(7)"
name: "alter_tablespace"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_tablespace/"
description: "ALTER TABLESPACE – change the definition of a tablespace"
---

<p>ALTER TABLESPACE &#8211; change the definition of a tablespace </p>
<h2>Synopsis</h2>
<pre>ALTER TABLESPACE <i>name</i> RENAME TO <i>newname</i>
ALTER TABLESPACE <i>name</i> OWNER TO <i>newowner</i></pre>
<h2>Description</h2>
<p><code>ALTER TABLESPACE</code> changes the definition of a tablespace. </p>
<p> You must own the tablespace to use <code>ALTER TABLESPACE</code>. To alter the owner, you must also be a direct or indirect member of the new owning role. (Note that superusers have these privileges automatically.)</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of an existing tablespace.</p>
<dt><i>newname</i></p>
<dd>The new name of the tablespace. The new name cannot begin with pg_, as such names are reserved for system tablespaces.</p>
<dt><i>newowner</i></p>
<dd>The new owner of the tablespace.</dl>
<h2>Examples</h2>
<p>Rename tablespace index_space to fast_raid: </p>
<pre>ALTER TABLESPACE index_space RENAME TO fast_raid;</pre>
<p>Change the owner of tablespace index_space: </p>
<pre>ALTER TABLESPACE index_space OWNER TO mary;</pre>
<h2>Compatibility</h2>
<p>There is no <code>ALTER TABLESPACE</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE TABLESPACE [<code><a href="/docs/linux/man/7-create_tablespace/">create_tablespace</a></code>(7)], DROP TABLESPACE [<code><a href="/docs/linux/man/7-drop_tablespace/">drop_tablespace</a></code>(7)] </p>
