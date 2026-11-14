---
title: "snd_pcm_lib_default_mmap(9)"
name: "snd_pcm_lib_default_mmap"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_lib_default_mmap/"
---

snd_pcm_lib_default_mmap - Default PCM data mmap function

<h2>Synopsis</h2>

<pre><code>int snd_pcm_lib_default_mmap(struct snd_pcm_substream *substream, struct vm_area_struct *area);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>PCM substream</dl>
 

 <i>area</i>
<dl><dd>VMA</dl>

<h2>Description</h2>

This is the default mmap handler for PCM data. When mmap pcm_ops is NULL, this function is invoked implicitly.

<h2>Copyright</h2>


