---
title: "dev_get_phys_port_name(9)"
name: "dev_get_phys_port_name"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_get_phys_port_name/"
---

dev_get_phys_port_name - Get device physical port name

<h2>Synopsis</h2>

<pre><code>int dev_get_phys_port_name(struct net_device *dev, char *name, size_t len);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>
 

 <i>name</i>
<dl><dd>port name</dl>
 

 <i>len</i>
<dl><dd>limit of bytes to copy to name</dl>

<h2>Description</h2>

Get device physical port name

<h2>Copyright</h2>


