---
title: "snd_pcm_period_elapsed(9)"
name: "snd_pcm_period_elapsed"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_period_elapsed/"
---

snd_pcm_period_elapsed - update the pcm status for the next period

<h2>Synopsis</h2>

<pre><code>void snd_pcm_period_elapsed(struct snd_pcm_substream *substream);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>the pcm substream instance</dl>

<h2>Description</h2>

This function is called from the interrupt handler when the PCM has processed the period size. It will update the current pointer, wake up sleepers, etc. 

 Even if more than one periods have elapsed since the last call, you have to call this only once.

<h2>Copyright</h2>


