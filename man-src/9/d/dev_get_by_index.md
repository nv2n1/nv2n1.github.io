---
title: "dev_get_by_index(9)"
name: "dev_get_by_index"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_get_by_index/"
---

dev_get_by_index - find a device by its ifindex

<h2>Synopsis</h2>

<pre><code>struct net_device *dev_get_by_index(struct net *net, int ifindex);</code></pre>

<h2>Arguments</h2>

<i>net</i>
<dl><dd><dd>the applicable net namespace</dl>
 

 <i>ifindex</i>
<dl><dd>index of device</dl>

<h2>Description</h2>

Search for an interface by index. Returns NULL if the device is not found or a pointer to the device. The device returned has had a reference added and the pointer is safe until the user calls dev_put to indicate they have finished with it.

<h2>Copyright</h2>


