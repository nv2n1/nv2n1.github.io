---
title: "netdev_state_change(9)"
name: "netdev_state_change"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_state_change/"
---

netdev_state_change - device changes state

<h2>Synopsis</h2>

<pre><code>void netdev_state_change(struct net_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device to cause notification</dl>

<h2>Description</h2>

Called to indicate a device has changed state. This function calls the notifier chains for netdev_chain and sends a NEWLINK message to the routing socket.

<h2>Copyright</h2>


