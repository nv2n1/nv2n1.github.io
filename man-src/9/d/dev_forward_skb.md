---
title: "dev_forward_skb(9)"
name: "dev_forward_skb"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_forward_skb/"
---

dev_forward_skb - loopback an skb to another netif

<h2>Synopsis</h2>

<pre><code>int dev_forward_skb(struct net_device *dev, struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>destination network device</dl>
 

 <i>skb</i>
<dl><dd>buffer to forward</dl>

<h2>Description</h2>

return values: NET_RX_SUCCESS (no congestion) NET_RX_DROP (packet was dropped, but freed) 

 dev_forward_skb can be used for injecting an skb from the start_xmit function of one device into the receive queue of another device. 

 The receiving device may be in another namespace, so we have to clear all information in the skb that could impact namespace isolation.

<h2>Copyright</h2>


