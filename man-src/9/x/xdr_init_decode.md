---
title: "xdr_init_decode(9)"
name: "xdr_init_decode"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xdr_init_decode/"
---

xdr_init_decode - Initialize an xdr_stream for decoding data.

<h2>Synopsis</h2>

<pre><code>void xdr_init_decode(struct xdr_stream *xdr, struct xdr_buf *buf, __be32 *p);</code></pre>

<h2>Arguments</h2>

<i>xdr</i>
<dl><dd><dd>pointer to xdr_stream struct</dl>
 

 <i>buf</i>
<dl><dd>pointer to XDR buffer from which to decode data</dl>
 

 <i>p</i>
<dl><dd>current pointer inside XDR buffer</dl>

<h2>Copyright</h2>


