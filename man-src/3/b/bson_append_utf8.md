---
title: "bson_append_utf8(3)"
name: "bson_append_utf8"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_utf8/"
description: "bson_append_utf8() – The bson_append_utf8() function shall append a UTF-8 encoded string to bson."
---

<h2>NAME</h2>
<p> bson_append_utf8() &#8211; The bson_append_utf8() function shall append a UTF-8 encoded string to bson.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_append_utf8(bson_t *bson,
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
<dd> A UTF-8 encoded string.</dl>
<dl>
<dt><code>length</code></p>
<dd> The number of bytes in <code>value</code> excluding the trailing <code>
