---
title: "bson_json_reader_new(3)"
name: "bson_json_reader_new"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_json_reader_new/"
description: "bson_json_reader_new() – Creates a new bson_json_reader_t that can read from an arbitrary data source in a streaming fashion."
---

<h2>NAME</h2>
<p> bson_json_reader_new() &#8211; Creates a new bson_json_reader_t that can read from an arbitrary data source in a streaming fashion.</p>
<h2>SYNOPSIS</h2>
<pre>
bson_json_reader_t *
bson_json_reader_new (void                *data,
                      bson_json_reader_cb  cb,
                      bson_json_destroy_cb dcb,
                      bool                 allow_multiple,
                      size_t               buf_size);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>data</code></p>
<dd> A user-defined pointer.</dl>
<dl>
<dt><code>cb</code></p>
<dd> A bson_json_reader_cb.</dl>
<dl>
<dt><code>dcb</code></p>
<dd> A bson_json_destroy_cb.</dl>
<dl>
<dt><code>allow_multiple</code></p>
<dd> A bool indicating if more than one document is allowed in the stream.</dl>
<dl>
<dt><code>buf_size</code></p>
<dd> A size_t containing the requested internal buffer size.</dl>
<h2>DESCRIPTION</h2>
<p> Creates a new bson_json_reader_t that can read from an arbitrary data source in a streaming fashion. </p>
<h2>RETURNS</h2>
<p> A newly allocated bson_json_reader_t that should be freed with bson_json_reader_destroy(). </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
