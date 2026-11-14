---
title: "devm_snd_soc_register_platform(9)"
name: "devm_snd_soc_register_platform"
section: "9"
letter: "d"
url: "/docs/linux/man/9-devm_snd_soc_register_platform/"
---

devm_snd_soc_register_platform - resource managed platform registration

<h2>Synopsis</h2>

<pre><code>int devm_snd_soc_register_platform(struct device *dev, const struct snd_soc_platform_driver *platform_drv);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>Device used to manage platform</dl>
 

 <i>platform_drv</i>
<dl><dd>platform to register</dl>

<h2>Description</h2>

Register a platform driver with automatic unregistration when the device is unregistered.

<h2>Copyright</h2>


