---
title: "snd_pcm_hw_rule_add(9)"
name: "snd_pcm_hw_rule_add"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_hw_rule_add/"
---

snd_pcm_hw_rule_add - add the hw-constraint rule

<h2>Synopsis</h2>

<pre><code>int snd_pcm_hw_rule_add(struct snd_pcm_runtime *runtime, unsigned int cond, int var, snd_pcm_hw_rule_func_t func, void *private, int dep, ...);</code></pre>

<h2>Arguments</h2>

<i>runtime</i>
<dl><dd><dd>the pcm runtime instance</dl>
 

 <i>cond</i>
<dl><dd>condition bits</dl>
 

 <i>var</i>
<dl><dd>the variable to evaluate</dl>
 

 <i>func</i>
<dl><dd>the evaluation function</dl>
 

 <i>private</i>
<dl><dd>the private data pointer passed to function</dl>
 

 <i>dep</i>
<dl><dd>the dependent variables</dl>
 

 <i>...</i>
<dl><dd>variable arguments</dl>

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


