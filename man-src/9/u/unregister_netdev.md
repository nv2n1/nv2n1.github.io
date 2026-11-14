---
title: "unregister_netdev(9)"
name: "unregister_netdev"
section: "9"
letter: "u"
url: "/docs/linux/man/9-unregister_netdev/"
---

unregister_netdev - remove device from the kernel

<h2>Synopsis</h2>

<pre><code>void unregister_netdev(struct net_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>

<h2>Description</h2>

This function shuts down a device interface and removes it from the kernel tables. 

 This is just a wrapper for unregister_netdevice that takes the rtnl semaphore. In general you want to use this and not unregister_netdevice.

<h2>Copyright</h2>


