---
title: "snd_soc_add_dai_link(9)"
name: "snd_soc_add_dai_link"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_add_dai_link/"
---

snd_soc_add_dai_link - Add a DAI link dynamically

<h2>Synopsis</h2>

<pre><code>int snd_soc_add_dai_link(struct snd_soc_card *card, struct snd_soc_dai_link *dai_link);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>The ASoC card to which the DAI link is added</dl>
 

 <i>dai_link</i>
<dl><dd>The new DAI link to add</dl>

<h2>Description</h2>

This function adds a DAI link to the ASoC card's link list.

<h2>Note</h2>

Topology can use this API to add DAI links when probing the topology component. And machine drivers can still define static DAI links in dai_link array.

<h2>Copyright</h2>


