---
title: "xdr_encode_opaque(9)"
name: "xdr_encode_opaque"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xdr_encode_opaque/"
description: "xdr_encode_opaque – Encode variable length opaque data"
---

<p>xdr_encode_opaque &#8211; Encode variable length opaque data</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>__be32 * xdr_encode_opaque(__be32&nbsp;<wbr>*&nbsp;<wbr></code><i>p</i><code>, const void&nbsp;<wbr>*&nbsp;<wbr></code><i>ptr</i><code>, unsigned int&nbsp;<wbr></code><i>nbytes</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>p</i></p>
<dl>
<dd>
<dd>pointer to current position in XDR buffer.</dl>
<p> <i>ptr</i></p>
<dl>
<dd>pointer to data to encode (or NULL)</dl>
<p> <i>nbytes</i></p>
<dl>
<dd>size of data.</dl>
<h2>Description</h2>
<p>Returns the updated current XDR buffer position</p>
<h2>Copyright</h2>
