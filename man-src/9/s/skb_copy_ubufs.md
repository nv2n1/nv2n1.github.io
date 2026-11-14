---
title: "skb_copy_ubufs(9)"
name: "skb_copy_ubufs"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_copy_ubufs/"
description: "skb_copy_ubufs – copy userspace skb frags buffers to kernel"
---

<p>skb_copy_ubufs &#8211; copy userspace skb frags buffers to kernel</p>
<h2>Synopsis</h2>
<pre><code>int skb_copy_ubufs(struct sk_buff *skb, gfp_t gfp_mask);</code></pre>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>the skb to modify</dl>
<p> <i>gfp_mask</i></p>
<dl>
<dd>allocation priority</dl>
<h2>Description</h2>
<p>This must be called on SKBTX_DEV_ZEROCOPY skb. It will copy all frags into kernel and drop the reference to userspace pages. </p>
<p> If this function is called from an interrupt <code>gfp_mask</code> must be <code>GFP_ATOMIC</code>. </p>
<p> Returns 0 on success or a negative error code on failure to allocate kernel memory to copy to.</p>
<h2>Copyright</h2>
