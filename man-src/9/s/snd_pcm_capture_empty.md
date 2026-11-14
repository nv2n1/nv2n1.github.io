---
title: "snd_pcm_capture_empty(9)"
name: "snd_pcm_capture_empty"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_capture_empty/"
---

snd_pcm_capture_empty - check whether the capture buffer is empty

<h2>Synopsis</h2>

<pre><code>int snd_pcm_capture_empty(struct snd_pcm_substream *substream);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>the pcm substream instance</dl>

<h2>Description</h2>

Checks whether the capture buffer is empty.

<h2>Return</h2>

Non-zero if empty, or zero if not.

<h2>Copyright</h2>


