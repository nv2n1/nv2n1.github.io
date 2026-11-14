---
title: "snd_soc_dai_set_clkdiv(9)"
name: "snd_soc_dai_set_clkdiv"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dai_set_clkdiv/"
---

snd_soc_dai_set_clkdiv - configure DAI clock dividers.

<h2>Synopsis</h2>

<pre><code>int snd_soc_dai_set_clkdiv(struct snd_soc_dai *dai, int div_id, int div);</code></pre>

<h2>Arguments</h2>

<i>dai</i>
<dl><dd><dd>DAI</dl>
 

 <i>div_id</i>
<dl><dd>DAI specific clock divider ID</dl>
 

 <i>div</i>
<dl><dd>new clock divisor.</dl>

<h2>Description</h2>

Configures the clock dividers. This is used to derive the best DAI bit and frame clocks from the system or master clock. It's best to set the DAI bit and frame clocks as low as possible to save system power.

<h2>Copyright</h2>


