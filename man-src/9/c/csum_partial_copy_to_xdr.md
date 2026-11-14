---
title: "csum_partial_copy_to_xdr(9)"
name: "csum_partial_copy_to_xdr"
section: "9"
letter: "c"
url: "/docs/linux/man/9-csum_partial_copy_to_xdr/"
---

csum_partial_copy_to_xdr - checksum and copy data

<h2>Synopsis</h2>

<pre><code>int csum_partial_copy_to_xdr(struct xdr_buf *xdr, struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>xdr</i>
<dl><dd><dd>target XDR buffer</dl>
 

 <i>skb</i>
<dl><dd>source skb</dl>

<h2>Description</h2>

We have set things up such that we perform the checksum of the UDP packet in parallel with the copies into the RPC client iovec. -DaveM

<h2>Copyright</h2>


