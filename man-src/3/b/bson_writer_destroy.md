---
title: "bson_writer_destroy(3)"
name: "bson_writer_destroy"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_writer_destroy/"
description: "bson_writer_destroy() – Cleanup after writer and release any allocated memory. Note that the buffer supplied to bson_writer_new() is NOT freed from this method. The caller is responsible for that."
---

<h2>NAME</h2>
<p> bson_writer_destroy() &#8211; Cleanup after writer and release any allocated memory. Note that the buffer supplied to bson_writer_new() is NOT freed from this method. The caller is responsible for that.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_writer_destroy(bson_writer_t *writer);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>writer</code></p>
<dd> A <code>bson_writer_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Cleanup after <code>writer</code> and release any allocated memory. Note that the buffer supplied to <code><a href="/docs/linux/man/3-bson_writer_new/">bson_writer_new</a>(3)</code> is <code>NOT</code> freed from this method. The caller is responsible for that. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
