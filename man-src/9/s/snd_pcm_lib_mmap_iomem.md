---
title: "snd_pcm_lib_mmap_iomem(9)"
name: "snd_pcm_lib_mmap_iomem"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_lib_mmap_iomem/"
---

snd_pcm_lib_mmap_iomem - Default PCM data mmap function for I/O mem

<h2>Synopsis</h2>

<pre><code>int snd_pcm_lib_mmap_iomem(struct snd_pcm_substream *substream, struct vm_area_struct *area);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>PCM substream</dl>
 

 <i>area</i>
<dl><dd>VMA</dl>

<h2>Description</h2>

When your hardware uses the iomapped pages as the hardware buffer and wants to mmap it, pass this function as mmap pcm_ops. Note that this is supposed to work only on limited architectures.

<h2>Copyright</h2>


