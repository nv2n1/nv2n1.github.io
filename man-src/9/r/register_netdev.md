---
title: "register_netdev(9)"
name: "register_netdev"
section: "9"
letter: "r"
url: "/docs/linux/man/9-register_netdev/"
description: "register_netdev – register a network device"
---

<p>register_netdev &#8211; register a network device</p>
<h2>Synopsis</h2>
<pre><code>int register_netdev(struct net_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device to register</dl>
<h2>Description</h2>
<p>Take a completed network device structure and add it to the kernel interfaces. A <code>NETDEV_REGISTER</code> message is sent to the netdev notifier chain. 0 is returned on success. A negative errno code is returned on a failure to set up the device, or if the name is a duplicate. </p>
<p> This is a wrapper around register_netdevice that takes the rtnl semaphore and expands the device name if you passed a format string to alloc_netdev.</p>
<h2>Copyright</h2>
