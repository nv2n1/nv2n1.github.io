---
title: "bson_utf8_next_char(3)"
name: "bson_utf8_next_char"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_utf8_next_char/"
description: "bson_utf8_next_char() – Advances within utf8 to the next UTF-8 character, which may be multiple bytes offset from utf8. A pointer to the next character is returned."
---

<h2>NAME</h2>
<p> bson_utf8_next_char() &#8211; Advances within utf8 to the next UTF-8 character, which may be multiple bytes offset from utf8. A pointer to the next character is returned.</p>
<h2>SYNOPSIS</h2>
<pre><code>
const char *
bson_utf8_next_char(const char *utf8);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>utf8</code></p>
<dd> A UTF-8 encoded string.</dl>
<h2>DESCRIPTION</h2>
<p> Advances within <code>utf8</code> to the next UTF-8 character, which may be multiple bytes offset from <code>utf8</code> \&amp;. A pointer to the next character is returned. </p>
<p> It is invalid to call this function on a string whose current character is <code>
