---
title: "bson_json_reader_new_from_file(3)"
name: "bson_json_reader_new_from_file"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_json_reader_new_from_file/"
description: "bson_json_reader_new_from_file() – Creates a new bson_json_reader_t using the underlying file found at filename."
---

<h2>NAME</h2>
<p> bson_json_reader_new_from_file() &#8211; Creates a new bson_json_reader_t using the underlying file found at filename.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bson_json_reader_t *
bson_json_reader_new_from_file(const char *filename,
                               bson_error_t *error);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>filename</code></p>
<dd> A file-name in the system file-name encoding.</dl>
<dl>
<dt><code>error</code></p>
<dd> A <code>bson_error_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Creates a new bson_json_reader_t using the underlying file found at <code>filename</code> \&amp;. </p>
<h2>ERRORS</h2>
<p> Errors are propagated via <code>error</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> A newly allocated bson_json_reader_t if successful, otherwise NULL and error is set. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
