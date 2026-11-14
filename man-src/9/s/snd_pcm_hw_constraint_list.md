---
title: "snd_pcm_hw_constraint_list(9)"
name: "snd_pcm_hw_constraint_list"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_hw_constraint_list/"
---

snd_pcm_hw_constraint_list - apply a list of constraints to a parameter

<h2>Synopsis</h2>

<pre><code>int snd_pcm_hw_constraint_list(struct snd_pcm_runtime *runtime, unsigned int cond, snd_pcm_hw_param_t var, const struct snd_pcm_hw_constraint_list *l);</code></pre>

<h2>Arguments</h2>

<i>runtime</i>
<dl><dd><dd>PCM runtime instance</dl>
 

 <i>cond</i>
<dl><dd>condition bits</dl>
 

 <i>var</i>
<dl><dd>hw_params variable to apply the list constraint</dl>
 

 <i>l</i>
<dl><dd>list</dl>

<h2>Description</h2>

Apply the list of constraints to an interval parameter.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


