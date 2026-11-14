---
title: "snd_soc_jack_free_gpios(9)"
name: "snd_soc_jack_free_gpios"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_jack_free_gpios/"
---

snd_soc_jack_free_gpios - Release GPIO pins' resources of an ASoC jack

<h2>Synopsis</h2>

<pre><code>void snd_soc_jack_free_gpios(struct snd_soc_jack *jack, int count, struct snd_soc_jack_gpio *gpios);</code></pre>

<h2>Arguments</h2>

<i>jack</i>
<dl><dd><dd>ASoC jack</dl>
 

 <i>count</i>
<dl><dd>number of pins</dl>
 

 <i>gpios</i>
<dl><dd>array of gpio pins</dl>

<h2>Description</h2>

Release gpio and irq resources for gpio pins associated with an ASoC jack.

<h2>Copyright</h2>


