---
title: "snd_pcm_stream_str(9)"
name: "snd_pcm_stream_str"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_stream_str/"
---

snd_pcm_stream_str - Get a string naming the direction of a stream

<h2>Synopsis</h2>

<pre><code>const char *snd_pcm_stream_str(struct snd_pcm_substream *substream);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>the pcm substream instance</dl>

<h2>Return</h2>

A string naming the direction of the stream.

<h2>Copyright</h2>


