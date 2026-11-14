---
title: "snd_dmaengine_pcm_pointer(9)"
name: "snd_dmaengine_pcm_pointer"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_dmaengine_pcm_pointer/"
description: "snd_dmaengine_pcm_pointer – dmaengine based PCM pointer implementation"
---

<p>snd_dmaengine_pcm_pointer &#8211; dmaengine based PCM pointer implementation</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>snd_pcm_uframes_t snd_dmaengine_pcm_pointer(struct snd_pcm_substream&nbsp;<wbr>*&nbsp;<wbr></code><i>substream</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>substream</i></p>
<dl>
<dd>
<dd>PCM substream</dl>
<h2>Description</h2>
<p>This function can be used as the PCM pointer callback for dmaengine based PCM driver implementations.</p>
<h2>Copyright</h2>
