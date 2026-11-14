---
title: "snd_soc_add_codec_controls(9)"
name: "snd_soc_add_codec_controls"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_add_codec_controls/"
---

snd_soc_add_codec_controls - add an array of controls to a codec. Convenience function to add a list of controls. Many codecs were duplicating this code.

<h2>Synopsis</h2>

<pre><code>int snd_soc_add_codec_controls(struct snd_soc_codec *codec, const struct snd_kcontrol_new *controls, unsigned int num_controls);</code></pre>

<h2>Arguments</h2>

<i>codec</i>
<dl><dd><dd>codec to add controls to</dl>
 

 <i>controls</i>
<dl><dd>array of controls to add</dl>
 

 <i>num_controls</i>
<dl><dd>number of elements in the array</dl>

<h2>Description</h2>

Return 0 for success, else error.

<h2>Copyright</h2>


