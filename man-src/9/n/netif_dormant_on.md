---
title: "netif_dormant_on(9)"
name: "netif_dormant_on"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netif_dormant_on/"
---

netif_dormant_on - mark device as dormant.

<h2>Synopsis</h2>

<pre><code>void netif_dormant_on(struct net_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>network device</dl>

<h2>Description</h2>

Mark device as dormant (as per RFC2863). 

 The dormant state indicates that the relevant interface is not actually in a condition to pass packets (i.e., it is not 'up') but is in a "pending" state, waiting for some external event. For "on- demand" interfaces, this new state identifies the situation where the interface is waiting for events to place it in the up state.

<h2>Copyright</h2>


