---
title: "snd_pcm_gettime(9)"
name: "snd_pcm_gettime"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_gettime/"
---

snd_pcm_gettime - Fill the timespec depending on the timestamp mode

<h2>Synopsis</h2>

<pre><code>void snd_pcm_gettime(struct snd_pcm_runtime *runtime, struct timespec *tv);</code></pre>

<h2>Arguments</h2>

<i>runtime</i>
<dl><dd><dd>PCM runtime instance</dl>
 

 <i>tv</i>
<dl><dd>timespec to fill</dl>

<h2>Copyright</h2>


