---
title: "snd_pcm_stream_lock_irq(9)"
name: "snd_pcm_stream_lock_irq"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_stream_lock_irq/"
description: "snd_pcm_stream_lock_irq – Lock the PCM stream"
---

<p>snd_pcm_stream_lock_irq &#8211; Lock the PCM stream</p>
<h2>Synopsis</h2>
<pre><code>void snd_pcm_stream_lock_irq(struct snd_pcm_substream *substream);</code></pre>
<h2>Arguments</h2>
<p><i>substream</i></p>
<dl>
<dd>
<dd>PCM substream</dl>
<h2>Description</h2>
<p>This locks the PCM stream like <code>snd_pcm_stream_lock</code> and disables the local IRQ (only when nonatomic is false). In nonatomic case, this is identical as <code>snd_pcm_stream_lock</code>.</p>
<h2>Copyright</h2>
