---
title: "skb_store_bits(9)"
name: "skb_store_bits"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_store_bits/"
---

skb_store_bits - store bits from kernel buffer to skb

<h2>Synopsis</h2>

<pre><code>int skb_store_bits(struct sk_buff *skb, int offset, const void *from, int len);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>destination buffer</dl>
 

 <i>offset</i>
<dl><dd>offset in destination</dl>
 

 <i>from</i>
<dl><dd>source buffer</dl>
 

 <i>len</i>
<dl><dd>number of bytes to copy</dl>

<h2>Description</h2>

Copy the specified number of bytes from the source buffer to the destination skb. This function handles all the messy bits of traversing fragment lists and such.

<h2>Copyright</h2>


