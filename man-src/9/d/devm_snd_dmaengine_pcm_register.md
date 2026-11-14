---
title: "devm_snd_dmaengine_pcm_register(9)"
name: "devm_snd_dmaengine_pcm_register"
section: "9"
letter: "d"
url: "/docs/linux/man/9-devm_snd_dmaengine_pcm_register/"
---

devm_snd_dmaengine_pcm_register - resource managed dmaengine PCM registration

<h2>Synopsis</h2>

<pre><code>int devm_snd_dmaengine_pcm_register(struct device *dev, const struct snd_dmaengine_pcm_config *config, unsigned int flags);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>The parent device for the PCM device</dl>
 

 <i>config</i>
<dl><dd>Platform specific PCM configuration</dl>
 

 <i>flags</i>
<dl><dd>Platform specific quirks</dl>

<h2>Description</h2>

Register a dmaengine based PCM device with automatic unregistration when the device is unregistered.

<h2>Copyright</h2>


