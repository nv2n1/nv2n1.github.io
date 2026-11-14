---
title: "vscnprintf(9)"
name: "vscnprintf"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vscnprintf/"
description: "vscnprintf – Format a string and place it in a buffer"
---

<p>vscnprintf &#8211; Format a string and place it in a buffer</p>
<h2>Synopsis</h2>
<pre><code>int vscnprintf(char *buf, size_t size, const char *fmt, va_list args);</code></pre>
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
<p>The return value is the number of characters which have been written into the <i>buf</i> not including the trailing &#8216;
