---

title: "bson_realloc_func(3)"
name: "bson_realloc_func"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_realloc_func/"
description: "bson_realloc_func – This is a prototype for pluggable realloc functions used through the Libbson library. If you wish to use a custom allocator this is one way to do it. Additionally, bson_realloc_..."
---

<p> bson_realloc_func &#8211; This is a prototype for pluggable realloc functions used through the Libbson library. If you wish to use a custom allocator this is one way to do it. Additionally, bson_realloc_ctx() is a default implementation of this prototype.</p>
<h2>SYNOPSIS</h2>
<pre><code>
typedef void *(*bson_realloc_func)(void *mem,
                                   size_t num_bytes,
                                   void *ctx);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>mem</code></dt>
<dd> A memory region.</dd></dl>
<dl>
<dt><code>num_bytes</code></dt>
<dd> A size_t containing the requested size.</dd></dl>
<dl>
<dt><code>ctx</code></dt>
<dd> A consumer-specific pointer or <code>NULL</code> \&amp;.</dd></dl>
<h2>DESCRIPTION</h2>
<p> This is a prototype for pluggable realloc functions used through the Libbson library. If you wish to use a custom allocator this is one way to do it. Additionally, <code><a href="/docs/linux/man/3-bson_realloc_ctx/">bson_realloc_ctx</a>(3)</code> is a default implementation of this prototype. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
