---
title: "register_netdevice_notifier(9)"
name: "register_netdevice_notifier"
section: "9"
letter: "r"
url: "/docs/linux/man/9-register_netdevice_notifier/"
---

register_netdevice_notifier - register a network notifier block

<h2>Synopsis</h2>

<pre><code>int register_netdevice_notifier(struct notifier_block *nb);</code></pre>

<h2>Arguments</h2>

<i>nb</i>
<dl><dd><dd>notifier</dl>

<h2>Description</h2>

Register a notifier to be called when network device events occur. The notifier passed is linked into the kernel structures and must not be reused until it has been unregistered. A negative errno code is returned on a failure. 

 When registered all registration and up events are replayed to the new notifier to allow device to have a race free view of the network device list.

<h2>Copyright</h2>


