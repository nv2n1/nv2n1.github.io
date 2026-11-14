---
title: "snd_pcm_format_signed(9)"
name: "snd_pcm_format_signed"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_format_signed/"
---

snd_pcm_format_signed - Check the PCM format is signed linear

<h2>Synopsis</h2>

<pre><code>int snd_pcm_format_signed(snd_pcm_format_t format);</code></pre>

<h2>Arguments</h2>

<i>format</i>
<dl><dd><dd>the format to check</dl>

<h2>Return</h2>

1 if the given PCM format is signed linear, 0 if unsigned linear, and a negative error code for non-linear formats.

<h2>Copyright</h2>


