---
title: "snd_pcm_hw_param_last(9)"
name: "snd_pcm_hw_param_last"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_hw_param_last/"
description: "snd_pcm_hw_param_last – refine config space and return maximum value"
---

<p>snd_pcm_hw_param_last &#8211; refine config space and return maximum value</p>
<h2>Synopsis</h2>
<pre><code>int snd_pcm_hw_param_last(struct snd_pcm_substream *pcm, struct snd_pcm_hw_params *params, snd_pcm_hw_param_t var, int *dir);</code></pre>
<h2>Arguments</h2>
<p><i>pcm</i></p>
<dl>
<dd>
<dd>PCM instance</dl>
<p> <i>params</i></p>
<dl>
<dd>the hw_params instance</dl>
<p> <i>var</i></p>
<dl>
<dd>parameter to retrieve</dl>
<p> <i>dir</i></p>
<dl>
<dd>pointer to the direction (-1,0,1) or <code>NULL</code></dl>
<h2>Description</h2>
<p>Inside configuration space defined by <i>params</i> remove from <i>var</i> all values &lt; maximum. Reduce configuration space accordingly.</p>
<h2>Return</h2>
<p>The maximum, or a negative error code on failure.</p>
<h2>Copyright</h2>
