---
title: "snd_soc_add_card_controls(9)"
name: "snd_soc_add_card_controls"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_add_card_controls/"
---

snd_soc_add_card_controls - add an array of controls to a SoC card. Convenience function to add a list of controls.

<h2>Synopsis</h2>

<pre><code>int snd_soc_add_card_controls(struct snd_soc_card *soc_card, const struct snd_kcontrol_new *controls, int num_controls);</code></pre>

<h2>Arguments</h2>

<i>soc_card</i>
<dl><dd><dd>SoC card to add controls to</dl>
 

 <i>controls</i>
<dl><dd>array of controls to add</dl>
 

 <i>num_controls</i>
<dl><dd>number of elements in the array</dl>

<h2>Description</h2>

Return 0 for success, else error.

<h2>Copyright</h2>


