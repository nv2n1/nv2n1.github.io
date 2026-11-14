---
title: "skb_append(9)"
name: "skb_append"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_append/"
---

skb_append - append a buffer

<h2>Synopsis</h2>

<pre><code>void skb_append(struct sk_buff *old, struct sk_buff *newsk, struct sk_buff_head *list);</code></pre>

<h2>Arguments</h2>

<i>old</i>
<dl><dd><dd>buffer to insert after</dl>
 

 <i>newsk</i>
<dl><dd>buffer to insert</dl>
 

 <i>list</i>
<dl><dd>list to use</dl>

<h2>Description</h2>

Place a packet after a given packet in a list. The list locks are taken and this function is atomic with respect to other list locked calls. A buffer cannot be placed on two lists at the same time.

<h2>Copyright</h2>


