---
title: "snd_pcm_add_chmap_ctls(9)"
name: "snd_pcm_add_chmap_ctls"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_add_chmap_ctls/"
---

snd_pcm_add_chmap_ctls - create channel-mapping control elements

<h2>Synopsis</h2>

<pre><code>int snd_pcm_add_chmap_ctls(struct snd_pcm *pcm, int stream, const struct snd_pcm_chmap_elem *chmap, int max_channels, unsigned long private_value, struct snd_pcm_chmap **info_ret);</code></pre>

<h2>Arguments</h2>

<i>pcm</i>
<dl><dd><dd>the assigned PCM instance</dl>
 

 <i>stream</i>
<dl><dd>stream direction</dl>
 

 <i>chmap</i>
<dl><dd>channel map elements (for query)</dl>
 

 <i>max_channels</i>
<dl><dd>the max number of channels for the stream</dl>
 

 <i>private_value</i>
<dl><dd>the value passed to each kcontrol's private_value field</dl>
 

 <i>info_ret</i>
<dl><dd>store struct snd_pcm_chmap instance if non-NULL</dl>

<h2>Description</h2>

Create channel-mapping control elements assigned to the given PCM stream(s).

<h2>Return</h2>

Zero if successful, or a negative error value.

<h2>Copyright</h2>


