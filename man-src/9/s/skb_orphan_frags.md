---
title: "skb_orphan_frags(9)"
name: "skb_orphan_frags"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_orphan_frags/"
---

skb_orphan_frags - orphan the frags contained in a buffer

<h2>Synopsis</h2>

<pre><code>int skb_orphan_frags(struct sk_buff *skb, gfp_t gfp_mask);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to orphan frags from</dl>
 

 <i>gfp_mask</i>
<dl><dd>allocation mask for replacement pages</dl>

<h2>Description</h2>

For each frag in the SKB which needs a destructor (i.e. has an owner) create a copy of that frag and release the original page by calling the destructor.

<h2>Copyright</h2>


