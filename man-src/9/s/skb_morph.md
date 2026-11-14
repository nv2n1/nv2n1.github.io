---
title: "skb_morph(9)"
name: "skb_morph"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_morph/"
---

skb_morph - morph one skb into another

<h2>Synopsis</h2>

<pre><code>struct sk_buff *skb_morph(struct sk_buff *dst, struct sk_buff *src);</code></pre>

<h2>Arguments</h2>

<i>dst</i>
<dl><dd><dd>the skb to receive the contents</dl>
 

 <i>src</i>
<dl><dd>the skb to supply the contents</dl>

<h2>Description</h2>

This is identical to skb_clone except that the target skb is supplied by the user. 

 The target skb is returned upon exit.

<h2>Copyright</h2>


