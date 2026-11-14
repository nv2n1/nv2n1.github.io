---
title: "snd_pcm_lib_preallocate_pages_for_all(9)"
name: "snd_pcm_lib_preallocate_pages_for_all"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_lib_preallocate_pages_for_all/"
---

snd_pcm_lib_preallocate_pages_for_all - pre-allocation for continuous memory type (all substreams)

<h2>Synopsis</h2>

<pre><code>int snd_pcm_lib_preallocate_pages_for_all(struct snd_pcm *pcm, int type, void *data, size_t size, size_t max);</code></pre>

<h2>Arguments</h2>

<i>pcm</i>
<dl><dd><dd>the pcm instance</dl>
 

 <i>type</i>
<dl><dd>DMA type (SNDRV_DMA_TYPE_*)</dl>
 

 <i>data</i>
<dl><dd>DMA type dependent data</dl>
 

 <i>size</i>
<dl><dd>the requested pre-allocation size in bytes</dl>
 

 <i>max</i>
<dl><dd>the max. allowed pre-allocation size</dl>

<h2>Description</h2>

Do pre-allocation to all substreams of the given pcm for the specified DMA type.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


