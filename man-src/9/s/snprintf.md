---
title: "snprintf(9)"
name: "snprintf"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snprintf/"
description: "snprintf – Format a string and place it in a buffer"
---

<p>snprintf &#8211; Format a string and place it in a buffer</p>
<h2>Synopsis</h2>
<pre><code>int snprintf(char *buf, size_t size, const char *fmt, ...);</code></pre>
<h2>Arguments</h2>
<p><i>buf</i></p>
<dl>
<dd>
<dd>The buffer to place the result into</dl>
<p> <i>size</i></p>
<dl>
<dd>The size of the buffer, including the trailing null space</dl>
<p> <i>fmt</i></p>
<dl>
<dd>The format string to use</dl>
<p> <i>&#8230;</i></p>
<dl>
<dd>Arguments for the format string</dl>
<h2>Description</h2>
<p>The return value is the number of characters which would be generated for the given input, excluding the trailing null, as per ISO C99. If the return is greater than or equal to <i>size</i>, the resulting string is truncated. </p>
<p> See the <code>vsnprintf</code> documentation for format string extensions over C99.</p>
<h2>Copyright</h2>
