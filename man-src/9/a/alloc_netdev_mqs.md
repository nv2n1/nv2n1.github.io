---
title: "alloc_netdev_mqs(9)"
name: "alloc_netdev_mqs"
section: "9"
letter: "a"
url: "/docs/linux/man/9-alloc_netdev_mqs/"
---

alloc_netdev_mqs - allocate network device

<h2>Synopsis</h2>

<pre><code>struct net_device *alloc_netdev_mqs(int sizeof_priv, const char *name, unsigned char name_assign_type, void (*setup)(struct net_device *), unsigned int txqs, unsigned int rxqs);</code></pre>

<h2>Arguments</h2>

<i>sizeof_priv</i>
<dl><dd><dd>size of private data to allocate space for</dl>
 

 <i>name</i>
<dl><dd>device name format string</dl>
 

 <i>name_assign_type</i>
<dl><dd>origin of device name</dl>
 

 <i>setup</i>
<dl><dd>callback to initialize device</dl>
 

 <i>txqs</i>
<dl><dd>the number of TX subqueues to allocate</dl>
 

 <i>rxqs</i>
<dl><dd>the number of RX subqueues to allocate</dl>

<h2>Description</h2>

Allocates a struct net_device with private data area for driver use and performs basic initialization. Also allocates subqueue structs for each queue on the device.

<h2>Copyright</h2>


