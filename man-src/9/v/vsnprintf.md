---
title: "vsnprintf(9)"
name: "vsnprintf"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vsnprintf/"
description: "vsnprintf – Format a string and place it in a buffer"
---

<p>vsnprintf &#8211; Format a string and place it in a buffer</p>
<h2>Synopsis</h2>
<pre><code>int vsnprintf(char *buf, size_t size, const char *fmt, va_list args);</code></pre>
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
<p> <i>args</i></p>
<dl>
<dd>Arguments for the format string</dl>
<h2>Description</h2>
<p>This function generally follows C99 vsnprintf, but has some extensions and a few limitations: </p>
<p> <code>n</code> is unsupported <code>p</code>* is handled by <code>pointer</code> </p>
<p> See <code>pointer</code> or Documentation/printk-formats.txt for more extensive description. </p>
<p> ** Please update the documentation in both places when making changes ** </p>
<p> The return value is the number of characters which would be generated for the given input, excluding the trailing &#8216;
