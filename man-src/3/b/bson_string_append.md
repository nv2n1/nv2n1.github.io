---
title: "bson_string_append(3)"
name: "bson_string_append"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_string_append/"
description: "bson_string_append() – Appends the ASCII or UTF-8 encoded string str to string. This is not suitable for embedding NULLs in strings."
---

<h2>NAME</h2>
<p> bson_string_append() &#8211; Appends the ASCII or UTF-8 encoded string str to string. This is not suitable for embedding NULLs in strings.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_string_append(bson_string_t *string,
                        const char *str);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>string</code></p>
<dd> A <code>bson_string_t</code> \&amp;.</dl>
<dl>
<dt><code>str</code></p>
<dd> A string.</dl>
<h2>DESCRIPTION</h2>
<p> Appends the ASCII or UTF-8 encoded string <code>str</code> to <code>string</code> \&amp;. This is not suitable for embedding NULLs in strings. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
