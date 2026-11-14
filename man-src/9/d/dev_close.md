---
title: "dev_close(9)"
name: "dev_close"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_close/"
description: "dev_close – shutdown an interface."
---

<p>dev_close &#8211; shutdown an interface.</p>
<h2>Synopsis</h2>
<pre><code>int dev_close(struct net_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device to shutdown</dl>
<h2>Description</h2>
<p>This function moves an active device into down state. A <code>NETDEV_GOING_DOWN</code> is sent to the netdev notifier chain. The device is then deactivated and finally a <code>NETDEV_DOWN</code> is sent to the notifier chain.</p>
<h2>Copyright</h2>
