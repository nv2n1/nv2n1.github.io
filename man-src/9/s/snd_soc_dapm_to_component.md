---
title: "snd_soc_dapm_to_component(9)"
name: "snd_soc_dapm_to_component"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dapm_to_component/"
---

snd_soc_dapm_to_component - Casts a DAPM context to the component it is embedded in

<h2>Synopsis</h2>

<pre><code>struct snd_soc_component *snd_soc_dapm_to_component(struct snd_soc_dapm_context *dapm);</code></pre>

<h2>Arguments</h2>

<i>dapm</i>
<dl><dd><dd>The DAPM context to cast to the component</dl>

<h2>Description</h2>

This function must only be used on DAPM contexts that are known to be part of a component (e.g. in a component driver). Otherwise the behavior is undefined.

<h2>Copyright</h2>


