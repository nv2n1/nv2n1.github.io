---
title: "snd_pcm_running(9)"
name: "snd_pcm_running"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_running/"
---

snd_pcm_running - Check whether the substream is in a running state

<h2>Synopsis</h2>

<pre><code>int snd_pcm_running(struct snd_pcm_substream *substream);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>substream to check</dl>

<h2>Description</h2>

Returns true if the given substream is in the state RUNNING, or in the state DRAINING for playback.

<h2>Copyright</h2>


