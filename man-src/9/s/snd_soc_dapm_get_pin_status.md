---
title: "snd_soc_dapm_get_pin_status(9)"
name: "snd_soc_dapm_get_pin_status"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dapm_get_pin_status/"
---

snd_soc_dapm_get_pin_status - get audio pin status

<h2>Synopsis</h2>

<pre><code>int snd_soc_dapm_get_pin_status(struct snd_soc_dapm_context *dapm, const char *pin);</code></pre>

<h2>Arguments</h2>

<i>dapm</i>
<dl><dd><dd>DAPM context</dl>
 

 <i>pin</i>
<dl><dd>audio signal pin endpoint (or start point)</dl>

<h2>Description</h2>

Get audio pin status - connected or disconnected. 

 Returns 1 for connected otherwise 0.

<h2>Copyright</h2>


