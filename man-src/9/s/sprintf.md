---
title: "sprintf(9)"
name: "sprintf"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sprintf/"
description: "sprintf – Format a string and place it in a buffer"
---

<p>sprintf &#8211; Format a string and place it in a buffer</p>
<h2>Synopsis</h2>
<pre><code>int sprintf(char *buf, const char *fmt, ...);</code></pre>
<h2>Arguments</h2>
<p><i>buf</i></p>
<dl>
<dd>
<dd>The buffer to place the result into</dl>
<p> <i>fmt</i></p>
<dl>
<dd>The format string to use</dl>
<p> <i>&#8230;</i></p>
<dl>
<dd>Arguments for the format string</dl>
<h2>Description</h2>
<p>The function returns the number of characters written into <i>buf</i>. Use <code>snprintf</code> or <code>scnprintf</code> in order to avoid buffer overflows. </p>
<p> See the <code>vsnprintf</code> documentation for format string extensions over C99.</p>
<h2>Copyright</h2>
