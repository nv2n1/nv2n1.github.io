---
title: "bson_writer_rollback(3)"
name: "bson_writer_rollback"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_writer_rollback/"
description: "bson_writer_rollback() – Abort the appending of the current bson_t to the memory region managed by writer. This is useful if you detected that you went past a particular memory limit. For example, ..."
---

<h2>NAME</h2>
<p> bson_writer_rollback() &#8211; Abort the appending of the current bson_t to the memory region managed by writer. This is useful if you detected that you went past a particular memory limit. For example, MongoDB has 48MB message limits.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_writer_rollback(bson_writer_t *writer);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>writer</code></p>
<dd> A <code>bson_writer_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Abort the appending of the current bson_t to the memory region managed by <code>writer</code> \&amp;. This is useful if you detected that you went past a particular memory limit. For example, MongoDB has 48MB message limits. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
