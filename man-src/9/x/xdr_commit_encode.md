---
title: "xdr_commit_encode(9)"
name: "xdr_commit_encode"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xdr_commit_encode/"
---

xdr_commit_encode - Ensure all data is written to buffer

<h2>Synopsis</h2>

<pre><code>void xdr_commit_encode(struct xdr_stream *xdr);</code></pre>

<h2>Arguments</h2>

<i>xdr</i>
<dl><dd><dd>pointer to xdr_stream</dl>

<h2>Description</h2>

We handle encoding across page boundaries by giving the caller a temporary location to write to, then later copying the data into place; xdr_commit_encode does that copying. 

 Normally the caller doesn't need to call this directly, as the following xdr_reserve_space will do it. But an explicit call may be required at the end of encoding, or any other time when the xdr_buf data might be read.

<h2>Copyright</h2>


