---
title: "xdr_buf_trim(9)"
name: "xdr_buf_trim"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xdr_buf_trim/"
---

xdr_buf_trim - lop at most "len" bytes off the end of "buf"

<h2>Synopsis</h2>

<pre><code>void xdr_buf_trim(struct xdr_buf *buf, unsigned int len);</code></pre>

<h2>Arguments</h2>

<i>buf</i>
<dl><dd><dd>buf to be trimmed</dl>
 

 <i>len</i>
<dl><dd>number of bytes to reduce "buf" by</dl>

<h2>Description</h2>

Trim an xdr_buf by the given number of bytes by fixing up the lengths. Note that it's possible that we'll trim less than that amount if the xdr_buf is too small, or if (for instance) it's all in the head and the parser has already read too far into it.

<h2>Copyright</h2>


