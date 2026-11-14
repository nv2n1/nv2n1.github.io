---
title: "bson_utf8_get_char(3)"
name: "bson_utf8_get_char"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_utf8_get_char/"
description: "bson_utf8_get_char() – Converts the current character in a UTF-8 sequence to a bson_unichar_t, the 32-bit representation of the multi-byte character."
---

<h2>NAME</h2>
<p> bson_utf8_get_char() &#8211; Converts the current character in a UTF-8 sequence to a bson_unichar_t, the 32-bit representation of the multi-byte character.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bson_unichar_t
bson_utf8_get_char(const char *utf8);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>utf8</code></p>
<dd> A UTF-8 encoded string.</dl>
<h2>DESCRIPTION</h2>
<p> Converts the current character in a UTF-8 sequence to a bson_unichar_t, the 32-bit representation of the multi-byte character. </p>
<h2>RETURNS</h2>
<p> A bson_unichar_t. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
