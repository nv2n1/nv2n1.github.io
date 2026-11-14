---
title: "skb_postpush_rcsum(9)"
name: "skb_postpush_rcsum"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_postpush_rcsum/"
---

skb_postpush_rcsum - update checksum for received skb after push

<h2>Synopsis</h2>

<pre><code>void skb_postpush_rcsum(struct sk_buff *skb, const void *start, unsigned int len);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to update</dl>
 

 <i>start</i>
<dl><dd>start of data after push</dl>
 

 <i>len</i>
<dl><dd>length of data pushed</dl>

<h2>Description</h2>

After doing a push on a received packet, you need to call this to update the CHECKSUM_COMPLETE checksum.

<h2>Copyright</h2>


