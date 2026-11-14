---
title: "netif_device_detach(9)"
name: "netif_device_detach"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netif_device_detach/"
---

netif_device_detach - mark device as removed

<h2>Synopsis</h2>

<pre><code>void netif_device_detach(struct net_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>network device</dl>

<h2>Description</h2>

Mark device as removed from system and therefore no longer available.

<h2>Copyright</h2>


