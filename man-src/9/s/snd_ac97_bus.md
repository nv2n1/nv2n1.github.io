---
title: "snd_ac97_bus(9)"
name: "snd_ac97_bus"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ac97_bus/"
---

snd_ac97_bus - create an AC97 bus component

<h2>Synopsis</h2>

<pre><code>int snd_ac97_bus(struct snd_card *card, int num, struct snd_ac97_bus_ops *ops, void *private_data, struct snd_ac97_bus **rbus);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>the card instance</dl>
 

 <i>num</i>
<dl><dd>the bus number</dl>
 

 <i>ops</i>
<dl><dd>the bus callbacks table</dl>
 

 <i>private_data</i>
<dl><dd>private data pointer for the new instance</dl>
 

 <i>rbus</i>
<dl><dd>the pointer to store the new AC97 bus instance.</dl>

<h2>Description</h2>

Creates an AC97 bus component. An struct snd_ac97_bus instance is newly allocated and initialized. 

 The ops table must include valid callbacks (at least read and write). The other callbacks, wait and reset, are not mandatory. 

 The clock is set to 48000. If another clock is needed, set (*rbus)-&gt;clock manually. 

 The AC97 bus instance is registered as a low-level device, so you don't have to release it manually.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


