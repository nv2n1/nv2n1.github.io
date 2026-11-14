---
title: "netdev_alloc_skb(9)"
name: "netdev_alloc_skb"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_alloc_skb/"
description: "netdev_alloc_skb – allocate an skbuff for rx on a specific device"
---

<p>netdev_alloc_skb &#8211; allocate an skbuff for rx on a specific device</p>
<h2>Synopsis</h2>
<pre><code>struct sk_buff *netdev_alloc_skb(struct net_device *dev, unsigned int length);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>network device to receive on</dl>
<p> <i>length</i></p>
<dl>
<dd>length to allocate</dl>
<h2>Description</h2>
<p>Allocate a new sk_buff and assign it a usage count of one. The buffer has unspecified headroom built in. Users should allocate the headroom they think they need without accounting for the built in space. The built in space is used for optimisations. </p>
<p> <code>NULL</code> is returned if there is no free memory. Although this function allocates memory it can be called from an interrupt.</p>
<h2>Copyright</h2>
