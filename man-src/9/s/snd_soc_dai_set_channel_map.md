---
title: "snd_soc_dai_set_channel_map(9)"
name: "snd_soc_dai_set_channel_map"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dai_set_channel_map/"
---

snd_soc_dai_set_channel_map - configure DAI audio channel map

<h2>Synopsis</h2>

<pre><code>int snd_soc_dai_set_channel_map(struct snd_soc_dai *dai, unsigned int tx_num, unsigned int *tx_slot, unsigned int rx_num, unsigned int *rx_slot);</code></pre>

<h2>Arguments</h2>

<i>dai</i>
<dl><dd><dd>DAI</dl>
 

 <i>tx_num</i>
<dl><dd>how many TX channels</dl>
 

 <i>tx_slot</i>
<dl><dd>pointer to an array which imply the TX slot number channel 0~num-1 uses</dl>
 

 <i>rx_num</i>
<dl><dd>how many RX channels</dl>
 

 <i>rx_slot</i>
<dl><dd>pointer to an array which imply the RX slot number channel 0~num-1 uses</dl>

<h2>Description</h2>

configure the relationship between channel number and TDM slot number.

<h2>Copyright</h2>


