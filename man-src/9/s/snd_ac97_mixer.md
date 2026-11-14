---
title: "snd_ac97_mixer(9)"
name: "snd_ac97_mixer"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ac97_mixer/"
---

snd_ac97_mixer - create an Codec97 component

<h2>Synopsis</h2>

<pre><code>int snd_ac97_mixer(struct snd_ac97_bus *bus, struct snd_ac97_template *template, struct snd_ac97 **rac97);</code></pre>

<h2>Arguments</h2>

<i>bus</i>
<dl><dd><dd>the AC97 bus which codec is attached to</dl>
 

 <i>template</i>
<dl><dd>the template of ac97, including index, callbacks and the private data.</dl>
 

 <i>rac97</i>
<dl><dd>the pointer to store the new ac97 instance.</dl>

<h2>Description</h2>

Creates an Codec97 component. An struct snd_ac97 instance is newly allocated and initialized from the template. The codec is then initialized by the standard procedure. 

 The template must include the codec number (num) and address (addr), and the private data (private_data). 

 The ac97 instance is registered as a low-level device, so you don't have to release it manually.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


