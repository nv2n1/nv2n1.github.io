---
title: "snd_pcm_playback_ready(9)"
name: "snd_pcm_playback_ready"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_playback_ready/"
---

snd_pcm_playback_ready - check whether the playback buffer is available

<h2>Synopsis</h2>

<pre><code>int snd_pcm_playback_ready(struct snd_pcm_substream *substream);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>the pcm substream instance</dl>

<h2>Description</h2>

Checks whether enough free space is available on the playback buffer.

<h2>Return</h2>

Non-zero if available, or zero if not.

<h2>Copyright</h2>


