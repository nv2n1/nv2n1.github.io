---
title: "skb_dequeue_tail(9)"
name: "skb_dequeue_tail"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_dequeue_tail/"
description: "skb_dequeue_tail – remove from the tail of the queue"
---

<p>skb_dequeue_tail &#8211; remove from the tail of the queue</p>
<h2>Synopsis</h2>
<pre><code>struct sk_buff *skb_dequeue_tail(struct sk_buff_head *list);</code></pre>
<h2>Arguments</h2>
<p><i>list</i></p>
<dl>
<dd>
<dd>list to dequeue from</dl>
<h2>Description</h2>
<p>Remove the tail of the list. The list lock is taken so the function may be used safely with other locking list functions. The tail item is returned or <code>NULL</code> if the list is empty.</p>
<h2>Copyright</h2>
