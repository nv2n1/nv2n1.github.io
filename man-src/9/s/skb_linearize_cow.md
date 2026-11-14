---
title: "skb_linearize_cow(9)"
name: "skb_linearize_cow"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_linearize_cow/"
---

skb_linearize_cow - make sure skb is linear and writable

<h2>Synopsis</h2>

<pre><code>int skb_linearize_cow(struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to process</dl>

<h2>Description</h2>

If there is no free memory -ENOMEM is returned, otherwise zero is returned and the old skb data released.

<h2>Copyright</h2>


