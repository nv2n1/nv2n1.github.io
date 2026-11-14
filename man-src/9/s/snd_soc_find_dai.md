---
title: "snd_soc_find_dai(9)"
name: "snd_soc_find_dai"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_find_dai/"
---

snd_soc_find_dai - Find a registered DAI

<h2>Synopsis</h2>

<pre><code>struct snd_soc_dai *snd_soc_find_dai(const struct snd_soc_dai_link_component *dlc);</code></pre>

<h2>Arguments</h2>

<i>dlc</i>
<dl><dd><dd>name of the DAI and optional component info to match</dl>

<h2>Description</h2>

This function will search all regsitered components and their DAIs to find the DAI of the same name. The component's of_node and name should also match if being specified.

<h2>Return</h2>

pointer of DAI, or NULL if not found.

<h2>Copyright</h2>


