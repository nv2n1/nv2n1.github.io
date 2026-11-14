---
title: "xdr_terminate_string(9)"
name: "xdr_terminate_string"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xdr_terminate_string/"
---

xdr_terminate_string - '\0'-terminate a string residing in an xdr_buf

<h2>Synopsis</h2>

<pre><code>void xdr_terminate_string(struct xdr_buf *buf, const u32 len);</code></pre>

<h2>Arguments</h2>

<i>buf</i>
<dl><dd><dd>XDR buffer where string resides</dl>
 

 <i>len</i>
<dl><dd>length of string, in bytes</dl>

<h2>Copyright</h2>


