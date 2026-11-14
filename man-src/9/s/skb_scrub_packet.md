---
title: "skb_scrub_packet(9)"
name: "skb_scrub_packet"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_scrub_packet/"
---

skb_scrub_packet - scrub an skb

<h2>Synopsis</h2>

<pre><code>void skb_scrub_packet(struct sk_buff *skb, bool xnet);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to clean</dl>
 

 <i>xnet</i>
<dl><dd>packet is crossing netns</dl>

<h2>Description</h2>

skb_scrub_packet can be used after encapsulating or decapsulting a packet into/from a tunnel. Some information have to be cleared during these operations. skb_scrub_packet can also be used to clean a skb before injecting it in another namespace (<i>xnet</i> == true). We have to clear all information in the skb that could impact namespace isolation.

<h2>Copyright</h2>


