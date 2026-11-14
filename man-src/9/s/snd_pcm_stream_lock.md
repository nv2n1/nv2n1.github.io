---
title: "snd_pcm_stream_lock(9)"
name: "snd_pcm_stream_lock"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_stream_lock/"
---

snd_pcm_stream_lock - Lock the PCM stream

<h2>Synopsis</h2>

<pre><code>void snd_pcm_stream_lock(struct snd_pcm_substream *substream);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>PCM substream</dl>

<h2>Description</h2>

This locks the PCM stream's spinlock or mutex depending on the nonatomic flag of the given substream. This also takes the global link rw lock (or rw sem), too, for avoiding the race with linked streams.

<h2>Copyright</h2>


