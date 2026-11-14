---
title: "snd_soc_dapm_to_codec(9)"
name: "snd_soc_dapm_to_codec"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dapm_to_codec/"
---

snd_soc_dapm_to_codec - Casts a DAPM context to the CODEC it is embedded in

<h2>Synopsis</h2>

<pre><code>struct snd_soc_codec *snd_soc_dapm_to_codec(struct snd_soc_dapm_context *dapm);</code></pre>

<h2>Arguments</h2>

<i>dapm</i>
<dl><dd><dd>The DAPM context to cast to the CODEC</dl>

<h2>Description</h2>

This function must only be used on DAPM contexts that are known to be part of a CODEC (e.g. in a CODEC driver). Otherwise the behavior is undefined.

<h2>Copyright</h2>


