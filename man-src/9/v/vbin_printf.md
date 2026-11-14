---
title: "vbin_printf(9)"
name: "vbin_printf"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vbin_printf/"
description: "vbin_printf – Parse a format string and place args’ binary value in a buffer"
---

<p>vbin_printf &#8211; Parse a format string and place args&#8217; binary value in a buffer</p>
<h2>Synopsis</h2>
<pre><code>int vbin_printf(u32 *bin_buf, size_t size, const char *fmt, va_list args);</code></pre>
<h2>Arguments</h2>
<p><i>bin_buf</i></p>
<dl>
<dd>
<dd>The buffer to place args&#8217; binary value</dl>
<p> <i>size</i></p>
<dl>
<dd>The size of the buffer(by words(32bits), not characters)</dl>
<p> <i>fmt</i></p>
<dl>
<dd>The format string to use</dl>
<p> <i>args</i></p>
<dl>
<dd>Arguments for the format string</dl>
<h2>Description</h2>
<p>The format follows C99 vsnprintf, except <code>n</code> is ignored, and its argument is skipped. </p>
<p> The return value is the number of words(32bits) which would be generated for the given input.</p>
<h2>Note</h2>
<p>If the return value is greater than <i>size</i>, the resulting bin_buf is NOT valid for <code>bstr_printf</code>.</p>
<h2>Copyright</h2>
