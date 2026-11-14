---
title: "skb_queue_len(9)"
name: "skb_queue_len"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_queue_len/"
description: "skb_queue_len – get queue length"
---

<p>skb_queue_len &#8211; get queue length</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>__u32 skb_queue_len(const struct sk_buff_head&nbsp;<wbr>*&nbsp;<wbr></code><i>list_</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>list_</i></p>
<dl>
<dd>
<dd>list to measure</dl>
<h2>Description</h2>
<p>Return the length of an sk_buff queue.</p>
<h2>Copyright</h2>
