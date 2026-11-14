---
title: "snd_pcm_format_unsigned(9)"
name: "snd_pcm_format_unsigned"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_format_unsigned/"
---

snd_pcm_format_unsigned - Check the PCM format is unsigned linear

<h2>Synopsis</h2>

<pre><code>int snd_pcm_format_unsigned(snd_pcm_format_t format);</code></pre>

<h2>Arguments</h2>

<i>format</i>
<dl><dd><dd>the format to check</dl>

<h2>Return</h2>

1 if the given PCM format is unsigned linear, 0 if signed linear, and a negative error code for non-linear formats.

<h2>Copyright</h2>


