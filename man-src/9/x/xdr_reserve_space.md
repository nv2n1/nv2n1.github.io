---
title: "xdr_reserve_space(9)"
name: "xdr_reserve_space"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xdr_reserve_space/"
description: "xdr_reserve_space – Reserve buffer space for sending"
---

<p>xdr_reserve_space &#8211; Reserve buffer space for sending</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>__be32 * xdr_reserve_space(struct xdr_stream&nbsp;<wbr>*&nbsp;<wbr></code><i>xdr</i><code>, size_t&nbsp;<wbr></code><i>nbytes</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>xdr</i></p>
<dl>
<dd>
<dd>pointer to xdr_stream</dl>
<p> <i>nbytes</i></p>
<dl>
<dd>number of bytes to reserve</dl>
<h2>Description</h2>
<p>Checks that we have enough buffer space to encode &#8216;nbytes&#8217; more bytes of data. If so, update the total xdr_buf length, and adjust the length of the current kvec.</p>
<h2>Copyright</h2>
