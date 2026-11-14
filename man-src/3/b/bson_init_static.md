---
title: "bson_init_static(3)"
name: "bson_init_static"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_init_static/"
description: "bson_init_static() – The bson_init_static() function shall shall initialize a read-only bson_t on the stack using the data provided. No copies of the data will be made and therefore must remain val..."
---

<h2>NAME</h2>
<p> bson_init_static() &#8211; The bson_init_static() function shall shall initialize a read-only bson_t on the stack using the data provided. No copies of the data will be made and therefore must remain valid for the lifetime of the bson_t.</p>
<h2>SYNOPSIS</h2>
<pre>
bool
bson_init_static (bson_t        *b,
                  const uint8_t *data,
                  size_t         length);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>b</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>data</code></p>
<dd> A buffer to initialize with.</dl>
<dl>
<dt><code>length</code></p>
<dd> The length of <code>data</code> in bytes.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_init_static/">bson_init_static</a>(3)</code> function shall shall initialize a read-only <code>bson_t</code> on the stack using the data provided. No copies of the data will be made and therefore must remain valid for the lifetime of the <code>bson_t</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> <code><a href="/docs/linux/man/3-bson_init_static/">bson_init_static</a>(3)</code> will return <code>true</code> if the <code>bson_t</code> was successfully initialized. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
