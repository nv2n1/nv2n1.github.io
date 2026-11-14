---
title: "skb_dequeue(9)"
name: "skb_dequeue"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_dequeue/"
description: "skb_dequeue – remove from the head of the queue"
---

<p>skb_dequeue &#8211; remove from the head of the queue</p>
<h2>Synopsis</h2>
<pre><code>struct sk_buff *skb_dequeue(struct sk_buff_head *list);</code></pre>
<h2>Arguments</h2>
<p><i>list</i></p>
<dl>
<dd>
<dd>list to dequeue from</dl>
<h2>Description</h2>
<p>Remove the head of the list. The list lock is taken so the function may be used safely with other locking list functions. The head item is returned or <code>NULL</code> if the list is empty.</p>
<h2>Copyright</h2>
