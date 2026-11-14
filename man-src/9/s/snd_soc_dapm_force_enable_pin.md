---
title: "snd_soc_dapm_force_enable_pin(9)"
name: "snd_soc_dapm_force_enable_pin"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dapm_force_enable_pin/"
description: "snd_soc_dapm_force_enable_pin – force a pin to be enabled"
---

<p>snd_soc_dapm_force_enable_pin &#8211; force a pin to be enabled</p>
<h2>Synopsis</h2>
<pre><code>int snd_soc_dapm_force_enable_pin(struct snd_soc_dapm_context *dapm, const char *pin);</code></pre>
<h2>Arguments</h2>
<p><i>dapm</i></p>
<dl>
<dd>
<dd>DAPM context</dl>
<p> <i>pin</i></p>
<dl>
<dd>pin name</dl>
<h2>Description</h2>
<p>Enables input/output pin regardless of any other state. This is intended for use with microphone bias supplies used in microphone jack detection.</p>
<h2>Note</h2>
<p><code>snd_soc_dapm_sync</code> needs to be called after this for DAPM to do any widget power switching.</p>
<h2>Copyright</h2>
