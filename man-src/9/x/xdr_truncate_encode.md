---
title: "xdr_truncate_encode(9)"
name: "xdr_truncate_encode"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xdr_truncate_encode/"
---

xdr_truncate_encode - truncate an encode buffer

<h2>Synopsis</h2>

<pre><code>void xdr_truncate_encode(struct xdr_stream *xdr, size_t len);</code></pre>

<h2>Arguments</h2>

<i>xdr</i>
<dl><dd><dd>pointer to xdr_stream</dl>
 

 <i>len</i>
<dl><dd>new length of buffer</dl>

<h2>Description</h2>

Truncates the xdr stream, so that xdr-&gt;buf-&gt;len == len, and xdr-&gt;p points at offset len from the start of the buffer, and head, tail, and page lengths are adjusted to correspond. 

 If this means moving xdr-&gt;p to a different buffer, we assume that that the end pointer should be set to the end of the current page, except in the case of the head buffer when we assume the head buffer's current length represents the end of the available buffer. 

 This is *not* safe to use on a buffer that already has inlined page cache pages (as in a zero-copy server read reply), except for the simple case of truncating from one position in the tail to another.

<h2>Copyright</h2>


