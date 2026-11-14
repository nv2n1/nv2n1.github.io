---
title: "snd_pcm_hw_constraint_single(9)"
name: "snd_pcm_hw_constraint_single"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_hw_constraint_single/"
---

snd_pcm_hw_constraint_single - Constrain parameter to a single value

<h2>Synopsis</h2>

<pre><code>int snd_pcm_hw_constraint_single(struct snd_pcm_runtime *runtime, snd_pcm_hw_param_t var, unsigned int val);</code></pre>

<h2>Arguments</h2>

<i>runtime</i>
<dl><dd><dd>PCM runtime instance</dl>
 

 <i>var</i>
<dl><dd>The hw_params variable to constrain</dl>
 

 <i>val</i>
<dl><dd>The value to constrain to</dl>

<h2>Return</h2>

Positive if the value is changed, zero if it's not changed, or a negative error code.

<h2>Copyright</h2>


