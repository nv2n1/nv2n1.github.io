---
title: "bson_destroy_with_steal(3)"
name: "bson_destroy_with_steal"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_destroy_with_steal/"
description: "bson_destroy_with_steal() – The bson_destroy_with_steal() function shall destroy a bson_t structure but return the underlying buffer instead of freeing it. If steal is false, this is equivalent to ..."
---

<h2>NAME</h2>
<p> bson_destroy_with_steal() &#8211; The bson_destroy_with_steal() function shall destroy a bson_t structure but return the underlying buffer instead of freeing it. If steal is false, this is equivalent to calling bson_destroy(). It is a programming error to call this function on a bson_t that is not a top-level bson_t, shuch as those initialized with bson_append_document_begin(), bson_append_array_begin(), and bson_writer_begin().</p>
<h2>SYNOPSIS</h2>
<pre>
uint8_t *
bson_destroy_with_steal (bson_t   *bson,
                         bool      steal,
                         uint32_t *length);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>steal</code></p>
<dd> A bool indicating if the underlying buffer should be stolen.</dl>
<dl>
<dt><code>length</code></p>
<dd> A location for storing the resulting buffer length.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_destroy_with_steal/">bson_destroy_with_steal</a>(3)</code> function shall destroy a <code>bson_t</code> structure but return the underlying buffer instead of freeing it. If steal is false, this is equivalent to calling bson_destroy(). It is a programming error to call this function on a <code>bson_t</code> that is not a top-level <code>bson_t</code> , shuch as those initialized with <code><a href="/docs/linux/man/3-bson_append_document_begin/">bson_append_document_begin</a>(3)</code> , <code><a href="/docs/linux/man/3-bson_append_array_begin/">bson_append_array_begin</a>(3)</code> , and <code><a href="/docs/linux/man/3-bson_writer_begin/">bson_writer_begin</a>(3)</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> <code><a href="/docs/linux/man/3-bson_destroy_with_steal/">bson_destroy_with_steal</a>(3)</code> shall return a buffer containing the contents of the <code>bson_t</code> if <code>steal</code> is non-zero. This should be freed with <code><a href="/docs/linux/man/3-bson_free/">bson_free</a>(3)</code> when no longer in use. <code>length</code> will be set to the length of the bson document if non-NULL. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
