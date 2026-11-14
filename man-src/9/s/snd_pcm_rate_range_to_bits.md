---
title: "snd_pcm_rate_range_to_bits(9)"
name: "snd_pcm_rate_range_to_bits"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_rate_range_to_bits/"
---

snd_pcm_rate_range_to_bits - converts rate range to SNDRV_PCM_RATE_xxx bit

<h2>Synopsis</h2>

<pre><code>unsigned int snd_pcm_rate_range_to_bits(unsigned int rate_min, unsigned int rate_max);</code></pre>

<h2>Arguments</h2>

<i>rate_min</i>
<dl><dd><dd>the minimum sample rate</dl>
 

 <i>rate_max</i>
<dl><dd>the maximum sample rate</dl>

<h2>Description</h2>

This function has an implicit assumption: the rates in the given range have only the pre-defined rates like 44100 or 16000.

<h2>Return</h2>

The SNDRV_PCM_RATE_xxx flag that corresponds to the given rate range, or SNDRV_PCM_RATE_KNOT for an unknown range.

<h2>Copyright</h2>


