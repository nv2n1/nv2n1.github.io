---
title: "skb_put(9)"
name: "skb_put"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_put/"
---

skb_put - add data to a buffer

<h2>Synopsis</h2>

<pre><code>unsigned char *skb_put(struct sk_buff *skb, unsigned int len);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to use</dl>
 

 <i>len</i>
<dl><dd>amount of data to add</dl>

<h2>Description</h2>

This function extends the used data area of the buffer. If this would exceed the total buffer size the kernel will panic. A pointer to the first byte of the extra data is returned.

<h2>Copyright</h2>


