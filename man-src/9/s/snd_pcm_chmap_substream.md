---
title: "snd_pcm_chmap_substream(9)"
name: "snd_pcm_chmap_substream"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_chmap_substream/"
---

snd_pcm_chmap_substream - get the PCM substream assigned to the given chmap info

<h2>Synopsis</h2>

<pre><code>struct snd_pcm_substream *snd_pcm_chmap_substream(struct snd_pcm_chmap *info, unsigned int idx);</code></pre>

<h2>Arguments</h2>

<i>info</i>
<dl><dd><dd>chmap information</dl>
 

 <i>idx</i>
<dl><dd>the substream number index</dl>

<h2>Copyright</h2>


