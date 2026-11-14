---
title: "kfree_skb(9)"
name: "kfree_skb"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kfree_skb/"
---

kfree_skb - free an sk_buff

<h2>Synopsis</h2>

<pre><code>void kfree_skb(struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to free</dl>

<h2>Description</h2>

Drop a reference to the buffer and free it if the usage count has hit zero.

<h2>Copyright</h2>


