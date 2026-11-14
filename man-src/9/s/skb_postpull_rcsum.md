---
title: "skb_postpull_rcsum(9)"
name: "skb_postpull_rcsum"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_postpull_rcsum/"
---

skb_postpull_rcsum - update checksum for received skb after pull

<h2>Synopsis</h2>

<pre><code>void skb_postpull_rcsum(struct sk_buff *skb, const void *start, unsigned int len);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to update</dl>
 

 <i>start</i>
<dl><dd>start of data before pull</dl>
 

 <i>len</i>
<dl><dd>length of data pulled</dl>

<h2>Description</h2>

After doing a pull on a received packet, you need to call this to update the CHECKSUM_COMPLETE checksum, or set ip_summed to CHECKSUM_NONE so that it can be recomputed from scratch.

<h2>Copyright</h2>


