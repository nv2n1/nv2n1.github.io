---
title: "bson_utf8_next_char(3)"
name: "bson_utf8_next_char"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_utf8_next_char/"
description: "bson_utf8_next_char() – Advances within utf8 to the next UTF-8 character, which may be multiple bytes offset from utf8. A pointer to the next character is returned."
---
<h2>NAME</h2>
<p> bson_utf8_next_char() - Advances within utf8 to the next UTF-8 character, which may be multiple bytes offset from utf8. A pointer to the next character is returned.  </p>
<h2>SYNOPSIS</h2>
<pre><code>const char *
bson_utf8_next_char (const char *utf8);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>utf8</code></dt>
<dd> <p> A UTF-8 encoded string. </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p> Advances within <code>utf8</code> to the next UTF-8 character, which may be multiple bytes offset from <code>utf8</code> \&amp;. A pointer to the next character is returned. </p>
<p> It is invalid to call this function on a string whose current character is <code>\0</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> A pointer to the beginning of the next character in the UTF-8 encoded string. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
