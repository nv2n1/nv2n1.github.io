---
title: "snd_pcm_set_ops(9)"
name: "snd_pcm_set_ops"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_set_ops/"
---

snd_pcm_set_ops - set the PCM operators

<h2>Synopsis</h2>

<pre><code>void snd_pcm_set_ops(struct snd_pcm *pcm, int direction, const struct snd_pcm_ops *ops);</code></pre>

<h2>Arguments</h2>

<i>pcm</i>
<dl><dd><dd>the pcm instance</dl>
 

 <i>direction</i>
<dl><dd>stream direction, SNDRV_PCM_STREAM_XXX</dl>
 

 <i>ops</i>
<dl><dd>the operator table</dl>

<h2>Description</h2>

Sets the given PCM operators to the pcm instance.

<h2>Copyright</h2>


