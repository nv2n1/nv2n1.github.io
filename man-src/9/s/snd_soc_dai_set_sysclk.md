---
title: "snd_soc_dai_set_sysclk(9)"
name: "snd_soc_dai_set_sysclk"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dai_set_sysclk/"
---

snd_soc_dai_set_sysclk - configure DAI system or master clock.

<h2>Synopsis</h2>

<pre><code>int snd_soc_dai_set_sysclk(struct snd_soc_dai *dai, int clk_id, unsigned int freq, int dir);</code></pre>

<h2>Arguments</h2>

<i>dai</i>
<dl><dd><dd>DAI</dl>
 

 <i>clk_id</i>
<dl><dd>DAI specific clock ID</dl>
 

 <i>freq</i>
<dl><dd>new clock frequency in Hz</dl>
 

 <i>dir</i>
<dl><dd>new clock direction - input/output.</dl>

<h2>Description</h2>

Configures the DAI master (MCLK) or system (SYSCLK) clocking.

<h2>Copyright</h2>


