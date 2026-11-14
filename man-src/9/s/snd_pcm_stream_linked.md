---
title: "snd_pcm_stream_linked(9)"
name: "snd_pcm_stream_linked"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_stream_linked/"
---

snd_pcm_stream_linked - Check whether the substream is linked with others

<h2>Synopsis</h2>

<pre><code>int snd_pcm_stream_linked(struct snd_pcm_substream *substream);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>substream to check</dl>

<h2>Description</h2>

Returns true if the given substream is being linked with others.

<h2>Copyright</h2>


