---

title: "bson_writer_new(3)"
name: "bson_writer_new"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_writer_new/"
description: "bson_writer_new() – Creates a new instance of bson_writer_t using the buffer, length, offset, and _realloc()_ function supplied."
---

<p> bson_writer_new() &#8211; Creates a new instance of bson_writer_t using the buffer, length, offset, and _realloc()_ function supplied.</p>
<h2>SYNOPSIS</h2>
<pre>
bson_writer_t *
bson_writer_new (uint8_t         **buf,
                 size_t           *buflen,
                 size_t            offset,
                 bson_realloc_func realloc_func,
                 void             *realloc_func_ctx);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>buf</code></dt>
<dd> A uint8_t.</dd></dl>
<dl>
<dt><code>buflen</code></dt>
<dd> A size_t.</dd></dl>
<dl>
<dt><code>offset</code></dt>
<dd> A size_t.</dd></dl>
<dl>
<dt><code>realloc_func</code></dt>
<dd> A bson_realloc_func.</dd></dl>
<dl>
<dt><code>realloc_func_ctx</code></dt>
<dd> A bson_realloc_func.</dd></dl>
<h2>DESCRIPTION</h2>
<p> Creates a new instance of <code>bson_writer_t</code> using the <code>buffer</code> , <code>length</code> , <code>offset</code> , and _realloc()_ function supplied. </p>
<p> The caller is expected to clean up the structure when finished using <code><a href="/docs/linux/man/3-bson_writer_destroy/">bson_writer_destroy</a>(3)</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> A newly allocated bson_writer_t. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
