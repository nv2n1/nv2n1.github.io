---
title: "bson_reader_new_from_file(3)"
name: "bson_reader_new_from_file"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_reader_new_from_file/"
description: "bson_reader_new_from_file() – Creates a new bson_reader_t using the file denoted by filename."
---

<h2>NAME</h2>
<p> bson_reader_new_from_file() &#8211; Creates a new bson_reader_t using the file denoted by filename.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bson_reader_t *
bson_reader_new_from_file(const char *path,
                          bson_error_t *error);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>path</code></p>
<dd> A filename in the host filename encoding.</dl>
<dl>
<dt><code>error</code></p>
<dd> A <code>bson_error_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Creates a new <code>bson_reader_t</code> using the file denoted by <code>filename</code> \&amp;. </p>
<h2>ERRORS</h2>
<p> Errors are propagated via the <code>error</code> parameter. </p>
<h2>RETURNS</h2>
<p> A newly allocated <code>bson_reader_t</code> on success, otherwise NULL and error is set. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
