---
title: "skb_head_is_locked(9)"
name: "skb_head_is_locked"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_head_is_locked/"
description: "skb_head_is_locked – Determine if the skb->head is locked down"
---

<p>skb_head_is_locked &#8211; Determine if the skb-&gt;head is locked down</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool skb_head_is_locked(const struct sk_buff&nbsp;<wbr>*&nbsp;<wbr></code><i>skb</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>skb to check</dl>
<h2>Description</h2>
<p>The head on skbs build around a head frag can be removed if they are not cloned. This function returns true if the skb head is locked down due to either being allocated via kmalloc, or by being a clone with multiple references to the head.</p>
<h2>Copyright</h2>
