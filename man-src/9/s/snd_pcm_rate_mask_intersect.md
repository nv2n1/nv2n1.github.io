---
title: "snd_pcm_rate_mask_intersect(9)"
name: "snd_pcm_rate_mask_intersect"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_rate_mask_intersect/"
---

snd_pcm_rate_mask_intersect - computes the intersection between two rate masks

<h2>Synopsis</h2>

<pre><code>unsigned int snd_pcm_rate_mask_intersect(unsigned int rates_a, unsigned int rates_b);</code></pre>

<h2>Arguments</h2>

<i>rates_a</i>
<dl><dd><dd>The first rate mask</dl>
 

 <i>rates_b</i>
<dl><dd>The second rate mask</dl>

<h2>Description</h2>

This function computes the rates that are supported by both rate masks passed to the function. It will take care of the special handling of SNDRV_PCM_RATE_CONTINUOUS and SNDRV_PCM_RATE_KNOT.

<h2>Return</h2>

A rate mask containing the rates that are supported by both rates_a and rates_b.

<h2>Copyright</h2>


