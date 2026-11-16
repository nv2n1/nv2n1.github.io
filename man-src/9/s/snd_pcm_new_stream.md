---
title: "snd_pcm_new_stream(9)"
name: "snd_pcm_new_stream"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_new_stream/"
description: "snd_pcm_new_stream – create a new PCM stream"
---

<p>snd_pcm_new_stream &#8211; create a new PCM stream</p>
<h2>Synopsis</h2>
<pre><code>int snd_pcm_new_stream(struct snd_pcm *pcm, int stream, int substream_count);</code></pre>
<h2>Arguments</h2>
<p><i>pcm</i></p>
<dl>
<dd>
</dd><dd>the pcm instance</dd></dl>
<p> <i>stream</i></p>
<dl>
<dd>the stream direction, SNDRV_PCM_STREAM_XXX</dd></dl>
<p> <i>substream_count</i></p>
<dl>
<dd>the number of substreams</dd></dl>
<h2>Description</h2>
<p>Creates a new stream for the pcm. The corresponding stream on the pcm must have been empty before calling this, i.e. zero must be given to the argument of <code>snd_pcm_new</code>.</p>
<h2>Return</h2>
<p>Zero if successful, or a negative error code on failure.</p>
<h2>Copyright</h2>
