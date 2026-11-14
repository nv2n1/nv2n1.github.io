---
title: "snd_pcm_limit_hw_rates(9)"
name: "snd_pcm_limit_hw_rates"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_limit_hw_rates/"
---

snd_pcm_limit_hw_rates - determine rate_min/rate_max fields

<h2>Synopsis</h2>

<pre><code>int snd_pcm_limit_hw_rates(struct snd_pcm_runtime *runtime);</code></pre>

<h2>Arguments</h2>

<i>runtime</i>
<dl><dd><dd>the runtime instance</dl>

<h2>Description</h2>

Determines the rate_min and rate_max fields from the rates bits of the given runtime-&gt;hw.

<h2>Return</h2>

Zero if successful.

<h2>Copyright</h2>


