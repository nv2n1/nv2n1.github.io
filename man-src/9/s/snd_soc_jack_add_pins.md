---
title: "snd_soc_jack_add_pins(9)"
name: "snd_soc_jack_add_pins"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_jack_add_pins/"
---

snd_soc_jack_add_pins - Associate DAPM pins with an ASoC jack

<h2>Synopsis</h2>

<pre><code>int snd_soc_jack_add_pins(struct snd_soc_jack *jack, int count, struct snd_soc_jack_pin *pins);</code></pre>

<h2>Arguments</h2>

<i>jack</i>
<dl><dd><dd>ASoC jack</dl>
 

 <i>count</i>
<dl><dd>Number of pins</dl>
 

 <i>pins</i>
<dl><dd>Array of pins</dl>

<h2>Description</h2>

After this function has been called the DAPM pins specified in the pins array will have their status updated to reflect the current state of the jack whenever the jack status is updated.

<h2>Copyright</h2>


