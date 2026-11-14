---
title: "dev_getbyhwaddr_rcu(9)"
name: "dev_getbyhwaddr_rcu"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_getbyhwaddr_rcu/"
---

dev_getbyhwaddr_rcu - find a device by its hardware address

<h2>Synopsis</h2>

<pre><code>struct net_device *dev_getbyhwaddr_rcu(struct net *net, unsigned short type, const char *ha);</code></pre>

<h2>Arguments</h2>

<i>net</i>
<dl><dd><dd>the applicable net namespace</dl>
 

 <i>type</i>
<dl><dd>media type of device</dl>
 

 <i>ha</i>
<dl><dd>hardware address</dl>

<h2>Description</h2>

Search for an interface by MAC address. Returns NULL if the device is not found or a pointer to the device. The caller must hold RCU or RTNL. The returned device has not had its ref count increased and the caller must therefore be careful about locking

<h2>Copyright</h2>


