---
title: "bprintf(9)"
name: "bprintf"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bprintf/"
---

bprintf - Parse a format string and place args' binary value in a buffer

<h2>Synopsis</h2>

<pre><code>int bprintf(u32 *bin_buf, size_t size, const char *fmt, ...);</code></pre>

<h2>Arguments</h2>

<i>bin_buf</i>
<dl><dd><dd>The buffer to place args' binary value</dl>
 

 <i>size</i>
<dl><dd>The size of the buffer(by words(32bits), not characters)</dl>
 

 <i>fmt</i>
<dl><dd>The format string to use</dl>
 

 <i>...</i>
<dl><dd>Arguments for the format string</dl>

<h2>Description</h2>

The function returns the number of words(u32) written into <i>bin_buf</i>.

<h2>Copyright</h2>


