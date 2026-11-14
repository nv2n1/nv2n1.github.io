---
title: "xdr_inline_decode(9)"
name: "xdr_inline_decode"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xdr_inline_decode/"
description: "xdr_inline_decode – Retrieve XDR data to decode"
---

<p>xdr_inline_decode &#8211; Retrieve XDR data to decode</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>__be32 * xdr_inline_decode(struct xdr_stream&nbsp;<wbr>*&nbsp;<wbr></code><i>xdr</i><code>, size_t&nbsp;<wbr></code><i>nbytes</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>xdr</i></p>
<dl>
<dd>
<dd>pointer to xdr_stream struct</dl>
<p> <i>nbytes</i></p>
<dl>
<dd>number of bytes of data to decode</dl>
<h2>Description</h2>
<p>Check if the input buffer is long enough to enable us to decode &#8216;nbytes&#8217; more bytes of data starting at the current position. If so return the current pointer, then update the current pointer position.</p>
<h2>Copyright</h2>
