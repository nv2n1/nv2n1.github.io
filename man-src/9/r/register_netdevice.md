---
title: "register_netdevice(9)"
name: "register_netdevice"
section: "9"
letter: "r"
url: "/docs/linux/man/9-register_netdevice/"
description: "register_netdevice – register a network device"
---

<p>register_netdevice &#8211; register a network device</p>
<h2>Synopsis</h2>
<pre><code>int register_netdevice(struct net_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device to register</dl>
<h2>Description</h2>
<p>Take a completed network device structure and add it to the kernel interfaces. A <code>NETDEV_REGISTER</code> message is sent to the netdev notifier chain. 0 is returned on success. A negative errno code is returned on a failure to set up the device, or if the name is a duplicate. </p>
<p> Callers must hold the rtnl semaphore. You may want <code>register_netdev</code> instead of this. </p>
<p> BUGS: The locking appears insufficient to guarantee two parallel registers will not get the same name.</p>
<h2>Copyright</h2>
