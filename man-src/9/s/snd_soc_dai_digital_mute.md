---
title: "snd_soc_dai_digital_mute(9)"
name: "snd_soc_dai_digital_mute"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dai_digital_mute/"
---

snd_soc_dai_digital_mute - configure DAI system or master clock.

<h2>Synopsis</h2>

<pre><code>int snd_soc_dai_digital_mute(struct snd_soc_dai *dai, int mute, int direction);</code></pre>

<h2>Arguments</h2>

<i>dai</i>
<dl><dd><dd>DAI</dl>
 

 <i>mute</i>
<dl><dd>mute enable</dl>
 

 <i>direction</i>
<dl><dd>stream to mute</dl>

<h2>Description</h2>

Mutes the DAI DAC.

<h2>Copyright</h2>


