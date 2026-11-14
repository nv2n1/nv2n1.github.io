---
title: "skb_trim(9)"
name: "skb_trim"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_trim/"
---

skb_trim - remove end from a buffer

<h2>Synopsis</h2>

<pre><code>void skb_trim(struct sk_buff *skb, unsigned int len);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to alter</dl>
 

 <i>len</i>
<dl><dd>new length</dl>

<h2>Description</h2>

Cut the length of a buffer down by removing data from the tail. If the buffer is already under the length specified it is not modified. The skb must be linear.

<h2>Copyright</h2>


