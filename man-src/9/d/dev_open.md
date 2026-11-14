---
title: "dev_open(9)"
name: "dev_open"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_open/"
description: "dev_open – prepare an interface for use."
---

<p>dev_open &#8211; prepare an interface for use.</p>
<h2>Synopsis</h2>
<pre><code>int dev_open(struct net_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device to open</dl>
<h2>Description</h2>
<p>Takes a device from down to up state. The device&#8217;s private open function is invoked and then the multicast lists are loaded. Finally the device is moved into the up state and a <code>NETDEV_UP</code> message is sent to the netdev notifier chain. </p>
<p> Calling this function on an active interface is a nop. On a failure a negative errno code is returned.</p>
<h2>Copyright</h2>
