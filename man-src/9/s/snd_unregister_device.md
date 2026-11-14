---
title: "snd_unregister_device(9)"
name: "snd_unregister_device"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_unregister_device/"
description: "snd_unregister_device – unregister the device on the given card"
---

<p>snd_unregister_device &#8211; unregister the device on the given card</p>
<h2>Synopsis</h2>
<pre><code>int snd_unregister_device(struct device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the device instance</dl>
<h2>Description</h2>
<p>Unregisters the device file already registered via <code>snd_register_device</code>.</p>
<h2>Return</h2>
<p>Zero if successful, or a negative error code on failure.</p>
<h2>Copyright</h2>
