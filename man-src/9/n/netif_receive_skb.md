---
title: "netif_receive_skb(9)"
name: "netif_receive_skb"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netif_receive_skb/"
description: "netif_receive_skb – process receive buffer from network"
---

<p>netif_receive_skb &#8211; process receive buffer from network</p>
<h2>Synopsis</h2>
<pre><code>int netif_receive_skb(struct sk_buff *skb);</code></pre>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>buffer to process</dl>
<h2>Description</h2>
<p><code>netif_receive_skb</code> is the main receive data processing function. It always succeeds. The buffer may be dropped during processing for congestion control or by the protocol layers. </p>
<p> This function may only be called from softirq context and interrupts should be enabled. </p>
<p> Return values (usually ignored): NET_RX_SUCCESS: no congestion NET_RX_DROP: packet was dropped</p>
<h2>Copyright</h2>
