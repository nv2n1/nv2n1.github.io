---
title: "xdr_restrict_buflen(9)"
name: "xdr_restrict_buflen"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xdr_restrict_buflen/"
---

xdr_restrict_buflen - decrease available buffer space

<h2>Synopsis</h2>

<pre><code>int xdr_restrict_buflen(struct xdr_stream *xdr, int newbuflen);</code></pre>

<h2>Arguments</h2>

<i>xdr</i>
<dl><dd><dd>pointer to xdr_stream</dl>
 

 <i>newbuflen</i>
<dl><dd>new maximum number of bytes available</dl>

<h2>Description</h2>

Adjust our idea of how much space is available in the buffer. If we've already used too much space in the buffer, returns -1. If the available space is already smaller than newbuflen, returns 0 and does nothing. Otherwise, adjusts xdr-&gt;buf-&gt;buflen to newbuflen and ensures xdr-&gt;end is set at most offset newbuflen from the start of the buffer.

<h2>Copyright</h2>


