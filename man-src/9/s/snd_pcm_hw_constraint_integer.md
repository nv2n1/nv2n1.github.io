---
title: "snd_pcm_hw_constraint_integer(9)"
name: "snd_pcm_hw_constraint_integer"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_hw_constraint_integer/"
---

snd_pcm_hw_constraint_integer - apply an integer constraint to an interval

<h2>Synopsis</h2>

<pre><code>int snd_pcm_hw_constraint_integer(struct snd_pcm_runtime *runtime, snd_pcm_hw_param_t var);</code></pre>

<h2>Arguments</h2>

<i>runtime</i>
<dl><dd><dd>PCM runtime instance</dl>
 

 <i>var</i>
<dl><dd>hw_params variable to apply the integer constraint</dl>

<h2>Description</h2>

Apply the constraint of integer to an interval parameter.

<h2>Return</h2>

Positive if the value is changed, zero if it's not changed, or a negative error code.

<h2>Copyright</h2>


