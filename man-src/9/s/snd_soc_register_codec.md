---
title: "snd_soc_register_codec(9)"
name: "snd_soc_register_codec"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_register_codec/"
---

snd_soc_register_codec - Register a codec with the ASoC core

<h2>Synopsis</h2>

<pre><code>int snd_soc_register_codec(struct device *dev, const struct snd_soc_codec_driver *codec_drv, struct snd_soc_dai_driver *dai_drv, int num_dai);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>The parent device for this codec</dl>
 

 <i>codec_drv</i>
<dl><dd>Codec driver</dl>
 

 <i>dai_drv</i>
<dl><dd>The associated DAI driver</dl>
 

 <i>num_dai</i>
<dl><dd>Number of DAIs</dl>

<h2>Copyright</h2>


