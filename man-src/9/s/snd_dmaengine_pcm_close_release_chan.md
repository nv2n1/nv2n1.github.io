---
title: "snd_dmaengine_pcm_close_release_chan(9)"
name: "snd_dmaengine_pcm_close_release_chan"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_dmaengine_pcm_close_release_chan/"
---

snd_dmaengine_pcm_close_release_chan - Close a dmaengine based PCM substream and release channel

<h2>Synopsis</h2>

<pre><code>int snd_dmaengine_pcm_close_release_chan(struct snd_pcm_substream *substream);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>PCM substream</dl>

<h2>Description</h2>

Releases the DMA channel associated with the PCM substream.

<h2>Copyright</h2>


