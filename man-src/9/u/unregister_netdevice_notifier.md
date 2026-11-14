---
title: "unregister_netdevice_notifier(9)"
name: "unregister_netdevice_notifier"
section: "9"
letter: "u"
url: "/docs/linux/man/9-unregister_netdevice_notifier/"
description: "unregister_netdevice_notifier – unregister a network notifier block"
---

<p>unregister_netdevice_notifier &#8211; unregister a network notifier block</p>
<h2>Synopsis</h2>
<pre><code>int unregister_netdevice_notifier(struct notifier_block *nb);</code></pre>
<h2>Arguments</h2>
<p><i>nb</i></p>
<dl>
<dd>
<dd>notifier</dl>
<h2>Description</h2>
<p>Unregister a notifier previously registered by <code>register_netdevice_notifier</code>. The notifier is unlinked into the kernel structures and may then be reused. A negative errno code is returned on a failure. </p>
<p> After unregistering unregister and down device events are synthesized for all devices on the device list to the removed notifier to remove the need for special case cleanup code.</p>
<h2>Copyright</h2>
