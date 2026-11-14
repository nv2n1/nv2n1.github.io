---
title: "bson_reader_set_read_func(3)"
name: "bson_reader_set_read_func"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_reader_set_read_func/"
description: "bson_reader_set_read_func() – Sets the function to read more data from the underlying stream in a custom bson_reader_t."
---

<h2>NAME</h2>
<p> bson_reader_set_read_func() &#8211; Sets the function to read more data from the underlying stream in a custom bson_reader_t.</p>
<h2>SYNOPSIS</h2>
<pre>
void
bson_reader_set_read_func (bson_reader_t          *reader,
                           bson_reader_read_func_t func);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>reader</code></p>
<dd> A <code>bson_reader_t</code> \&amp;.</dl>
<dl>
<dt><code>func</code></p>
<dd> A <code>bson_reader_read_func_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Sets the function to read more data from the underlying stream in a custom bson_reader_t. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
