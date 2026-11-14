---
title: "skb_copy_expand(9)"
name: "skb_copy_expand"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_copy_expand/"
description: "skb_copy_expand – copy and expand sk_buff"
---

<p>skb_copy_expand &#8211; copy and expand sk_buff</p>
<h2>Synopsis</h2>
<pre><code>struct sk_buff *skb_copy_expand(const struct sk_buff *skb, int newheadroom, int newtailroom, gfp_t gfp_mask);</code></pre>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>buffer to copy</dl>
<p> <i>newheadroom</i></p>
<dl>
<dd>new free bytes at head</dl>
<p> <i>newtailroom</i></p>
<dl>
<dd>new free bytes at tail</dl>
<p> <i>gfp_mask</i></p>
<dl>
<dd>allocation priority</dl>
<h2>Description</h2>
<p>Make a copy of both an sk_buff and its data and while doing so allocate additional space. </p>
<p> This is used when the caller wishes to modify the data and needs a private copy of the data to alter as well as more space for new fields. Returns <code>NULL</code> on failure or the pointer to the buffer on success. The returned buffer has a reference count of 1. </p>
<p> You must pass <code>GFP_ATOMIC</code> as the allocation priority if this function is called from an interrupt.</p>
<h2>Copyright</h2>
