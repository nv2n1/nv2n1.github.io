---
title: "snd_soc_codec_set_sysclk(9)"
name: "snd_soc_codec_set_sysclk"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_codec_set_sysclk/"
---

snd_soc_codec_set_sysclk - configure CODEC system or master clock.

<h2>Synopsis</h2>

<pre><code>int snd_soc_codec_set_sysclk(struct snd_soc_codec *codec, int clk_id, int source, unsigned int freq, int dir);</code></pre>

<h2>Arguments</h2>

<i>codec</i>
<dl><dd></dd><dd>CODEC</dd></dl>
 

 <i>clk_id</i>
<dl><dd>DAI specific clock ID</dd></dl>
 

 <i>source</i>
<dl><dd>Source for the clock</dd></dl>
 

 <i>freq</i>
<dl><dd>new clock frequency in Hz</dd></dl>
 

 <i>dir</i>
<dl><dd>new clock direction - input/output.</dd></dl>

<h2>Description</h2>

Configures the CODEC master (MCLK) or system (SYSCLK) clocking.

<h2>Copyright</h2>


