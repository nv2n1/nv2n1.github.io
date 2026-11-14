---
title: "snd_soc_add_platform(9)"
name: "snd_soc_add_platform"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_add_platform/"
---

snd_soc_add_platform - Add a platform to the ASoC core

<h2>Synopsis</h2>

<pre><code>int snd_soc_add_platform(struct device *dev, struct snd_soc_platform *platform, const struct snd_soc_platform_driver *platform_drv);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>The parent device for the platform</dl>
 

 <i>platform</i>
<dl><dd>The platform to add</dl>
 

 <i>platform_drv</i>
<dl><dd>The driver for the platform</dl>

<h2>Copyright</h2>


