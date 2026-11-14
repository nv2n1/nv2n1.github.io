---
title: "snd_soc_dapm_new_controls(9)"
name: "snd_soc_dapm_new_controls"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dapm_new_controls/"
---

snd_soc_dapm_new_controls - create new dapm controls

<h2>Synopsis</h2>

<pre><code>int snd_soc_dapm_new_controls(struct snd_soc_dapm_context *dapm, const struct snd_soc_dapm_widget *widget, int num);</code></pre>

<h2>Arguments</h2>

<i>dapm</i>
<dl><dd><dd>DAPM context</dl>
 

 <i>widget</i>
<dl><dd>widget array</dl>
 

 <i>num</i>
<dl><dd>number of widgets</dl>

<h2>Description</h2>

Creates new DAPM controls based upon the templates. 

 Returns 0 for success else error.

<h2>Copyright</h2>


