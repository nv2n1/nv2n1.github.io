---
title: "snd_pcm_stream_unlock_irq(9)"
name: "snd_pcm_stream_unlock_irq"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_stream_unlock_irq/"
description: "snd_pcm_stream_unlock_irq – Unlock the PCM stream"
---

<p>snd_pcm_stream_unlock_irq &#8211; Unlock the PCM stream</p>
<h2>Synopsis</h2>
<pre><code>void snd_pcm_stream_unlock_irq(struct snd_pcm_substream *substream);</code></pre>
<h2>Arguments</h2>
<p><i>substream</i></p>
<dl>
<dd>
<dd>PCM substream</dl>
<h2>Description</h2>
<p>This is a counter-part of <code>snd_pcm_stream_lock_irq</code>.</p>
<h2>Copyright</h2>
