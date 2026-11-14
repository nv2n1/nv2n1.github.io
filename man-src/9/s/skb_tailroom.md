---
title: "skb_tailroom(9)"
name: "skb_tailroom"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_tailroom/"
---

skb_tailroom - bytes at buffer end

<h2>Synopsis</h2>

<pre><code>int skb_tailroom(const struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to check</dl>

<h2>Description</h2>

Return the number of bytes of free space at the tail of an sk_buff

<h2>Copyright</h2>


