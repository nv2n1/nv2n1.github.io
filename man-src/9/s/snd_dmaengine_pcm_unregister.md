---
title: "snd_dmaengine_pcm_unregister(9)"
name: "snd_dmaengine_pcm_unregister"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_dmaengine_pcm_unregister/"
---

snd_dmaengine_pcm_unregister - Removes a dmaengine based PCM device

<h2>Synopsis</h2>

<pre><code>void snd_dmaengine_pcm_unregister(struct device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>Parent device the PCM was register with</dl>

<h2>Description</h2>

Removes a dmaengine based PCM device previously registered with snd_dmaengine_pcm_register.

<h2>Copyright</h2>


