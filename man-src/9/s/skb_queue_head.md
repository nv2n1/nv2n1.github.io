---
title: "skb_queue_head(9)"
name: "skb_queue_head"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_queue_head/"
---

skb_queue_head - queue a buffer at the list head

<h2>Synopsis</h2>

<pre><code>void skb_queue_head(struct sk_buff_head *list, struct sk_buff *newsk);</code></pre>

<h2>Arguments</h2>

<i>list</i>
<dl><dd><dd>list to use</dl>
 

 <i>newsk</i>
<dl><dd>buffer to queue</dl>

<h2>Description</h2>

Queue a buffer at the start of the list. This function takes the list lock and can be used safely with other locking sk_buff functions safely. 

 A buffer cannot be placed on two lists at the same time.

<h2>Copyright</h2>


