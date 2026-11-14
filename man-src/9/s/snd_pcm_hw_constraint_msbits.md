---
title: "snd_pcm_hw_constraint_msbits(9)"
name: "snd_pcm_hw_constraint_msbits"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_hw_constraint_msbits/"
---

snd_pcm_hw_constraint_msbits - add a hw constraint msbits rule

<h2>Synopsis</h2>

<pre><code>int snd_pcm_hw_constraint_msbits(struct snd_pcm_runtime *runtime, unsigned int cond, unsigned int width, unsigned int msbits);</code></pre>

<h2>Arguments</h2>

<i>runtime</i>
<dl><dd><dd>PCM runtime instance</dl>
 

 <i>cond</i>
<dl><dd>condition bits</dl>
 

 <i>width</i>
<dl><dd>sample bits width</dl>
 

 <i>msbits</i>
<dl><dd>msbits width</dl>

<h2>Description</h2>

This constraint will set the number of most significant bits (msbits) if a sample format with the specified width has been select. If width is set to 0 the msbits will be set for any sample format with a width larger than the specified msbits.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


