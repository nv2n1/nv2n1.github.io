---
title: "snd_soc_get_volsw(9)"
name: "snd_soc_get_volsw"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_get_volsw/"
---

snd_soc_get_volsw - single mixer get callback

<h2>Synopsis</h2>

<pre><code>int snd_soc_get_volsw(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol);</code></pre>

<h2>Arguments</h2>

<i>kcontrol</i>
<dl><dd><dd>mixer control</dl>
 

 <i>ucontrol</i>
<dl><dd>control element information</dl>

<h2>Description</h2>

Callback to get the value of a single mixer control, or a double mixer control that spans 2 registers. 

 Returns 0 for success.

<h2>Copyright</h2>


