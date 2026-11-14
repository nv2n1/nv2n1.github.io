---
title: "bson_utf8_escape_for_json(3)"
name: "bson_utf8_escape_for_json"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_utf8_escape_for_json/"
description: "bson_utf8_escape_for_json() – Escapes the string utf8 to be placed inside of a JSON string."
---

<h2>NAME</h2>
<p> bson_utf8_escape_for_json() &#8211; Escapes the string utf8 to be placed inside of a JSON string.</p>
<h2>SYNOPSIS</h2>
<pre><code>
char *
bson_utf8_escape_for_json(const char *utf8,
                          ssize_t utf8_len);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>utf8</code></p>
<dd> A UTF-8 encoded string.</dl>
<dl>
<dt><code>utf8_len</code></p>
<dd> The length of <code>utf8</code> in bytes or -1 if it is NULL terminated.</dl>
<h2>DESCRIPTION</h2>
<p> Escapes the string <code>utf8</code> to be placed inside of a JSON string. </p>
<h2>RETURNS</h2>
<p> A newly allocated string that should be freed with <code><a href="/docs/linux/man/3-bson_free/">bson_free</a>(3)</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
