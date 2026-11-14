---
title: "eth_skb_pad(9)"
name: "eth_skb_pad"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eth_skb_pad/"
---

eth_skb_pad - Pad buffer to mininum number of octets for Ethernet frame

<h2>Synopsis</h2>

<pre><code>int eth_skb_pad(struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>Buffer to pad</dl>

<h2>Description</h2>

An Ethernet frame should have a minimum size of 60 bytes. This function takes short frames and pads them with zeros up to the 60 byte limit.

<h2>Copyright</h2>


