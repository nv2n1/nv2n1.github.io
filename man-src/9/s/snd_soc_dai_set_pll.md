---
title: "snd_soc_dai_set_pll(9)"
name: "snd_soc_dai_set_pll"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dai_set_pll/"
---

snd_soc_dai_set_pll - configure DAI PLL.

<h2>Synopsis</h2>

<pre><code>int snd_soc_dai_set_pll(struct snd_soc_dai *dai, int pll_id, int source, unsigned int freq_in, unsigned int freq_out);</code></pre>

<h2>Arguments</h2>

<i>dai</i>
<dl><dd><dd>DAI</dl>
 

 <i>pll_id</i>
<dl><dd>DAI specific PLL ID</dl>
 

 <i>source</i>
<dl><dd>DAI specific source for the PLL</dl>
 

 <i>freq_in</i>
<dl><dd>PLL input clock frequency in Hz</dl>
 

 <i>freq_out</i>
<dl><dd>requested PLL output clock frequency in Hz</dl>

<h2>Description</h2>

Configures and enables PLL to generate output clock based on input clock.

<h2>Copyright</h2>


