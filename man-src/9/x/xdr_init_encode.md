---
title: "xdr_init_encode(9)"
name: "xdr_init_encode"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xdr_init_encode/"
description: "xdr_init_encode – Initialize a struct xdr_stream for sending data."
---

<p>xdr_init_encode &#8211; Initialize a struct xdr_stream for sending data.</p>
<h2>Synopsis</h2>
<pre><code>void xdr_init_encode(struct xdr_stream *xdr, struct xdr_buf *buf, __be32 *p);</code></pre>
<h2>Arguments</h2>
<p><i>xdr</i></p>
<dl>
<dd>
<dd>pointer to xdr_stream struct</dl>
<p> <i>buf</i></p>
<dl>
<dd>pointer to XDR buffer in which to encode data</dl>
<p> <i>p</i></p>
<dl>
<dd>current pointer inside XDR buffer</dl>
<h2>Note</h2>
<p>at the moment the RPC client only passes the length of our scratch buffer in the xdr_buf&#8217;s header kvec. Previously this meant we needed to call <code>xdr_adjust_iovec</code> after encoding the data. With the new scheme, the xdr_stream manages the details of the buffer length, and takes care of adjusting the kvec length for us.</p>
<h2>Copyright</h2>
