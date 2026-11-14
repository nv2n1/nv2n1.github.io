---
title: "snd_soc_dai_set_tdm_slot(9)"
name: "snd_soc_dai_set_tdm_slot"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dai_set_tdm_slot/"
---

snd_soc_dai_set_tdm_slot - Configures a DAI for TDM operation

<h2>Synopsis</h2>

<pre><code>int snd_soc_dai_set_tdm_slot(struct snd_soc_dai *dai, unsigned int tx_mask, unsigned int rx_mask, int slots, int slot_width);</code></pre>

<h2>Arguments</h2>

<i>dai</i>
<dl><dd><dd>The DAI to configure</dl>
 

 <i>tx_mask</i>
<dl><dd>bitmask representing active TX slots.</dl>
 

 <i>rx_mask</i>
<dl><dd>bitmask representing active RX slots.</dl>
 

 <i>slots</i>
<dl><dd>Number of slots in use.</dl>
 

 <i>slot_width</i>
<dl><dd>Width in bits for each slot.</dl>

<h2>Description</h2>

This function configures the specified DAI for TDM operation. <i>slot</i> contains the total number of slots of the TDM stream and <i>slot_with</i> the width of each slot in bit clock cycles. <i>tx_mask</i> and <i>rx_mask</i> are bitmasks specifying the active slots of the TDM stream for the specified DAI, i.e. which slots the DAI should write to or read from. If a bit is set the corresponding slot is active, if a bit is cleared the corresponding slot is inactive. Bit 0 maps to the first slot, bit 1 to the second slot and so on. The first active slot maps to the first channel of the DAI, the second active slot to the second channel and so on. 

 TDM mode can be disabled by passing 0 for <i>slots</i>. In this case <i>tx_mask</i>, <i>rx_mask</i> and <i>slot_width</i> will be ignored. 

 Returns 0 on success, a negative error code otherwise.

<h2>Copyright</h2>


