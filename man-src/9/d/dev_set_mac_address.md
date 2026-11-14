---
title: "dev_set_mac_address(9)"
name: "dev_set_mac_address"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_set_mac_address/"
---

dev_set_mac_address - Change Media Access Control Address

<h2>Synopsis</h2>

<pre><code>int dev_set_mac_address(struct net_device *dev, struct sockaddr *sa);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>
 

 <i>sa</i>
<dl><dd>new address</dl>

<h2>Description</h2>

Change the hardware (MAC) address of the device

<h2>Copyright</h2>


