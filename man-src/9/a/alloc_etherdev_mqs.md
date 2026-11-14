---
title: "alloc_etherdev_mqs(9)"
name: "alloc_etherdev_mqs"
section: "9"
letter: "a"
url: "/docs/linux/man/9-alloc_etherdev_mqs/"
---

alloc_etherdev_mqs - Allocates and sets up an Ethernet device

<h2>Synopsis</h2>

<pre><code>struct net_device *alloc_etherdev_mqs(int sizeof_priv, unsigned int txqs, unsigned int rxqs);</code></pre>

<h2>Arguments</h2>

<i>sizeof_priv</i>
<dl><dd><dd>Size of additional driver-private structure to be allocated for this Ethernet device</dl>
 

 <i>txqs</i>
<dl><dd>The number of TX queues this device has.</dl>
 

 <i>rxqs</i>
<dl><dd>The number of RX queues this device has.</dl>

<h2>Description</h2>

Fill in the fields of the device structure with Ethernet-generic values. Basically does everything except registering the device. 

 Constructs a new net device, complete with a private data area of size (sizeof_priv). A 32-byte (not bit) alignment is enforced for this private data area.

<h2>Copyright</h2>


