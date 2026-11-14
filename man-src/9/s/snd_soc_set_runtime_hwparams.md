---
title: "snd_soc_set_runtime_hwparams(9)"
name: "snd_soc_set_runtime_hwparams"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_set_runtime_hwparams/"
---

snd_soc_set_runtime_hwparams - set the runtime hardware parameters

<h2>Synopsis</h2>

<pre><code>int snd_soc_set_runtime_hwparams(struct snd_pcm_substream *substream, const struct snd_pcm_hardware *hw);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>the pcm substream</dl>
 

 <i>hw</i>
<dl><dd>the hardware parameters</dl>

<h2>Description</h2>

Sets the substream runtime hardware parameters.

<h2>Copyright</h2>


