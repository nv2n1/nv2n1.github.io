---
title: "snd_soc_component_to_platform(9)"
name: "snd_soc_component_to_platform"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_component_to_platform/"
---

snd_soc_component_to_platform - Casts a component to the platform it is embedded in

<h2>Synopsis</h2>

<pre><code>struct snd_soc_platform *snd_soc_component_to_platform(struct snd_soc_component *component);</code></pre>

<h2>Arguments</h2>

<i>component</i>
<dl><dd><dd>The component to cast to a platform</dl>

<h2>Description</h2>

This function must only be used on components that are known to be platforms. Otherwise the behavior is undefined.

<h2>Copyright</h2>


