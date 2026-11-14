---
title: "netif_rx(9)"
name: "netif_rx"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netif_rx/"
---

netif_rx - post buffer to the network code

<h2>Synopsis</h2>

<pre><code>int netif_rx(struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to post</dl>

<h2>Description</h2>

This function receives a packet from a device driver and queues it for the upper (protocol) levels to process. It always succeeds. The buffer may be dropped during processing for congestion control or by the protocol layers. 

 return values: NET_RX_SUCCESS (no congestion) NET_RX_DROP (packet was dropped)

<h2>Copyright</h2>


