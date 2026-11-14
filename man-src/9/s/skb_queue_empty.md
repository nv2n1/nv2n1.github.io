---
title: "skb_queue_empty(9)"
name: "skb_queue_empty"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_queue_empty/"
---

skb_queue_empty - check if a queue is empty

<h2>Synopsis</h2>

<pre><code>int skb_queue_empty(const struct sk_buff_head *list);</code></pre>

<h2>Arguments</h2>

<i>list</i>
<dl><dd><dd>queue head</dl>

<h2>Description</h2>

Returns true if the queue is empty, false otherwise.

<h2>Copyright</h2>


