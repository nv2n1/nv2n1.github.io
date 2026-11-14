---
title: "bson_json_data_reader_new(3)"
name: "bson_json_data_reader_new"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_json_data_reader_new/"
description: "bson_json_data_reader_new() – Creates a new streaming JSON reader that will convert JSON documents to BSON."
---

<h2>NAME</h2>
<p> bson_json_data_reader_new() &#8211; Creates a new streaming JSON reader that will convert JSON documents to BSON.</p>
<h2>SYNOPSIS</h2>
<pre>
bson_json_reader_t *
bson_json_data_reader_new (bool   allow_multiple,
                           size_t size);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>allow_multiple</code></p>
<dd> A boolean denoting if more than one document may be allowed in the stream.</dl>
<dl>
<dt><code>size</code></p>
<dd> A requested buffer size.</dl>
<h2>DESCRIPTION</h2>
<p> Creates a new streaming JSON reader that will convert JSON documents to BSON. </p>
<h2>RETURNS</h2>
<p> A newly allocated bson_json_reader_t that should be freed with bson_json_reader_destroy(). </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
