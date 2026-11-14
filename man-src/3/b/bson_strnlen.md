---
title: "bson_strnlen(3)"
name: "bson_strnlen"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_strnlen/"
description: "bson_strnlen() – A portable version of strnlen()."
---

<h2>NAME</h2>
<p> bson_strnlen() &#8211; A portable version of strnlen().</p>
<h2>SYNOPSIS</h2>
<pre><code>
size_t
bson_strnlen(const char *s,
             size_t maxlen);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>s</code></p>
<dd> A string.</dl>
<dl>
<dt><code>maxlen</code></p>
<dd> The maximum size of string to check.</dl>
<h2>DESCRIPTION</h2>
<p> A portable version of <code><a href="/docs/linux/man/3-strnlen/">strnlen</a>(3)</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> The length of <code>s</code> in bytes or <code>maxlen</code> if no <code>
