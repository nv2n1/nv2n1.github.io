---
title: "snd_pcm_stream_unlock_irqrestore(9)"
name: "snd_pcm_stream_unlock_irqrestore"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_stream_unlock_irqrestore/"
description: "snd_pcm_stream_unlock_irqrestore – Unlock the PCM stream"
---

<p>snd_pcm_stream_unlock_irqrestore &#8211; Unlock the PCM stream</p>
<h2>Synopsis</h2>
<pre><code>void snd_pcm_stream_unlock_irqrestore(struct snd_pcm_substream *substream, unsigned long flags);</code></pre>
<h2>Arguments</h2>
<p><i>substream</i></p>
<dl>
<dd>
<dd>PCM substream</dl>
<p> <i>flags</i></p>
<dl>
<dd>irq flags</dl>
<h2>Description</h2>
<p>This is a counter-part of <code>snd_pcm_stream_lock_irqsave</code>.</p>
<h2>Copyright</h2>
