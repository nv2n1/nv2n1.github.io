---
title: "snd_pcm_hw_constraint_ranges(9)"
name: "snd_pcm_hw_constraint_ranges"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_hw_constraint_ranges/"
---

snd_pcm_hw_constraint_ranges - apply list of range constraints to a parameter

<h2>Synopsis</h2>

<pre><code>int snd_pcm_hw_constraint_ranges(struct snd_pcm_runtime *runtime, unsigned int cond, snd_pcm_hw_param_t var, const struct snd_pcm_hw_constraint_ranges *r);</code></pre>

<h2>Arguments</h2>

<i>runtime</i>
<dl><dd><dd>PCM runtime instance</dl>
 

 <i>cond</i>
<dl><dd>condition bits</dl>
 

 <i>var</i>
<dl><dd>hw_params variable to apply the list of range constraints</dl>
 

 <i>r</i>
<dl><dd>ranges</dl>

<h2>Description</h2>

Apply the list of range constraints to an interval parameter.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


