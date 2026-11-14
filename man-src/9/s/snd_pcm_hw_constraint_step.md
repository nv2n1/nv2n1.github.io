---
title: "snd_pcm_hw_constraint_step(9)"
name: "snd_pcm_hw_constraint_step"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_hw_constraint_step/"
---

snd_pcm_hw_constraint_step - add a hw constraint step rule

<h2>Synopsis</h2>

<pre><code>int snd_pcm_hw_constraint_step(struct snd_pcm_runtime *runtime, unsigned int cond, snd_pcm_hw_param_t var, unsigned long step);</code></pre>

<h2>Arguments</h2>

<i>runtime</i>
<dl><dd><dd>PCM runtime instance</dl>
 

 <i>cond</i>
<dl><dd>condition bits</dl>
 

 <i>var</i>
<dl><dd>hw_params variable to apply the step constraint</dl>
 

 <i>step</i>
<dl><dd>step size</dl>

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


