---
title: "skb_peek_next(9)"
name: "skb_peek_next"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_peek_next/"
description: "skb_peek_next – peek skb following the given one from a queue"
---

<p>skb_peek_next &#8211; peek skb following the given one from a queue</p>
<h2>Synopsis</h2>
<pre><code>struct sk_buff *skb_peek_next(struct sk_buff *skb, const struct sk_buff_head *list_);</code></pre>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>skb to start from</dl>
<p> <i>list_</i></p>
<dl>
<dd>list to peek at</dl>
<h2>Description</h2>
<p>Returns <code>NULL</code> when the end of the list is met or a pointer to the next element. The reference count is not incremented and the reference is therefore volatile. Use with caution.</p>
<h2>Copyright</h2>
