---
title: "scnprintf(9)"
name: "scnprintf"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scnprintf/"
---

scnprintf - Format a string and place it in a buffer

<h2>Synopsis</h2>

<pre><code>int scnprintf(char *buf, size_t size, const char *fmt, ...);</code></pre>

<h2>Arguments</h2>

<i>buf</i>
<dl><dd><dd>The buffer to place the result into</dl>
 

 <i>size</i>
<dl><dd>The size of the buffer, including the trailing null space</dl>
 

 <i>fmt</i>
<dl><dd>The format string to use</dl>
 

 <i>...</i>
<dl><dd>Arguments for the format string</dl>

<h2>Description</h2>

The return value is the number of characters written into <i>buf</i> not including the trailing '\0'. If <i>size</i> is == 0 the function returns 0.

<h2>Copyright</h2>


