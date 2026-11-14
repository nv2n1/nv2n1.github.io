---
title: "skb_get(9)"
name: "skb_get"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_get/"
---

skb_get - reference buffer

<h2>Synopsis</h2>

<pre><code>struct sk_buff *skb_get(struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to reference</dl>

<h2>Description</h2>

Makes another reference to a socket buffer and returns a pointer to the buffer.

<h2>Copyright</h2>


