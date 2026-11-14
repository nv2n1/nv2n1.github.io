---
title: "skb_copy_bits(9)"
name: "skb_copy_bits"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_copy_bits/"
---

skb_copy_bits - copy bits from skb to kernel buffer

<h2>Synopsis</h2>

<pre><code>int skb_copy_bits(const struct sk_buff *skb, int offset, void *to, int len);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>source skb</dl>
 

 <i>offset</i>
<dl><dd>offset in source</dl>
 

 <i>to</i>
<dl><dd>destination buffer</dl>
 

 <i>len</i>
<dl><dd>number of bytes to copy</dl>

<h2>Description</h2>

Copy the specified number of bytes from the source skb to the destination buffer. 

 CAUTION ! : If its prototype is ever changed, check arch/{*}/net/{*}.S files, since it is called from BPF assembly code.

<h2>Copyright</h2>


