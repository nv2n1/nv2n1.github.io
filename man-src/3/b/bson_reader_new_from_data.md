---
title: "bson_reader_new_from_data(3)"
name: "bson_reader_new_from_data"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_reader_new_from_data/"
description: "bson_reader_new_from_data() – The bson_reader_new_from_data() function shall create a new bson_reader_t using the buffer supplied. data is not copied and MUST be valid for the lifetime of the resul..."
---

<h2>NAME</h2>
<p> bson_reader_new_from_data() &#8211; The bson_reader_new_from_data() function shall create a new bson_reader_t using the buffer supplied. data is not copied and MUST be valid for the lifetime of the resulting bson_reader_t.</p>
<h2>SYNOPSIS</h2>
<pre>
bson_reader_t *
bson_reader_new_from_data (const uint8_t *data,
                           size_t         length);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>data</code></p>
<dd> A uint8_t.</dl>
<dl>
<dt><code>length</code></p>
<dd> A size_t.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_reader_new_from_data/">bson_reader_new_from_data</a>(3)</code> function shall create a new <code>bson_reader_t</code> using the buffer supplied. <code>data</code> is not copied and <code>MUST</code> be valid for the lifetime of the resulting <code>bson_reader_t</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> A newly allocated <code>bson_reader_t</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
