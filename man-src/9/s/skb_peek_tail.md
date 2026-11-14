---
title: "skb_peek_tail(9)"
name: "skb_peek_tail"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_peek_tail/"
description: "skb_peek_tail – peek at the tail of an sk_buff_head"
---

<p>skb_peek_tail &#8211; peek at the tail of an sk_buff_head</p>
<h2>Synopsis</h2>
<pre><code>struct sk_buff *skb_peek_tail(const struct sk_buff_head *list_);</code></pre>
<h2>Arguments</h2>
<p><i>list_</i></p>
<dl>
<dd>
<dd>list to peek at</dl>
<h2>Description</h2>
<p>Peek an sk_buff. Unlike most other operations you _MUST_ be careful with this one. A peek leaves the buffer on the list and someone else may run off with it. You must hold the appropriate locks or have a private queue to do this. </p>
<p> Returns <code>NULL</code> for an empty list or a pointer to the tail element. The reference count is not incremented and the reference is therefore volatile. Use with caution.</p>
<h2>Copyright</h2>
