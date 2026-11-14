---
title: "netif_queue_stopped(9)"
name: "netif_queue_stopped"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netif_queue_stopped/"
description: "netif_queue_stopped – test if transmit queue is flowblocked"
---

<p>netif_queue_stopped &#8211; test if transmit queue is flowblocked</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool netif_queue_stopped(const struct net_device&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>network device</dl>
<h2>Description</h2>
<p>Test if transmit queue on device is currently unable to send.</p>
<h2>Copyright</h2>
