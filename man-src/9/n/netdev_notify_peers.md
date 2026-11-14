---
title: "netdev_notify_peers(9)"
name: "netdev_notify_peers"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_notify_peers/"
---

netdev_notify_peers - notify network peers about existence of <i>dev</i>

<h2>Synopsis</h2>

<pre><code>void netdev_notify_peers(struct net_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>network device</dl>

<h2>Description</h2>

Generate traffic such that interested network peers are aware of <i>dev</i>, such as by generating a gratuitous ARP. This may be used when a device wants to inform the rest of the network about some sort of reconfiguration such as a failover event or virtual machine migration.

<h2>Copyright</h2>


