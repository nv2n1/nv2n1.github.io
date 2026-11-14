---
title: "snd_pcm_stream_lock_irqsave(9)"
name: "snd_pcm_stream_lock_irqsave"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_stream_lock_irqsave/"
description: "snd_pcm_stream_lock_irqsave – Lock the PCM stream"
---

<p>snd_pcm_stream_lock_irqsave &#8211; Lock the PCM stream</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>snd_pcm_stream_lock_irqsave(</code><i>substream</i><code>, </code><i>flags</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>substream</i></p>
<dl>
<dd>
<dd>PCM substream</dl>
<p> <i>flags</i></p>
<dl>
<dd>irq flags</dl>
<h2>Description</h2>
<p>This locks the PCM stream like <code>snd_pcm_stream_lock</code> but with the local IRQ (only when nonatomic is false). In nonatomic case, this is identical as <code>snd_pcm_stream_lock</code>.</p>
<h2>Copyright</h2>
