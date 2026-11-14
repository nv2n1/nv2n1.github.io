---
title: "snd_pcm_format_set_silence(9)"
name: "snd_pcm_format_set_silence"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_format_set_silence/"
---

snd_pcm_format_set_silence - set the silence data on the buffer

<h2>Synopsis</h2>

<pre><code>int snd_pcm_format_set_silence(snd_pcm_format_t format, void *data, unsigned int samples);</code></pre>

<h2>Arguments</h2>

<i>format</i>
<dl><dd><dd>the PCM format</dl>
 

 <i>data</i>
<dl><dd>the buffer pointer</dl>
 

 <i>samples</i>
<dl><dd>the number of samples to set silence</dl>

<h2>Description</h2>

Sets the silence data on the buffer for the given samples.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


