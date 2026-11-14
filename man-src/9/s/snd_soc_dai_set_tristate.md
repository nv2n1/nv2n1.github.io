---
title: "snd_soc_dai_set_tristate(9)"
name: "snd_soc_dai_set_tristate"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dai_set_tristate/"
---

snd_soc_dai_set_tristate - configure DAI system or master clock.

<h2>Synopsis</h2>

<pre><code>int snd_soc_dai_set_tristate(struct snd_soc_dai *dai, int tristate);</code></pre>

<h2>Arguments</h2>

<i>dai</i>
<dl><dd><dd>DAI</dl>
 

 <i>tristate</i>
<dl><dd>tristate enable</dl>

<h2>Description</h2>

Tristates the DAI so that others can use it.

<h2>Copyright</h2>


