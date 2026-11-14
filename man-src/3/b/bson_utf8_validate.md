---
title: "bson_utf8_validate(3)"
name: "bson_utf8_validate"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_utf8_validate/"
description: "bson_utf8_validate() – Validates that the content within utf8 is valid UTF-8. If allow_null is true, then embedded NULL bytes are allowed ( )."
---

<h2>NAME</h2>
<p> bson_utf8_validate() &#8211; Validates that the content within utf8 is valid UTF-8. If allow_null is true, then embedded NULL bytes are allowed (&nbsp;<wbr>).</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_utf8_validate(const char *utf8,
                        size_t utf8_len,
                        bool allow_null);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>utf8</code></p>
<dd> A string to verify.</dl>
<dl>
<dt><code>utf8_len</code></p>
<dd> The length of <code>utf8</code> in bytes.</dl>
<dl>
<dt><code>allow_null</code></p>
<dd> A bool indicating that embedded <code>
