---
title: "snd_dmaengine_pcm_register(9)"
name: "snd_dmaengine_pcm_register"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_dmaengine_pcm_register/"
---

snd_dmaengine_pcm_register - Register a dmaengine based PCM device

<h2>Synopsis</h2>

<pre><code>int snd_dmaengine_pcm_register(struct device *dev, const struct snd_dmaengine_pcm_config *config, unsigned int flags);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>The parent device for the PCM device</dl>
 

 <i>config</i>
<dl><dd>Platform specific PCM configuration</dl>
 

 <i>flags</i>
<dl><dd>Platform specific quirks</dl>

<h2>Copyright</h2>


