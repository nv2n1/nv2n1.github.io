---
title: "snd_pcm_lib_preallocate_free_for_all(9)"
name: "snd_pcm_lib_preallocate_free_for_all"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_lib_preallocate_free_for_all/"
---

snd_pcm_lib_preallocate_free_for_all - release all pre-allocated buffers on the pcm

<h2>Synopsis</h2>

<pre><code>int snd_pcm_lib_preallocate_free_for_all(struct snd_pcm *pcm);</code></pre>

<h2>Arguments</h2>

<i>pcm</i>
<dl><dd><dd>the pcm instance</dl>

<h2>Description</h2>

Releases all the pre-allocated buffers on the given pcm.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


