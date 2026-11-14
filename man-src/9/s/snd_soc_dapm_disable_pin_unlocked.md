---
title: "snd_soc_dapm_disable_pin_unlocked(9)"
name: "snd_soc_dapm_disable_pin_unlocked"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dapm_disable_pin_unlocked/"
description: "snd_soc_dapm_disable_pin_unlocked – disable pin."
---

<p>snd_soc_dapm_disable_pin_unlocked &#8211; disable pin.</p>
<h2>Synopsis</h2>
<pre><code>int snd_soc_dapm_disable_pin_unlocked(struct snd_soc_dapm_context *dapm, const char *pin);</code></pre>
<h2>Arguments</h2>
<p><i>dapm</i></p>
<dl>
<dd>
<dd>DAPM context</dl>
<p> <i>pin</i></p>
<dl>
<dd>pin name</dl>
<h2>Description</h2>
<p>Disables input/output pin and its parents or children widgets. </p>
<p> Requires external locking.</p>
<h2>Note</h2>
<p><code>snd_soc_dapm_sync</code> needs to be called after this for DAPM to do any widget power switching.</p>
<h2>Copyright</h2>
