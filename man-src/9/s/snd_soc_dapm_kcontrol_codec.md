---
title: "snd_soc_dapm_kcontrol_codec(9)"
name: "snd_soc_dapm_kcontrol_codec"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dapm_kcontrol_codec/"
---

snd_soc_dapm_kcontrol_codec - Returns the codec associated to a kcontrol

<h2>Synopsis</h2>

<pre><code>struct snd_soc_codec *snd_soc_dapm_kcontrol_codec(struct snd_kcontrol *kcontrol);</code></pre>

<h2>Arguments</h2>

<i>kcontrol</i>
<dl><dd><dd>The kcontrol</dl>

<h2>Description</h2>

This function must only be used on DAPM contexts that are known to be part of a CODEC (e.g. in a CODEC driver). Otherwise the behavior is undefined.

<h2>Copyright</h2>


