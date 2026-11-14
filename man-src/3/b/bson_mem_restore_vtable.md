---
title: "bson_mem_restore_vtable(3)"
name: "bson_mem_restore_vtable"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_mem_restore_vtable/"
description: "bson_mem_restore_vtable() – This function shall restore the default memory allocator to be used by Libbson."
---

<h2>NAME</h2>
<p> bson_mem_restore_vtable() &#8211; This function shall restore the default memory allocator to be used by Libbson.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_mem_restore_vtable(void);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This function shall restore the default memory allocator to be used by Libbson. </p>
<p> <code>NOTE</code></p>
<dl>
<dt>
<dd> This function <code>MUST</code> be called at the end of the process. Failure to do so will result in memory being freed by the wrong allocator.</dl>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
