---
title: "snd_soc_dapm_kcontrol_dapm(9)"
name: "snd_soc_dapm_kcontrol_dapm"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dapm_kcontrol_dapm/"
---

snd_soc_dapm_kcontrol_dapm - Returns the dapm context associated to a kcontrol

<h2>Synopsis</h2>

<pre><code>struct snd_soc_dapm_context *snd_soc_dapm_kcontrol_dapm(struct snd_kcontrol *kcontrol);</code></pre>

<h2>Arguments</h2>

<i>kcontrol</i>
<dl><dd><dd>The kcontrol</dl>

<h2>Note</h2>

This function must only be used on kcontrols that are known to have been registered for a CODEC. Otherwise the behaviour is undefined.

<h2>Copyright</h2>


