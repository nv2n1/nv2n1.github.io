---
title: "snd_soc_jack_add_gpiods(9)"
name: "snd_soc_jack_add_gpiods"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_jack_add_gpiods/"
---

snd_soc_jack_add_gpiods - Associate GPIO descriptor pins with an ASoC jack

<h2>Synopsis</h2>

<pre><code>int snd_soc_jack_add_gpiods(struct device *gpiod_dev, struct snd_soc_jack *jack, int count, struct snd_soc_jack_gpio *gpios);</code></pre>

<h2>Arguments</h2>

<i>gpiod_dev</i>
<dl><dd><dd>GPIO consumer device</dl>
 

 <i>jack</i>
<dl><dd>ASoC jack</dl>
 

 <i>count</i>
<dl><dd>number of pins</dl>
 

 <i>gpios</i>
<dl><dd>array of gpio pins</dl>

<h2>Description</h2>

This function will request gpio, set data direction and request irq for each gpio in the array.

<h2>Copyright</h2>


