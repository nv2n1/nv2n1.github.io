---
title: "snd_soc_get_volsw_range(9)"
name: "snd_soc_get_volsw_range"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_get_volsw_range/"
---

snd_soc_get_volsw_range - single mixer get callback with range

<h2>Synopsis</h2>

<pre><code>int snd_soc_get_volsw_range(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol);</code></pre>

<h2>Arguments</h2>

<i>kcontrol</i>
<dl><dd><dd>mixer control</dl>
 

 <i>ucontrol</i>
<dl><dd>control element information</dl>

<h2>Description</h2>

Callback to get the value, within a range, of a single mixer control. 

 Returns 0 for success.

<h2>Copyright</h2>


