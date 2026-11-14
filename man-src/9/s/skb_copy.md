---
title: "skb_copy(9)"
name: "skb_copy"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_copy/"
description: "skb_copy – create private copy of an sk_buff"
---

<p>skb_copy &#8211; create private copy of an sk_buff</p>
<h2>Synopsis</h2>
<pre><code>struct sk_buff *skb_copy(const struct sk_buff *skb, gfp_t gfp_mask);</code></pre>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>buffer to copy</dl>
<p> <i>gfp_mask</i></p>
<dl>
<dd>allocation priority</dl>
<h2>Description</h2>
<p>Make a copy of both an sk_buff and its data. This is used when the caller wishes to modify the data and needs a private copy of the data to alter. Returns <code>NULL</code> on failure or the pointer to the buffer on success. The returned buffer has a reference count of 1. </p>
<p> As by-product this function converts non-linear sk_buff to linear one, so that sk_buff becomes completely private and caller is allowed to modify all the data of returned buffer. This means that this function is not recommended for use in circumstances when only header is going to be modified. Use <code>pskb_copy</code> instead.</p>
<h2>Copyright</h2>
