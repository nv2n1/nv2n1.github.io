---
title: "init_dummy_netdev(9)"
name: "init_dummy_netdev"
section: "9"
letter: "i"
url: "/docs/linux/man/9-init_dummy_netdev/"
---

init_dummy_netdev - init a dummy network device for NAPI

<h2>Synopsis</h2>

<pre><code>int init_dummy_netdev(struct net_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device to init</dl>

<h2>Description</h2>

This takes a network device structure and initialize the minimum amount of fields so it can be used to schedule NAPI polls without registering a full blown interface. This is to be used by drivers that need to tie several hardware interfaces to a single NAPI poll scheduler due to HW limitations.

<h2>Copyright</h2>


