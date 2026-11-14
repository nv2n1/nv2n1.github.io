---
title: "skb_shared(9)"
name: "skb_shared"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_shared/"
---

skb_shared - is the buffer shared

<h2>Synopsis</h2>

<pre><code>int skb_shared(const struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to check</dl>

<h2>Description</h2>

Returns true if more than one person has a reference to this buffer.

<h2>Copyright</h2>


