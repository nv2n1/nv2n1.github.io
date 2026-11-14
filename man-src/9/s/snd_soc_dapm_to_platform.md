---
title: "snd_soc_dapm_to_platform(9)"
name: "snd_soc_dapm_to_platform"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dapm_to_platform/"
---

snd_soc_dapm_to_platform - Casts a DAPM context to the platform it is embedded in

<h2>Synopsis</h2>

<pre><code>struct snd_soc_platform *snd_soc_dapm_to_platform(struct snd_soc_dapm_context *dapm);</code></pre>

<h2>Arguments</h2>

<i>dapm</i>
<dl><dd><dd>The DAPM context to cast to the platform.</dl>

<h2>Description</h2>

This function must only be used on DAPM contexts that are known to be part of a platform (e.g. in a platform driver). Otherwise the behavior is undefined.

<h2>Copyright</h2>


