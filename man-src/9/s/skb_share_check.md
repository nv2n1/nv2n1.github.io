---
title: "skb_share_check(9)"
name: "skb_share_check"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_share_check/"
---

skb_share_check - check if buffer is shared and if so clone it

<h2>Synopsis</h2>

<pre><code>struct sk_buff *skb_share_check(struct sk_buff *skb, gfp_t pri);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to check</dl>
 

 <i>pri</i>
<dl><dd>priority for memory allocation</dl>

<h2>Description</h2>

If the buffer is shared the buffer is cloned and the old copy drops a reference. A new clone with a single reference is returned. If the buffer is not shared the original buffer is returned. When being called from interrupt status or with spinlocks held pri must be GFP_ATOMIC. 

 NULL is returned on a memory allocation failure.

<h2>Copyright</h2>


