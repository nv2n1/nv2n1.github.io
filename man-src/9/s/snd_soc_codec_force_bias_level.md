---
title: "snd_soc_codec_force_bias_level(9)"
name: "snd_soc_codec_force_bias_level"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_codec_force_bias_level/"
description: "snd_soc_codec_force_bias_level – Set the CODEC DAPM bias level"
---

<p>snd_soc_codec_force_bias_level &#8211; Set the CODEC DAPM bias level</p>
<h2>Synopsis</h2>
<pre><code>int snd_soc_codec_force_bias_level(struct snd_soc_codec *codec, enum snd_soc_bias_level level);</code></pre>
<h2>Arguments</h2>
<p><i>codec</i></p>
<dl>
<dd>
<dd>The CODEC for which to set the level</dl>
<p> <i>level</i></p>
<dl>
<dd>The level to set to</dl>
<h2>Description</h2>
<p>Forces the CODEC bias level to a specific state. See <code>snd_soc_dapm_force_bias_level</code>.</p>
<h2>Copyright</h2>
