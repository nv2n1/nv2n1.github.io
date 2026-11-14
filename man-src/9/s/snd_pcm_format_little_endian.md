---
title: "snd_pcm_format_little_endian(9)"
name: "snd_pcm_format_little_endian"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_format_little_endian/"
---

snd_pcm_format_little_endian - Check the PCM format is little-endian

<h2>Synopsis</h2>

<pre><code>int snd_pcm_format_little_endian(snd_pcm_format_t format);</code></pre>

<h2>Arguments</h2>

<i>format</i>
<dl><dd><dd>the format to check</dl>

<h2>Return</h2>

1 if the given PCM format is little-endian, 0 if big-endian, or a negative error code if endian not specified.

<h2>Copyright</h2>


