---
title: "xdr_skb_read_bits(9)"
name: "xdr_skb_read_bits"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xdr_skb_read_bits/"
---

xdr_skb_read_bits - copy some data bits from skb to internal buffer

<h2>Synopsis</h2>

<pre><code>size_t xdr_skb_read_bits(struct xdr_skb_reader *desc, void *to, size_t len);</code></pre>

<h2>Arguments</h2>

<i>desc</i>
<dl><dd><dd>sk_buff copy helper</dl>
 

 <i>to</i>
<dl><dd>copy destination</dl>
 

 <i>len</i>
<dl><dd>number of bytes to copy</dl>

<h2>Description</h2>

Possibly called several times to iterate over an sk_buff and copy data out of it.

<h2>Copyright</h2>


