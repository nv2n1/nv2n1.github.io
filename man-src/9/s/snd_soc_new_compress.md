---
title: "snd_soc_new_compress(9)"
name: "snd_soc_new_compress"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_new_compress/"
---

snd_soc_new_compress - create a new compress.

<h2>Synopsis</h2>

<pre><code>int snd_soc_new_compress(struct snd_soc_pcm_runtime *rtd, int num);</code></pre>

<h2>Arguments</h2>

<i>rtd</i>
<dl><dd><dd>The runtime for which we will create compress</dl>
 

 <i>num</i>
<dl><dd>the device index number (zero based - shared with normal PCMs)</dl>

<h2>Return</h2>

0 for success, else error.

<h2>Copyright</h2>


