---
title: "vsprintf(9)"
name: "vsprintf"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vsprintf/"
description: "vsprintf – Format a string and place it in a buffer"
---

<p>vsprintf &#8211; Format a string and place it in a buffer</p>
<h2>Synopsis</h2>
<pre><code>int vsprintf(char *buf, const char *fmt, va_list args);</code></pre>
<h2>Arguments</h2>
<p><i>buf</i></p>
<dl>
<dd>
<dd>The buffer to place the result into</dl>
<p> <i>fmt</i></p>
<dl>
<dd>The format string to use</dl>
<p> <i>args</i></p>
<dl>
<dd>Arguments for the format string</dl>
<h2>Description</h2>
<p>The function returns the number of characters written into <i>buf</i>. Use <code>vsnprintf</code> or <code>vscnprintf</code> in order to avoid buffer overflows. </p>
<p> If you&#8217;re not already dealing with a va_list consider using <code>sprintf</code>. </p>
<p> See the <code>vsnprintf</code> documentation for format string extensions over C99.</p>
<h2>Copyright</h2>
