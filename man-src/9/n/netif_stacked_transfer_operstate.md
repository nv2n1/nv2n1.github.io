---
title: "netif_stacked_transfer_operstate(9)"
name: "netif_stacked_transfer_operstate"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netif_stacked_transfer_operstate/"
---

netif_stacked_transfer_operstate - transfer operstate

<h2>Synopsis</h2>

<pre><code>void netif_stacked_transfer_operstate(const struct net_device *rootdev, struct net_device *dev);</code></pre>

<h2>Arguments</h2>

<i>rootdev</i>
<dl><dd><dd>the root or lower level device to transfer state from</dl>
 

 <i>dev</i>
<dl><dd>the device to transfer operstate to</dl>

<h2>Description</h2>

Transfer operational state from root to device. This is normally called when a stacking relationship exists between the root device and the device(a leaf device).

<h2>Copyright</h2>


