---
title: "snd_pcm_hw_param_value(9)"
name: "snd_pcm_hw_param_value"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_hw_param_value/"
description: "snd_pcm_hw_param_value – return params field var value"
---

<p>snd_pcm_hw_param_value &#8211; return <i>params</i> field <i>var</i> value</p>
<h2>Synopsis</h2>
<pre><code>int snd_pcm_hw_param_value(const struct snd_pcm_hw_params *params, snd_pcm_hw_param_t var, int *dir);</code></pre>
<h2>Arguments</h2>
<p><i>params</i></p>
<dl>
<dd>
<dd>the hw_params instance</dl>
<p> <i>var</i></p>
<dl>
<dd>parameter to retrieve</dl>
<p> <i>dir</i></p>
<dl>
<dd>pointer to the direction (-1,0,1) or <code>NULL</code></dl>
<h2>Return</h2>
<p>The value for field <i>var</i> if it&#8217;s fixed in configuration space defined by <i>params</i>. &#8211;<code>EINVAL</code> otherwise.</p>
<h2>Copyright</h2>
