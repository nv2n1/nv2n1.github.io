---
title: "snd_soc_dai_set_fmt(9)"
name: "snd_soc_dai_set_fmt"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dai_set_fmt/"
---

snd_soc_dai_set_fmt - configure DAI hardware audio format.

<h2>Synopsis</h2>

<pre><code>int snd_soc_dai_set_fmt(struct snd_soc_dai *dai, unsigned int fmt);</code></pre>

<h2>Arguments</h2>

<i>dai</i>
<dl><dd><dd>DAI</dl>
 

 <i>fmt</i>
<dl><dd>SND_SOC_DAIFMT_ format value.</dl>

<h2>Description</h2>

Configures the DAI hardware format and clocking.

<h2>Copyright</h2>


