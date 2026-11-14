---
title: "netdev_lower_state_changed(9)"
name: "netdev_lower_state_changed"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_lower_state_changed/"
---

netdev_lower_state_changed - Dispatch event about lower device state change

<h2>Synopsis</h2>

<pre><code>void netdev_lower_state_changed(struct net_device *lower_dev, void *lower_state_info);</code></pre>

<h2>Arguments</h2>

<i>lower_dev</i>
<dl><dd><dd>device</dl>
 

 <i>lower_state_info</i>
<dl><dd>state to dispatch</dl>

<h2>Description</h2>

Send NETDEV_CHANGELOWERSTATE to netdev notifiers with info. The caller must hold the RTNL lock.

<h2>Copyright</h2>


