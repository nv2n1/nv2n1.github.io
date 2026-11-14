---
title: "snd_soc_kcontrol_codec(9)"
name: "snd_soc_kcontrol_codec"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_kcontrol_codec/"
description: "snd_soc_kcontrol_codec – Returns the CODEC that registered the control"
---

<p>snd_soc_kcontrol_codec &#8211; Returns the CODEC that registered the control</p>
<h2>Synopsis</h2>
<pre><code>struct snd_soc_codec *snd_soc_kcontrol_codec(struct snd_kcontrol *kcontrol);</code></pre>
<h2>Arguments</h2>
<p><i>kcontrol</i></p>
<dl>
<dd>
<dd>The control for which to get the CODEC</dl>
<h2>Note</h2>
<p>This function will only work correctly if the control has been registered with <code>snd_soc_add_codec_controls</code> or via table based setup of snd_soc_codec_driver. Otherwise the behavior is undefined.</p>
<h2>Copyright</h2>
