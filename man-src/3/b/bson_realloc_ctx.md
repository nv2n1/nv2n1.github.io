---
title: "bson_realloc_ctx(3)"
name: "bson_realloc_ctx"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_realloc_ctx/"
description: "bson_realloc_ctx() – This function is identical to bson_realloc() except it takes a context parameter. This is useful when working with pooled or specific memory allocators."
---

<h2>NAME</h2>
<p> bson_realloc_ctx() &#8211; This function is identical to bson_realloc() except it takes a context parameter. This is useful when working with pooled or specific memory allocators.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void *
bson_realloc_ctx(void *mem,
                 size_t num_bytes,
                 void *ctx);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>mem</code></p>
<dd> A memory region.</dl>
<dl>
<dt><code>num_bytes</code></p>
<dd> A size_t containing the requested size.</dl>
<dl>
<dt><code>ctx</code></p>
<dd> A consumer-specific pointer or <code>NULL</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> This function is identical to <code><a href="/docs/linux/man/3-bson_realloc/">bson_realloc</a>(3)</code> except it takes a context parameter. This is useful when working with pooled or specific memory allocators. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
