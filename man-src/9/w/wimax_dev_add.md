---
title: "wimax_dev_add(9)"
name: "wimax_dev_add"
section: "9"
letter: "w"
url: "/docs/linux/man/9-wimax_dev_add/"
description: "wimax_dev_add – Register a new WiMAX device"
---

<p>wimax_dev_add &#8211; Register a new WiMAX device</p>
<h2>Synopsis</h2>
<pre><code>int wimax_dev_add(struct wimax_dev *wimax_dev, struct net_device *net_dev);</code></pre>
<h2>Arguments</h2>
<p><i>wimax_dev</i></p>
<dl>
<dd>
<dd>WiMAX device descriptor (as embedded in your <i>net_dev</i>&#8216;s priv data). You must have called <code>wimax_dev_init</code> on it before.</dl>
<p> <i>net_dev</i></p>
<dl>
<dd>net device the <i>wimax_dev</i> is associated with. The function expects <code>SET_NETDEV_DEV</code> and <code>register_netdev</code> were already called on it.</dl>
<h2>Description</h2>
<p>Registers the new WiMAX device, sets up the user-kernel control interface (generic netlink) and common WiMAX infrastructure. </p>
<p> Note that the parts that will allow interaction with user space are setup at the very end, when the rest is in place, as once that happens, the driver might get user space control requests via netlink or from debugfs that might translate into calls into wimax_dev-&gt;op_*().</p>
<h2>Copyright</h2>
