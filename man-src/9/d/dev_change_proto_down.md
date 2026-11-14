---
title: "dev_change_proto_down(9)"
name: "dev_change_proto_down"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_change_proto_down/"
---

dev_change_proto_down - update protocol port state information

<h2>Synopsis</h2>

<pre><code>int dev_change_proto_down(struct net_device *dev, bool proto_down);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>
 

 <i>proto_down</i>
<dl><dd>new value</dl>

<h2>Description</h2>

This info can be used by switch drivers to set the phys state of the port.

<h2>Copyright</h2>


