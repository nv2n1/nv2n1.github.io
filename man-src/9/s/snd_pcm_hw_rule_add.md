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
<dl><dd></dd><dd>the pcm runtime instance</dd></dl>
 

 <i>cond</i>
<dl><dd>condition bits</dd></dl>
 

 <i>var</i>
<dl><dd>the variable to evaluate</dd></dl>
 

 <i>func</i>
<dl><dd>the evaluation function</dd></dl>
 

 <i>private</i>
<dl><dd>the private data pointer passed to function</dd></dl>
 

 <i>dep</i>
<dl><dd>the dependent variables</dd></dl>
 

 <i>...</i>
<dl><dd>variable arguments</dd></dl>

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


