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
<dt><code>bson</code></dt>
<dd> A <code>bson_t</code> \&amp;.</dd></dl>
<dl>
<dt><code>key</code></dt>
<dd> An ASCII C string containing the name of the field.</dd></dl>
<dl>
<dt><code>key_length</code></dt>
<dd> The length of <code>key</code> in bytes, or -1 to determine the length with <code><a href="/docs/linux/man/3-strlen/">strlen</a>(3)</code> \&amp;.</dd></dl>
<dl>
<dt><code>value</code></dt>
<dd> A UTF-8 encoded string.</dd></dl>
<dl>
<dt><code>length</code></dt>
<dd> The number of bytes in <code>value</code> excluding the trailing <code>
</dd></dl>
</code>
