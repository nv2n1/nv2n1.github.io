---
title: "bson_validate(3)"
name: "bson_validate"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_validate/"
description: "bson_validate() – Validates a BSON document by walking through the document and inspecting the fields for valid content."
---

<h2>NAME</h2>
<p> bson_validate() &#8211; Validates a BSON document by walking through the document and inspecting the fields for valid content.</p>
<h2>SYNOPSIS</h2>
<pre><code>
typedef enum {
    BSON_VALIDATE_NONE = 0,
    BSON_VALIDATE_UTF8 = (1 &lt;&lt; 0),
    BSON_VALIDATE_DOLLAR_KEYS = (1 &lt;&lt; 1),
    BSON_VALIDATE_DOT_KEYS = (1 &lt;&lt; 2),
    BSON_VALIDATE_UTF8_ALLOW_NULL = (1 &lt;&lt; 3),
} bson_validate_flags_t;
bool bson_validate(const bson_t *bson,
                   bson_validate_flags_t flags,
                   size_t *offset);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>flags</code></p>
<dd> A bitwise-or of all desired <code>bson_validate_flags_t</code> \&amp;.</dl>
<dl>
<dt><code>offset</code></p>
<dd> A location for the offset within <code>bson</code> where the error ocurred.</dl>
<h2>DESCRIPTION</h2>
<p> Validates a BSON document by walking through the document and inspecting the fields for valid content. </p>
<p> You can modify how the validation occurs through the use of the <code>flags</code> parameter. A description of their effect is below. </p>
<dl>
<dt>\[bu]</p>
<dd> <code>BSON_VALIDATE_UTF8</code> will request that all UTF-8 strings are checked to contain valid UTF-8 sequences. This is expensive and disabled by default.</p>
<dt>\[bu]</p>
<dd> <code>BSON_VALIDATE_UTF8_ALLOW_NULL</code> will specify that UTF-8 strings are allowed to have embedded NULL bytes. Many UTF-8 implementations use a 2-byte squence for embedded NULLs so that they work with stanard libc functions. Libbson expects this by default.</p>
<dt>\[bu]</p>
<dd> <code>BSON_VALIDATE_DOLLAR_KEYS</code> will request that all key names are checked to ensure they do not start with the ASCII dollar character ( <code>$</code> ).</p>
<dt>\[bu]</p>
<dd> <code>BSON_VALIDATE_DOT_KEYS</code> will request that all key names are checked to ensure they do not contain an ASCII dot ( <code>.</code> ) character. </p>
</dl>
<h2>RETURNS</h2>
<p> Returns true if <code>bson</code> is valid; otherwise false and <code>offset</code> is set to the byte offset where the error was detected. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
