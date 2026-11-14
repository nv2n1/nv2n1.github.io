---
title: "snd_pcm_rate_to_rate_bit(9)"
name: "snd_pcm_rate_to_rate_bit"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_rate_to_rate_bit/"
---

snd_pcm_rate_to_rate_bit - converts sample rate to SNDRV_PCM_RATE_xxx bit

<h2>Synopsis</h2>

<pre><code>unsigned int snd_pcm_rate_to_rate_bit(unsigned int rate);</code></pre>

<h2>Arguments</h2>

<i>rate</i>
<dl><dd><dd>the sample rate to convert</dl>

<h2>Return</h2>

The SNDRV_PCM_RATE_xxx flag that corresponds to the given rate, or SNDRV_PCM_RATE_KNOT for an unknown rate.

<h2>Copyright</h2>


