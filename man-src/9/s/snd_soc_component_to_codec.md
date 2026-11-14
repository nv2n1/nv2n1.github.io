---
title: "snd_soc_component_to_codec(9)"
name: "snd_soc_component_to_codec"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_component_to_codec/"
---

snd_soc_component_to_codec - Casts a component to the CODEC it is embedded in

<h2>Synopsis</h2>

<pre><code>struct snd_soc_codec *snd_soc_component_to_codec(struct snd_soc_component *component);</code></pre>

<h2>Arguments</h2>

<i>component</i>
<dl><dd><dd>The component to cast to a CODEC</dl>

<h2>Description</h2>

This function must only be used on components that are known to be CODECs. Otherwise the behavior is undefined.

<h2>Copyright</h2>


