---
title: "snd_soc_info_volsw_sx(9)"
name: "snd_soc_info_volsw_sx"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_info_volsw_sx/"
---

snd_soc_info_volsw_sx - Mixer info callback for SX TLV controls

<h2>Synopsis</h2>

<pre><code>int snd_soc_info_volsw_sx(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_info *uinfo);</code></pre>

<h2>Arguments</h2>

<i>kcontrol</i>
<dl><dd><dd>mixer control</dl>
 

 <i>uinfo</i>
<dl><dd>control element information</dl>

<h2>Description</h2>

Callback to provide information about a single mixer control, or a double mixer control that spans 2 registers of the SX TLV type. SX TLV controls have a range that represents both positive and negative values either side of zero but without a sign bit. 

 Returns 0 for success.

<h2>Copyright</h2>


