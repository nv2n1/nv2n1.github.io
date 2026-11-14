---
title: "strlcpy(9)"
name: "strlcpy"
section: "9"
letter: "s"
url: "/docs/linux/man/9-strlcpy/"
description: "strlcpy – Copy a C-string into a sized buffer"
---

<p>strlcpy &#8211; Copy a C-string into a sized buffer</p>
<h2>Synopsis</h2>
<pre><code>size_t strlcpy(char *dest, const char *src, size_t size);</code></pre>
<h2>Arguments</h2>
<p><i>dest</i></p>
<dl>
<dd>
<dd>Where to copy the string to</dl>
<p> <i>src</i></p>
<dl>
<dd>Where to copy the string from</dl>
<p> <i>size</i></p>
<dl>
<dd>size of destination buffer</dl>
<h2>Description</h2>
<p>Compatible with *BSD: the result is always a valid NUL-terminated string that fits in the buffer (unless, of course, the buffer size is zero). It does not pad out the result like <code>strncpy</code> does.</p>
<h2>Copyright</h2>
