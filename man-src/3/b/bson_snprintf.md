---
title: "bson_snprintf(3)"
name: "bson_snprintf"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_snprintf/"
description: "bson_snprintf() – This is a portable wrapper around snprintf(). It also enforces a trailing in the resulting string."
---

<h2>NAME</h2>
<p> bson_snprintf() &#8211; This is a portable wrapper around snprintf(). It also enforces a trailing &nbsp;<wbr> in the resulting string.</p>
<h2>SYNOPSIS</h2>
<pre><code>
int bson_snprintf(char *str,
                  size_t size,
                  const char *format,
                  ...) BSON_GNUC_PRINTF(3, 4);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>str</code></p>
<dd> The destination buffer.</dl>
<dl>
<dt><code>size</code></p>
<dd> The size of <code>str</code> \&amp;.</dl>
<dl>
<dt><code>format</code></p>
<dd> A printf style format string.</dl>
<h2>DESCRIPTION</h2>
<p> This is a portable wrapper around <code><a href="/docs/linux/man/3-snprintf/">snprintf</a>(3)</code> \&amp;. It also enforces a trailing <code>
