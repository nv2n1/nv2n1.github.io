---
title: "skb_clone(9)"
name: "skb_clone"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_clone/"
description: "skb_clone – duplicate an sk_buff"
---

<p>skb_clone &#8211; duplicate an sk_buff</p>
<h2>Synopsis</h2>
<pre><code>struct sk_buff *skb_clone(struct sk_buff *skb, gfp_t gfp_mask);</code></pre>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>buffer to clone</dl>
<p> <i>gfp_mask</i></p>
<dl>
<dd>allocation priority</dl>
<h2>Description</h2>
<p>Duplicate an sk_buff. The new one is not owned by a socket. Both copies share the same packet data but not structure. The new buffer has a reference count of 1. If the allocation fails the function returns <code>NULL</code> otherwise the new buffer is returned. </p>
<p> If this function is called from an interrupt <code>gfp_mask</code> must be <code>GFP_ATOMIC</code>.</p>
<h2>Copyright</h2>
