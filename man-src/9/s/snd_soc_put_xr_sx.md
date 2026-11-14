---
title: "snd_soc_put_xr_sx(9)"
name: "snd_soc_put_xr_sx"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_put_xr_sx/"
---

snd_soc_put_xr_sx - signed multi register get callback

<h2>Synopsis</h2>

<pre><code>int snd_soc_put_xr_sx(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol);</code></pre>

<h2>Arguments</h2>

<i>kcontrol</i>
<dl><dd><dd>mreg control</dl>
 

 <i>ucontrol</i>
<dl><dd>control element information</dl>

<h2>Description</h2>

Callback to set the value of a control that can span multiple codec registers which together forms a single signed value in a MSB/LSB manner. The control supports specifying total no of bits used to allow for bitfields across the multiple codec registers. 

 Returns 0 for success.

<h2>Copyright</h2>


