---
title: "snd_soc_codec_get_dapm(9)"
name: "snd_soc_codec_get_dapm"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_codec_get_dapm/"
---

snd_soc_codec_get_dapm - Returns the DAPM context for the CODEC

<h2>Synopsis</h2>

<pre><code>struct snd_soc_dapm_context *snd_soc_codec_get_dapm(struct snd_soc_codec *codec);</code></pre>

<h2>Arguments</h2>

<i>codec</i>
<dl><dd><dd>The CODEC for which to get the DAPM context</dl>

<h2>Note</h2>

Use this function instead of directly accessing the CODEC's dapm field

<h2>Copyright</h2>


