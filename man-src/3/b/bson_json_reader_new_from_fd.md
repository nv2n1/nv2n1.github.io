---
title: "bson_json_reader_new_from_fd(3)"
name: "bson_json_reader_new_from_fd"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_json_reader_new_from_fd/"
description: "bson_json_reader_new_from_fd() – Creates a new JSON to BSON converter that will be reading from the file-descriptor fd."
---

<h2>NAME</h2>
<p> bson_json_reader_new_from_fd() &#8211; Creates a new JSON to BSON converter that will be reading from the file-descriptor fd.</p>
<h2>SYNOPSIS</h2>
<pre>
bson_json_reader_t *
bson_json_reader_new_from_fd (int  fd,
                              bool close_on_destroy);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>fd</code></p>
<dd> An open file-descriptor.</dl>
<dl>
<dt><code>close_on_destroy</code></p>
<dd> Whether <code><a href="/docs/linux/man/3-close/">close</a>(3)</code> should be called on <code>fd</code> when the reader is destroyed.</dl>
<h2>DESCRIPTION</h2>
<p> Creates a new JSON to BSON converter that will be reading from the file-descriptor <code>fd</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> A newly allocated bson_json_reader_t that should be freed with bson_json_reader_destroy(). </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
