---
title: "netif_is_multiqueue(9)"
name: "netif_is_multiqueue"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netif_is_multiqueue/"
description: "netif_is_multiqueue – test if device has multiple transmit queues"
---

<p>netif_is_multiqueue &#8211; test if device has multiple transmit queues</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool netif_is_multiqueue(const struct net_device&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>network device</dl>
<h2>Description</h2>
<p>Check if device has multiple transmit queues</p>
<h2>Copyright</h2>
