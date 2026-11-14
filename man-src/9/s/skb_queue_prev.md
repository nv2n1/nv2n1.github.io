---
title: "skb_queue_prev(9)"
name: "skb_queue_prev"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_queue_prev/"
description: "skb_queue_prev – return the prev packet in the queue"
---

<p>skb_queue_prev &#8211; return the prev packet in the queue</p>
<h2>Synopsis</h2>
<pre><code>struct sk_buff *skb_queue_prev(const struct sk_buff_head *list, const struct sk_buff *skb);</code></pre>
<h2>Arguments</h2>
<p><i>list</i></p>
<dl>
<dd>
<dd>queue head</dl>
<p> <i>skb</i></p>
<dl>
<dd>current buffer</dl>
<h2>Description</h2>
<p>Return the prev packet in <i>list</i> before <i>skb</i>. It is only valid to call this if <code>skb_queue_is_first</code> evaluates to false.</p>
<h2>Copyright</h2>
