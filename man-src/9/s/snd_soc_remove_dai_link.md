---
title: "snd_soc_remove_dai_link(9)"
name: "snd_soc_remove_dai_link"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_remove_dai_link/"
---

snd_soc_remove_dai_link - Remove a DAI link from the list

<h2>Synopsis</h2>

<pre><code>void snd_soc_remove_dai_link(struct snd_soc_card *card, struct snd_soc_dai_link *dai_link);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>The ASoC card that owns the link</dl>
 

 <i>dai_link</i>
<dl><dd>The DAI link to remove</dl>

<h2>Description</h2>

This function removes a DAI link from the ASoC card's link list. 

 For DAI links previously added by topology, topology should remove them by using the dobj embedded in the link.

<h2>Copyright</h2>


