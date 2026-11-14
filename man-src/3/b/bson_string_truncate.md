---
title: "bson_string_truncate(3)"
name: "bson_string_truncate"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_string_truncate/"
description: "bson_string_truncate() – Truncates the string so that it is len bytes in length. This must be smaller or equal to the current length of the string."
---

<h2>NAME</h2>
<p> bson_string_truncate() &#8211; Truncates the string so that it is len bytes in length. This must be smaller or equal to the current length of the string.</p>
<h2>SYNOPSIS</h2>
<pre>
void
bson_string_truncate (bson_string_t *string,
                      uint32_t       len);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>string</code></p>
<dd> A <code>bson_string_t</code> \&amp;.</dl>
<dl>
<dt><code>len</code></p>
<dd> The new length of the string, excluding the trailing <code>
