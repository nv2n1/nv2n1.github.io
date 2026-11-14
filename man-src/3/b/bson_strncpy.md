---
title: "bson_strncpy(3)"
name: "bson_strncpy"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_strncpy/"
description: "bson_strncpy() – Copies up to size bytes from src into dst. dst must be at least size bytes in size. A trailing will be set."
---

<h2>NAME</h2>
<p> bson_strncpy() &#8211; Copies up to size bytes from src into dst. dst must be at least size bytes in size. A trailing &nbsp;<wbr> will be set.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_strncpy(char *dst,
                  const char *src,
                  size_t size);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>dst</code></p>
<dd> The destination buffer.</dl>
<dl>
<dt><code>src</code></p>
<dd> The src buffer.</dl>
<dl>
<dt><code>size</code></p>
<dd> The number of bytes to copy into dst, which must be at least that size.</dl>
<h2>DESCRIPTION</h2>
<p> Copies up to <code>size</code> bytes from <code>src</code> into <code>dst</code> \&amp;. <code>dst</code> must be at least <code>size</code> bytes in size. A trailing <code>
