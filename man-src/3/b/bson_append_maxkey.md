---
title: "bson_append_maxkey(3)"
name: "bson_append_maxkey"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_maxkey/"
description: "bson_append_maxkey() – The bson_append_maxkey() function shall append an element of type BSON_TYPE_MAXKEY to a bson document. This is primarily used in queries and unlikely to be used when storing ..."
---

<h2>NAME</h2>
<p> bson_append_maxkey() &#8211; The bson_append_maxkey() function shall append an element of type BSON_TYPE_MAXKEY to a bson document. This is primarily used in queries and unlikely to be used when storing a document to MongoDB.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_append_maxkey(bson_t *bson,
                        const char *key,
                        int key_length);
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
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_append_maxkey/">bson_append_maxkey</a>(3)</code> function shall append an element of type BSON_TYPE_MAXKEY to a bson document. This is primarily used in queries and unlikely to be used when storing a document to MongoDB. </p>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
