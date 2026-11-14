---
title: "unregister_netdevice_queue(9)"
name: "unregister_netdevice_queue"
section: "9"
letter: "u"
url: "/docs/linux/man/9-unregister_netdevice_queue/"
description: "unregister_netdevice_queue – remove device from the kernel"
---

<p>unregister_netdevice_queue &#8211; remove device from the kernel</p>
<h2>Synopsis</h2>
<pre><code>void unregister_netdevice_queue(struct net_device *dev, struct list_head *head);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device</dl>
<p> <i>head</i></p>
<dl>
<dd>list</dl>
<h2>Description</h2>
<p>This function shuts down a device interface and removes it from the kernel tables. If head not NULL, device is queued to be unregistered later. </p>
<p> Callers must hold the rtnl semaphore. You may want <code>unregister_netdev</code> instead of this.</p>
<h2>Copyright</h2>
