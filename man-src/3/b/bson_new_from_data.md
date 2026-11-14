---
title: "bson_new_from_data(3)"
name: "bson_new_from_data"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_new_from_data/"
description: "bson_new_from_data() – The bson_new_from_data() function shall create a new bson_t on the heap and copy the contents of data. This may be helpful when working with language bindings but is generall..."
---

<h2>NAME</h2>
<p> bson_new_from_data() &#8211; The bson_new_from_data() function shall create a new bson_t on the heap and copy the contents of data. This may be helpful when working with language bindings but is generally expected to be slower.</p>
<h2>SYNOPSIS</h2>
<pre>
bson_t *
bson_new_from_data (const uint8_t *data,
                    size_t         length);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>data</code></p>
<dd> A BSON encoded document buffer.</dl>
<dl>
<dt><code>length</code></p>
<dd> The length of <code>data</code> in bytes.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_new_from_data/">bson_new_from_data</a>(3)</code> function shall create a new <code>bson_t</code> on the heap and copy the contents of <code>data</code> \&amp;. This may be helpful when working with language bindings but is generally expected to be slower. </p>
<h2>RETURNS</h2>
<p> A newly allocated <code>bson_t</code> if successful, otherwise NULL. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
