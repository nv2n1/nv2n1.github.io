---
title: "bson_reader_destroy_func_t(3)"
name: "bson_reader_destroy_func_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_reader_destroy_func_t/"
description: "bson_reader_destroy_func_t – An optional callback function that will be called when a bson_reader_t created with bson_reader_new_from_handle is destroyed with bson_reader_destroy()."
---

<h2>NAME</h2>
<p> bson_reader_destroy_func_t &#8211; An optional callback function that will be called when a bson_reader_t created with bson_reader_new_from_handle is destroyed with bson_reader_destroy().</p>
<h2>SYNOPSIS</h2>
<pre><code>
typedef void (*bson_reader_destroy_func_t)(void *handle);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>handle</code></p>
<dd> The opaque handle provided to <code>bson_reader_new_from_handle</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> An optional callback function that will be called when a <code>bson_reader_t</code> created with <code>bson_reader_new_from_handle</code> is destroyed with <code><a href="/docs/linux/man/3-bson_reader_destroy/">bson_reader_destroy</a>(3)</code> \&amp;. </p>
<p> The handle used when creating the reader is passed to this callback. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
