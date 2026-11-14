---
title: "skb_tailroom_reserve(9)"
name: "skb_tailroom_reserve"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_tailroom_reserve/"
---

skb_tailroom_reserve - adjust reserved_tailroom

<h2>Synopsis</h2>

<pre><code>void skb_tailroom_reserve(struct sk_buff *skb, unsigned int mtu, unsigned int needed_tailroom);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to alter</dl>
 

 <i>mtu</i>
<dl><dd>maximum amount of headlen permitted</dl>
 

 <i>needed_tailroom</i>
<dl><dd>minimum amount of reserved_tailroom</dl>

<h2>Description</h2>

Set reserved_tailroom so that headlen can be as large as possible but not larger than mtu and tailroom cannot be smaller than needed_tailroom. The required headroom should already have been reserved before using this function.

<h2>Copyright</h2>


