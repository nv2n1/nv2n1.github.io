---
title: "skb_cow_head(9)"
name: "skb_cow_head"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_cow_head/"
---

skb_cow_head - skb_cow but only making the head writable

<h2>Synopsis</h2>

<pre><code>int skb_cow_head(struct sk_buff *skb, unsigned int headroom);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to cow</dl>
 

 <i>headroom</i>
<dl><dd>needed headroom</dl>

<h2>Description</h2>

This function is identical to skb_cow except that we replace the skb_cloned check by skb_header_cloned. It should be used when you only need to push on some header and do not need to modify the data.

<h2>Copyright</h2>


