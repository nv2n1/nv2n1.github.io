---
title: "skb_linearize(9)"
name: "skb_linearize"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_linearize/"
---

skb_linearize - convert paged skb to linear one

<h2>Synopsis</h2>

<pre><code>int skb_linearize(struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to linarize</dl>

<h2>Description</h2>

If there is no free memory -ENOMEM is returned, otherwise zero is returned and the old skb data released.

<h2>Copyright</h2>


