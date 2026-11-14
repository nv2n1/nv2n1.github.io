---
title: "snd_pcm_stream_unlock(9)"
name: "snd_pcm_stream_unlock"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_stream_unlock/"
description: "snd_pcm_stream_unlock – Unlock the PCM stream"
---

<p>snd_pcm_stream_unlock &#8211; Unlock the PCM stream</p>
<h2>Synopsis</h2>
<pre><code>void snd_pcm_stream_unlock(struct snd_pcm_substream *substream);</code></pre>
<h2>Arguments</h2>
<p><i>substream</i></p>
<dl>
<dd>
<dd>PCM substream</dl>
<h2>Description</h2>
<p>This unlocks the PCM stream that has been locked via <code>snd_pcm_stream_lock</code>.</p>
<h2>Copyright</h2>
