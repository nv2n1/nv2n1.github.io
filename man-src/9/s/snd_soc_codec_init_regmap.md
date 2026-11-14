---
title: "snd_soc_codec_init_regmap(9)"
name: "snd_soc_codec_init_regmap"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_codec_init_regmap/"
---

snd_soc_codec_init_regmap - Initialize regmap instance for the CODEC

<h2>Synopsis</h2>

<pre><code>void snd_soc_codec_init_regmap(struct snd_soc_codec *codec, struct regmap *regmap);</code></pre>

<h2>Arguments</h2>

<i>codec</i>
<dl><dd><dd>The CODEC for which to initialize the regmap instance</dl>
 

 <i>regmap</i>
<dl><dd>The regmap instance that should be used by the CODEC</dl>

<h2>Description</h2>

This function allows deferred assignment of the regmap instance that is associated with the CODEC. Only use this if the regmap instance is not yet ready when the CODEC is registered. The function must also be called before the first IO attempt of the CODEC.

<h2>Copyright</h2>


