---
title: "snd_pcm_format_width(9)"
name: "snd_pcm_format_width"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_format_width/"
---

snd_pcm_format_width - return the bit-width of the format

<h2>Synopsis</h2>

<pre><code>int snd_pcm_format_width(snd_pcm_format_t format);</code></pre>

<h2>Arguments</h2>

<i>format</i>
<dl><dd><dd>the format to check</dl>

<h2>Return</h2>

The bit-width of the format, or a negative error code if unknown format.

<h2>Copyright</h2>


