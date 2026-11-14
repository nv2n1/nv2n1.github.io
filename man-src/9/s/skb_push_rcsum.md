---
title: "skb_push_rcsum(9)"
name: "skb_push_rcsum"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_push_rcsum/"
---

skb_push_rcsum - push skb and update receive checksum

<h2>Synopsis</h2>

<pre><code>unsigned char *skb_push_rcsum(struct sk_buff *skb, unsigned int len);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to update</dl>
 

 <i>len</i>
<dl><dd>length of data pulled</dl>

<h2>Description</h2>

This function performs an skb_push on the packet and updates the CHECKSUM_COMPLETE checksum. It should be used on receive path processing instead of skb_push unless you know that the checksum difference is zero (e.g., a valid IP header) or you are setting ip_summed to CHECKSUM_NONE.

<h2>Copyright</h2>


