---
title: "bson_string_append_unichar(3)"
name: "bson_string_append_unichar"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_string_append_unichar/"
description: "bson_string_append_unichar() – Appends a unicode character to string. The character will be encoded into its multi-byte UTF-8 representation."
---

<h2>NAME</h2>
<p> bson_string_append_unichar() &#8211; Appends a unicode character to string. The character will be encoded into its multi-byte UTF-8 representation.</p>
<h2>SYNOPSIS</h2>
<pre>
void
bson_string_append_unichar (bson_string_t *string,
                            bson_unichar_t unichar);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>string</code></p>
<dd> A <code>bson_string_t</code> \&amp;.</dl>
<dl>
<dt><code>unichar</code></p>
<dd> A <code>bson_unichar_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Appends a unicode character to string. The character will be encoded into its multi-byte UTF-8 representation. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
