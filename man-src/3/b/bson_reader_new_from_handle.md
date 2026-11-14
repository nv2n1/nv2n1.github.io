---
title: "bson_reader_new_from_handle(3)"
name: "bson_reader_new_from_handle"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_reader_new_from_handle/"
description: "bson_reader_new_from_handle() – This function allows for a pluggable data stream for the reader. This can be used to read from sockets, files, memory, or other arbitrary sources."
---

<h2>NAME</h2>
<p> bson_reader_new_from_handle() &#8211; This function allows for a pluggable data stream for the reader. This can be used to read from sockets, files, memory, or other arbitrary sources.</p>
<h2>SYNOPSIS</h2>
<pre>
bson_reader_t *
bson_reader_new_from_handle (void                      *handle,
                             bson_reader_read_func_t    rf,
                             bson_reader_destroy_func_t df);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>handle</code></p>
<dd> A user-provided pointer or NULL.</dl>
<dl>
<dt><code>rf</code></p>
<dd> A <code>bson_reader_read_func_t</code> \&amp;.</dl>
<dl>
<dt><code>df</code></p>
<dd> A <code>bson_reader_destroy_func_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> This function allows for a pluggable data stream for the reader. This can be used to read from sockets, files, memory, or other arbitrary sources. </p>
<h2>RETURNS</h2>
<p> A newly allocated bson_reader_t if successful; otherwise NULL. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
