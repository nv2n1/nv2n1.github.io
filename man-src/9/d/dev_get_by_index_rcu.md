---
title: "dev_get_by_index_rcu(9)"
name: "dev_get_by_index_rcu"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_get_by_index_rcu/"
description: "dev_get_by_index_rcu – find a device by its ifindex"
---

<p>dev_get_by_index_rcu &#8211; find a device by its ifindex</p>
<h2>Synopsis</h2>
<pre><code>struct net_device *dev_get_by_index_rcu(struct net *net, int ifindex);</code></pre>
<h2>Arguments</h2>
<p><i>net</i></p>
<dl>
<dd>
<dd>the applicable net namespace</dl>
<p> <i>ifindex</i></p>
<dl>
<dd>index of device</dl>
<h2>Description</h2>
<p>Search for an interface by index. Returns <code>NULL</code> if the device is not found or a pointer to the device. The device has not had its reference counter increased so the caller must be careful about locking. The caller must hold RCU lock.</p>
<h2>Copyright</h2>
