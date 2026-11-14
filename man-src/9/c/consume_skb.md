---
title: "consume_skb(9)"
name: "consume_skb"
section: "9"
letter: "c"
url: "/docs/linux/man/9-consume_skb/"
---

consume_skb - free an skbuff

<h2>Synopsis</h2>

<pre><code>void consume_skb(struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to free</dl>

<h2>Description</h2>

Drop a ref to the buffer and free it if the usage count has hit zero Functions identically to kfree_skb, but kfree_skb assumes that the frame is being dropped after a failure and notes that

<h2>Copyright</h2>


