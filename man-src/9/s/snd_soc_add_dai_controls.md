---
title: "snd_soc_add_dai_controls(9)"
name: "snd_soc_add_dai_controls"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_add_dai_controls/"
---

snd_soc_add_dai_controls - add an array of controls to a DAI. Convienience function to add a list of controls.

<h2>Synopsis</h2>

<pre><code>int snd_soc_add_dai_controls(struct snd_soc_dai *dai, const struct snd_kcontrol_new *controls, int num_controls);</code></pre>

<h2>Arguments</h2>

<i>dai</i>
<dl><dd><dd>DAI to add controls to</dl>
 

 <i>controls</i>
<dl><dd>array of controls to add</dl>
 

 <i>num_controls</i>
<dl><dd>number of elements in the array</dl>

<h2>Description</h2>

Return 0 for success, else error.

<h2>Copyright</h2>


