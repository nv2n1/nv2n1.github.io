---
title: "bson_uint32_to_string(3)"
name: "bson_uint32_to_string"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_uint32_to_string/"
description: "bson_uint32_to_string() – Converts value to a string."
---

<h2>NAME</h2>
<p> bson_uint32_to_string() &#8211; Converts value to a string.</p>
<h2>SYNOPSIS</h2>
<pre><code>
size_t
bson_uint32_to_string(uint32_t value,
                      const char **strptr,
                      char *str,
                      size_t size);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>value</code></p>
<dd> A uint32_t.</dl>
<dl>
<dt><code>strptr</code></p>
<dd> A location for the resulting string pointer.</dl>
<dl>
<dt><code>str</code></p>
<dd> A location to buffer the string.</dl>
<dl>
<dt><code>size</code></p>
<dd> A size_t containing the size of <code>str</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Converts <code>value</code> to a string. </p>
<p> If <code>value</code> is from 0 to 999, it will use a constant string in the data section of the library. </p>
<p> If not, a string will be formatted using <code>str</code> and <code><a href="/docs/linux/man/3-snprintf/">snprintf</a>(3)</code> \&amp;. </p>
<p> <code>strptr</code> will always be set. It will either point to <code>str</code> or a constant string. You will want to use this as your key. </p>
<h2>RETURNS</h2>
<p> The number of bytes in the resulting string. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
