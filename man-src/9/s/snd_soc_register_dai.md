---
title: "snd_soc_register_dai(9)"
name: "snd_soc_register_dai"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_register_dai/"
---

snd_soc_register_dai - Register a DAI dynamically &amp; create its widgets

<h2>Synopsis</h2>

<pre><code>int snd_soc_register_dai(struct snd_soc_component *component, struct snd_soc_dai_driver *dai_drv);</code></pre>

<h2>Arguments</h2>

<i>component</i>
<dl><dd><dd>The component the DAIs are registered for</dl>
 

 <i>dai_drv</i>
<dl><dd>DAI driver to use for the DAI</dl>

<h2>Description</h2>

Topology can use this API to register DAIs when probing a component. These DAIs's widgets will be freed in the card cleanup and the DAIs will be freed in the component cleanup.

<h2>Copyright</h2>


