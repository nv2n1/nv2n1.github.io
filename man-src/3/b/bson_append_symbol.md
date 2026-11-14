---
title: "bson_append_symbol(3)"
name: "bson_append_symbol"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_symbol/"
description: "bson_append_symbol() – Appends a new field to bson of type BSON_TYPE_SYMBOL. This BSON type is deprecated and should not be used in new code."
---

<h2>NAME</h2>
<p> bson_append_symbol() &#8211; Appends a new field to bson of type BSON_TYPE_SYMBOL. This BSON type is deprecated and should not be used in new code.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_append_symbol(bson_t *bson,
                        const char *key,
                        int key_length,
                        const char *value,
                        int length);
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
<dt><code>value</code></p>
<dd> The symbol.</dl>
<dl>
<dt><code>length</code></p>
<dd> A length of <code>symbol</code> in bytes, or -1 to determine the length with <code><a href="/docs/linux/man/3-strlen/">strlen</a>(3)</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Appends a new field to <code>bson</code> of type BSON_TYPE_SYMBOL. This BSON type is deprecated and should not be used in new code. </p>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
