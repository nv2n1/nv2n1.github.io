---
title: "snd_pcm_set_runtime_buffer(9)"
name: "snd_pcm_set_runtime_buffer"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_set_runtime_buffer/"
---

snd_pcm_set_runtime_buffer - Set the PCM runtime buffer

<h2>Synopsis</h2>

<pre><code>void snd_pcm_set_runtime_buffer(struct snd_pcm_substream *substream, struct snd_dma_buffer *bufp);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>PCM substream to set</dl>
 

 <i>bufp</i>
<dl><dd>the buffer information, NULL to clear</dl>

<h2>Description</h2>

Copy the buffer information to runtime-&gt;dma_buffer when <i>bufp</i> is non-NULL. Otherwise it clears the current buffer information.

<h2>Copyright</h2>


