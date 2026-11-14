---
title: "snd_pcm_playback_data(9)"
name: "snd_pcm_playback_data"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_playback_data/"
---

snd_pcm_playback_data - check whether any data exists on the playback buffer

<h2>Synopsis</h2>

<pre><code>int snd_pcm_playback_data(struct snd_pcm_substream *substream);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>the pcm substream instance</dl>

<h2>Description</h2>

Checks whether any data exists on the playback buffer.

<h2>Return</h2>

Non-zero if any data exists, or zero if not. If stop_threshold is bigger or equal to boundary, then this function returns always non-zero.

<h2>Copyright</h2>


