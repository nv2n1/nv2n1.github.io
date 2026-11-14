---
title: "skb_queue_splice_tail(9)"
name: "skb_queue_splice_tail"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_queue_splice_tail/"
---

skb_queue_splice_tail - join two skb lists, each list being a queue

<h2>Synopsis</h2>

<pre><code>void skb_queue_splice_tail(const struct sk_buff_head *list, struct sk_buff_head *head);</code></pre>

<h2>Arguments</h2>

<i>list</i>
<dl><dd><dd>the new list to add</dl>
 

 <i>head</i>
<dl><dd>the place to add it in the first list</dl>

<h2>Copyright</h2>


