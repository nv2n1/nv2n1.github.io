---
title: "skb_split(9)"
name: "skb_split"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_split/"
---

skb_split - Split fragmented skb to two parts at length len.

<h2>Synopsis</h2>

<pre><code>void skb_split(struct sk_buff *skb, struct sk_buff *skb1, const u32 len);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>the buffer to split</dl>
 

 <i>skb1</i>
<dl><dd>the buffer to receive the second part</dl>
 

 <i>len</i>
<dl><dd>new length for skb</dl>

<h2>Copyright</h2>


