---
title: "bson_writer_begin(3)"
name: "bson_writer_begin"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_writer_begin/"
description: "bson_writer_begin() – Begins writing a new document. The caller may use the bson structure to write out a new BSON document. When completed, the caller must call either bson_writer_end() or bson_wr..."
---

<h2>NAME</h2>
<p> bson_writer_begin() &#8211; Begins writing a new document. The caller may use the bson structure to write out a new BSON document. When completed, the caller must call either bson_writer_end() or bson_writer_rollback().</p>
<h2>SYNOPSIS</h2>
<pre>
bool
bson_writer_begin (bson_writer_t *writer,
                   bson_t       **bson);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>writer</code></p>
<dd> A <code>bson_writer_t</code> \&amp;.</dl>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Begins writing a new document. The caller may use the bson structure to write out a new BSON document. When completed, the caller must call either <code><a href="/docs/linux/man/3-bson_writer_end/">bson_writer_end</a>(3)</code> or <code><a href="/docs/linux/man/3-bson_writer_rollback/">bson_writer_rollback</a>(3)</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> true if there was space in the underlying buffers to begin the document. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
