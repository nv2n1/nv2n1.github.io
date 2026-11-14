---
title: "netdev_boot_setup_check(9)"
name: "netdev_boot_setup_check"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_boot_setup_check/"
---

netdev_boot_setup_check - check boot time settings

<h2>Synopsis</h2>

<pre><code>int netdev_boot_setup_check(struct net_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>the netdevice</dl>

<h2>Description</h2>

Check boot time settings for the device. The found settings are set for the device to be used later in the device probing. Returns 0 if no settings found, 1 if they are.

<h2>Copyright</h2>


