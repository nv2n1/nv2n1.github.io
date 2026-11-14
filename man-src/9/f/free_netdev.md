---
title: "free_netdev(9)"
name: "free_netdev"
section: "9"
letter: "f"
url: "/docs/linux/man/9-free_netdev/"
---

free_netdev - free network device

<h2>Synopsis</h2>

<pre><code>void free_netdev(struct net_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>

<h2>Description</h2>

This function does the last stage of destroying an allocated device interface. The reference to the device object is released. If this is the last reference then it will be freed. Must be called in process context.

<h2>Copyright</h2>


