---
title: "skb_queue_is_first(9)"
name: "skb_queue_is_first"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_queue_is_first/"
description: "skb_queue_is_first – check if skb is the first entry in the queue"
---

<p>skb_queue_is_first &#8211; check if skb is the first entry in the queue</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool skb_queue_is_first(const struct sk_buff_head&nbsp;<wbr>*&nbsp;<wbr></code><i>list</i><code>, const struct sk_buff&nbsp;<wbr>*&nbsp;<wbr></code><i>skb</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>list</i></p>
<dl>
<dd>
<dd>queue head</dl>
<p> <i>skb</i></p>
<dl>
<dd>buffer</dl>
<h2>Description</h2>
<p>Returns true if <i>skb</i> is the first buffer on the list.</p>
<h2>Copyright</h2>
