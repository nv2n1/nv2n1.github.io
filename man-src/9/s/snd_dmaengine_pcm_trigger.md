---
title: "snd_dmaengine_pcm_trigger(9)"
name: "snd_dmaengine_pcm_trigger"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_dmaengine_pcm_trigger/"
---

snd_dmaengine_pcm_trigger - dmaengine based PCM trigger implementation

<h2>Synopsis</h2>

<pre><code>int snd_dmaengine_pcm_trigger(struct snd_pcm_substream *substream, int cmd);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>PCM substream</dl>
 

 <i>cmd</i>
<dl><dd>Trigger command</dl>

<h2>Description</h2>

Returns 0 on success, a negative error code otherwise. 

 This function can be used as the PCM trigger callback for dmaengine based PCM driver implementations.

<h2>Copyright</h2>


