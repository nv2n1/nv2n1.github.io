---
title: "snd_soc_put_strobe(9)"
name: "snd_soc_put_strobe"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_put_strobe/"
---

snd_soc_put_strobe - strobe put callback

<h2>Synopsis</h2>

<pre><code>int snd_soc_put_strobe(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol);</code></pre>

<h2>Arguments</h2>

<i>kcontrol</i>
<dl><dd><dd>mixer control</dl>
 

 <i>ucontrol</i>
<dl><dd>control element information</dl>

<h2>Description</h2>

Callback strobe a register bit to high then low (or the inverse) in one pass of a single mixer enum control. 

 Returns 1 for success.

<h2>Copyright</h2>


