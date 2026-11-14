---
title: "skb_push(9)"
name: "skb_push"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_push/"
---

skb_push - add data to the start of a buffer

<h2>Synopsis</h2>

<pre><code>unsigned char *skb_push(struct sk_buff *skb, unsigned int len);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to use</dl>
 

 <i>len</i>
<dl><dd>amount of data to add</dl>

<h2>Description</h2>

This function extends the used data area of the buffer at the buffer start. If this would exceed the total buffer headroom the kernel will panic. A pointer to the first byte of the extra data is returned.

<h2>Copyright</h2>


