---
title: "snd_soc_info_volsw_range(9)"
name: "snd_soc_info_volsw_range"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_info_volsw_range/"
---

snd_soc_info_volsw_range - single mixer info callback with range.

<h2>Synopsis</h2>

<pre><code>int snd_soc_info_volsw_range(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_info *uinfo);</code></pre>

<h2>Arguments</h2>

<i>kcontrol</i>
<dl><dd><dd>mixer control</dl>
 

 <i>uinfo</i>
<dl><dd>control element information</dl>

<h2>Description</h2>

Callback to provide information, within a range, about a single mixer control. 

 returns 0 for success.

<h2>Copyright</h2>


