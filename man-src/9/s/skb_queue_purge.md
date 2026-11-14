---
title: "skb_queue_purge(9)"
name: "skb_queue_purge"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_queue_purge/"
---

skb_queue_purge - empty a list

<h2>Synopsis</h2>

<pre><code>void skb_queue_purge(struct sk_buff_head *list);</code></pre>

<h2>Arguments</h2>

<i>list</i>
<dl><dd><dd>list to empty</dl>

<h2>Description</h2>

Delete all buffers on an sk_buff list. Each buffer is removed from the list and one reference dropped. This function takes the list lock and is atomic with respect to other list locking functions.

<h2>Copyright</h2>


