---
title: "skb_headroom(9)"
name: "skb_headroom"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_headroom/"
---

skb_headroom - bytes at buffer head

<h2>Synopsis</h2>

<pre><code>unsigned int skb_headroom(const struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to check</dl>

<h2>Description</h2>

Return the number of bytes of free space at the head of an sk_buff.

<h2>Copyright</h2>


