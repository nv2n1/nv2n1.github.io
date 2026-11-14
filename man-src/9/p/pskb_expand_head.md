---
title: "pskb_expand_head(9)"
name: "pskb_expand_head"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pskb_expand_head/"
---

pskb_expand_head - reallocate header of sk_buff

<h2>Synopsis</h2>

<pre><code>int pskb_expand_head(struct sk_buff *skb, int nhead, int ntail, gfp_t gfp_mask);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to reallocate</dl>
 

 <i>nhead</i>
<dl><dd>room to add at head</dl>
 

 <i>ntail</i>
<dl><dd>room to add at tail</dl>
 

 <i>gfp_mask</i>
<dl><dd>allocation priority</dl>

<h2>Description</h2>

Expands (or creates identical copy, if <i>nhead</i> and <i>ntail</i> are zero) header of <i>skb</i>. sk_buff itself is not changed. sk_buff MUST have reference count of 1. Returns zero in the case of success or error, if expansion failed. In the last case, sk_buff is not changed. 

 All the pointers pointing into skb header may change and must be reloaded after call to this function.

<h2>Copyright</h2>


