---
title: "snd_soc_runtime_set_dai_fmt(9)"
name: "snd_soc_runtime_set_dai_fmt"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_runtime_set_dai_fmt/"
---

snd_soc_runtime_set_dai_fmt - Change DAI link format for a ASoC runtime

<h2>Synopsis</h2>

<pre><code>int snd_soc_runtime_set_dai_fmt(struct snd_soc_pcm_runtime *rtd, unsigned int dai_fmt);</code></pre>

<h2>Arguments</h2>

<i>rtd</i>
<dl><dd><dd>The runtime for which the DAI link format should be changed</dl>
 

 <i>dai_fmt</i>
<dl><dd>The new DAI link format</dl>

<h2>Description</h2>

This function updates the DAI link format for all DAIs connected to the DAI link for the specified runtime.

<h2>Note</h2>

For setups with a static format set the dai_fmt field in the corresponding snd_dai_link struct instead of using this function. 

 Returns 0 on success, otherwise a negative error code.

<h2>Copyright</h2>


