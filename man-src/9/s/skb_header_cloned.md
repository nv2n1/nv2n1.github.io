---
title: "skb_header_cloned(9)"
name: "skb_header_cloned"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_header_cloned/"
---

skb_header_cloned - is the header a clone

<h2>Synopsis</h2>

<pre><code>int skb_header_cloned(const struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to check</dl>

<h2>Description</h2>

Returns true if modifying the header part of the buffer requires the data to be copied.

<h2>Copyright</h2>


