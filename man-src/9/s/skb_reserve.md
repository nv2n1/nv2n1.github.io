---
title: "skb_reserve(9)"
name: "skb_reserve"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_reserve/"
---

skb_reserve - adjust headroom

<h2>Synopsis</h2>

<pre><code>void skb_reserve(struct sk_buff *skb, int len);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to alter</dl>
 

 <i>len</i>
<dl><dd>bytes to move</dl>

<h2>Description</h2>

Increase the headroom of an empty sk_buff by reducing the tail room. This is only allowed for an empty buffer.

<h2>Copyright</h2>


