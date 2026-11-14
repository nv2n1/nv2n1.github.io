---
title: "skb_unlink(9)"
name: "skb_unlink"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_unlink/"
---

skb_unlink - remove a buffer from a list

<h2>Synopsis</h2>

<pre><code>void skb_unlink(struct sk_buff *skb, struct sk_buff_head *list);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to remove</dl>
 

 <i>list</i>
<dl><dd>list to use</dl>

<h2>Description</h2>

Remove a packet from a list. The list locks are taken and this function is atomic with respect to other list locked calls 

 You must know what list the SKB is on.

<h2>Copyright</h2>


