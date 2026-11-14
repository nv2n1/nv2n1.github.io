---
title: "snd_pcm_hw_rule_noresample(9)"
name: "snd_pcm_hw_rule_noresample"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_hw_rule_noresample/"
---

snd_pcm_hw_rule_noresample - add a rule to allow disabling hw resampling

<h2>Synopsis</h2>

<pre><code>int snd_pcm_hw_rule_noresample(struct snd_pcm_runtime *runtime, unsigned int base_rate);</code></pre>

<h2>Arguments</h2>

<i>runtime</i>
<dl><dd><dd>PCM runtime instance</dl>
 

 <i>base_rate</i>
<dl><dd>the rate at which the hardware does not resample</dl>

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


