---
title: "snd_soc_dai_set_bclk_ratio(9)"
name: "snd_soc_dai_set_bclk_ratio"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dai_set_bclk_ratio/"
---

snd_soc_dai_set_bclk_ratio - configure BCLK to sample rate ratio.

<h2>Synopsis</h2>

<pre><code>int snd_soc_dai_set_bclk_ratio(struct snd_soc_dai *dai, unsigned int ratio);</code></pre>

<h2>Arguments</h2>

<i>dai</i>
<dl><dd><dd>DAI</dl>
 

 <i>ratio</i>
<dl><dd>Ratio of BCLK to Sample rate.</dl>

<h2>Description</h2>

Configures the DAI for a preset BCLK to sample rate ratio.

<h2>Copyright</h2>


