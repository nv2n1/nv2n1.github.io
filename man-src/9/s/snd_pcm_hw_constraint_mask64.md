---
title: "snd_pcm_hw_constraint_mask64(9)"
name: "snd_pcm_hw_constraint_mask64"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_hw_constraint_mask64/"
---

snd_pcm_hw_constraint_mask64 - apply the given bitmap mask constraint

<h2>Synopsis</h2>

<pre><code>int snd_pcm_hw_constraint_mask64(struct snd_pcm_runtime *runtime, snd_pcm_hw_param_t var, u_int64_t mask);</code></pre>

<h2>Arguments</h2>

<i>runtime</i>
<dl><dd><dd>PCM runtime instance</dl>
 

 <i>var</i>
<dl><dd>hw_params variable to apply the mask</dl>
 

 <i>mask</i>
<dl><dd>the 64bit bitmap mask</dl>

<h2>Description</h2>

Apply the constraint of the given bitmap mask to a 64-bit mask parameter.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


