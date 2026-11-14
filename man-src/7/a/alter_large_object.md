---
title: "alter_large_object(7)"
name: "alter_large_object"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_large_object/"
description: "ALTER_LARGE_OBJECT – change the definition of a large object"
---

<p>ALTER_LARGE_OBJECT &#8211; change the definition of a large object</p>
<h2>Synopsis</h2>
<pre>ALTER LARGE OBJECT <i>large_object_oid</i> OWNER TO <i>new_owner</i></pre>
<h2>Description</h2>
<p><code>ALTER LARGE OBJECT</code> changes the definition of a large object. The only functionality is to assign a new owner. You must be superuser or owner of the large object to use <code>ALTER LARGE OBJECT</code>.</p>
<h2>Parameters</h2>
<p><i>large_object_oid</i></p>
<dl>
<dd>OID of the large object to be altered</dl>
<p> <i>new_owner</i></p>
<dl>
<dd>The new owner of the large object</dl>
<h2>Compatibility</h2>
<p>There is no <code>ALTER LARGE OBJECT</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>Chapter 32, Large Objects, in the documentation </p>
