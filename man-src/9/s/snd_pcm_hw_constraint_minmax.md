---
title: "snd_pcm_hw_constraint_minmax(9)"
name: "snd_pcm_hw_constraint_minmax"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_hw_constraint_minmax/"
---

snd_pcm_hw_constraint_minmax - apply a min/max range constraint to an interval

<h2>Synopsis</h2>

<pre><code>int snd_pcm_hw_constraint_minmax(struct snd_pcm_runtime *runtime, snd_pcm_hw_param_t var, unsigned int min, unsigned int max);</code></pre>

<h2>Arguments</h2>

<i>runtime</i>
<dl><dd><dd>PCM runtime instance</dl>
 

 <i>var</i>
<dl><dd>hw_params variable to apply the range</dl>
 

 <i>min</i>
<dl><dd>the minimal value</dl>
 

 <i>max</i>
<dl><dd>the maximal value</dl>

<h2>Description</h2>

Apply the min/max range constraint to an interval parameter.

<h2>Return</h2>

Positive if the value is changed, zero if it's not changed, or a negative error code.

<h2>Copyright</h2>


