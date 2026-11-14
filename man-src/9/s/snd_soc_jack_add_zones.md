---
title: "snd_soc_jack_add_zones(9)"
name: "snd_soc_jack_add_zones"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_jack_add_zones/"
---

snd_soc_jack_add_zones - Associate voltage zones with jack

<h2>Synopsis</h2>

<pre><code>int snd_soc_jack_add_zones(struct snd_soc_jack *jack, int count, struct snd_soc_jack_zone *zones);</code></pre>

<h2>Arguments</h2>

<i>jack</i>
<dl><dd><dd>ASoC jack</dl>
 

 <i>count</i>
<dl><dd>Number of zones</dl>
 

 <i>zones</i>
<dl><dd>Array of zones</dl>

<h2>Description</h2>

After this function has been called the zones specified in the array will be associated with the jack.

<h2>Copyright</h2>


