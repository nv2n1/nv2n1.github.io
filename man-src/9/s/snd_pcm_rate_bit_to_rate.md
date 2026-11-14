---
title: "snd_pcm_rate_bit_to_rate(9)"
name: "snd_pcm_rate_bit_to_rate"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_rate_bit_to_rate/"
---

snd_pcm_rate_bit_to_rate - converts SNDRV_PCM_RATE_xxx bit to sample rate

<h2>Synopsis</h2>

<pre><code>unsigned int snd_pcm_rate_bit_to_rate(unsigned int rate_bit);</code></pre>

<h2>Arguments</h2>

<i>rate_bit</i>
<dl><dd><dd>the rate bit to convert</dl>

<h2>Return</h2>

The sample rate that corresponds to the given SNDRV_PCM_RATE_xxx flag or 0 for an unknown rate bit.

<h2>Copyright</h2>


