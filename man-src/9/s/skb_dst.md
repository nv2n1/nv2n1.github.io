---
title: "skb_dst(9)"
name: "skb_dst"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_dst/"
---

skb_dst - returns skb dst_entry

<h2>Synopsis</h2>

<pre><code>struct dst_entry *skb_dst(const struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer</dl>

<h2>Description</h2>

Returns skb dst_entry, regardless of reference taken or not.

<h2>Copyright</h2>


