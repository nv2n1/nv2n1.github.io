---
title: "snd_jack_set_parent(9)"
name: "snd_jack_set_parent"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_jack_set_parent/"
---

snd_jack_set_parent - Set the parent device for a jack

<h2>Synopsis</h2>

<pre><code>void snd_jack_set_parent(struct snd_jack *jack, struct device *parent);</code></pre>

<h2>Arguments</h2>

<i>jack</i>
<dl><dd><dd>The jack to configure</dl>
 

 <i>parent</i>
<dl><dd>The device to set as parent for the jack.</dl>

<h2>Description</h2>

Set the parent for the jack devices in the device tree. This function is only valid prior to registration of the jack. If no parent is configured then the parent device will be the sound card.

<h2>Copyright</h2>


