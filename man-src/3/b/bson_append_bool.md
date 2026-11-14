---
title: "bson_append_bool(3)"
name: "bson_append_bool"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_bool/"
description: "bson_append_bool() – The bson_append_bool() function shall append a new element to bson containing the boolean provided."
---

<h2>NAME</h2>
<p> bson_append_bool() &#8211; The bson_append_bool() function shall append a new element to bson containing the boolean provided.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_append_bool(bson_t *bson,
                      const char *key,
                      int key_length,
                      bool value);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>key</code></p>
<dd> The name of the field.</dl>
<dl>
<dt><code>key_length</code></p>
<dd> The length of <code>key</code> or -1 to use strlen().</dl>
<dl>
<dt><code>value</code></p>
<dd> true or false.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_append_bool/">bson_append_bool</a>(3)</code> function shall append a new element to <code>bson</code> containing the boolean provided. </p>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
