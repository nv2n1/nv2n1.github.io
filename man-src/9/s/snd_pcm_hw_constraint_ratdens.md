---
title: "snd_pcm_hw_constraint_ratdens(9)"
name: "snd_pcm_hw_constraint_ratdens"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_hw_constraint_ratdens/"
---

snd_pcm_hw_constraint_ratdens - apply ratdens constraint to a parameter

<h2>Synopsis</h2>

<pre><code>int snd_pcm_hw_constraint_ratdens(struct snd_pcm_runtime *runtime, unsigned int cond, snd_pcm_hw_param_t var, const struct snd_pcm_hw_constraint_ratdens *r);</code></pre>

<h2>Arguments</h2>

<i>runtime</i>
<dl><dd><dd>PCM runtime instance</dl>
 

 <i>cond</i>
<dl><dd>condition bits</dl>
 

 <i>var</i>
<dl><dd>hw_params variable to apply the ratdens constraint</dl>
 

 <i>r</i>
<dl><dd>struct snd_ratdens constriants</dl>

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


