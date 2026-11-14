---
title: "skb_queue_next(9)"
name: "skb_queue_next"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_queue_next/"
description: "skb_queue_next – return the next packet in the queue"
---

<p>skb_queue_next &#8211; return the next packet in the queue</p>
<h2>Synopsis</h2>
<pre><code>struct sk_buff *skb_queue_next(const struct sk_buff_head *list, const struct sk_buff *skb);</code></pre>
<h2>Arguments</h2>
<p><i>list</i></p>
<dl>
<dd>
<dd>queue head</dl>
<p> <i>skb</i></p>
<dl>
<dd>current buffer</dl>
<h2>Description</h2>
<p>Return the next packet in <i>list</i> after <i>skb</i>. It is only valid to call this if <code>skb_queue_is_last</code> evaluates to false.</p>
<h2>Copyright</h2>
