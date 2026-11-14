---
title: "bson_append_dbpointer(3)"
name: "bson_append_dbpointer"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_dbpointer/"
description: "bson_append_dbpointer() – The dbpointer field type is DEPRECATED and should only be used when interacting with legacy systems."
---

<h2>NAME</h2>
<p> bson_append_dbpointer() &#8211; The dbpointer field type is DEPRECATED and should only be used when interacting with legacy systems.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_append_dbpointer(bson_t *bson,
                           const char *key,
                           int key_length,
                           const char *collection,
                           const bson_oid_t *oid);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>key</code></p>
<dd> An ASCII C string containing the name of the field.</dl>
<dl>
<dt><code>key_length</code></p>
<dd> The length of <code>key</code> in bytes, or -1 to determine the length with <code><a href="/docs/linux/man/3-strlen/">strlen</a>(3)</code> \&amp;.</dl>
<dl>
<dt><code>collection</code></p>
<dd> The target collection name.</dl>
<dl>
<dt><code>oid</code></p>
<dd> The target document identifer.</dl>
<h2>DESCRIPTION</h2>
<p> <code>NOTE</code></p>
<dl>
<dt>
<dd> The dbpointer field type is <code>DEPRECATED</code> and should only be used when interacting with legacy systems.</dl>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
