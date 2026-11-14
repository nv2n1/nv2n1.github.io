---
title: "snd_pcm_lib_alloc_vmalloc_buffer(9)"
name: "snd_pcm_lib_alloc_vmalloc_buffer"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_lib_alloc_vmalloc_buffer/"
description: "snd_pcm_lib_alloc_vmalloc_buffer – allocate virtual DMA buffer"
---

<p>snd_pcm_lib_alloc_vmalloc_buffer &#8211; allocate virtual DMA buffer</p>
<h2>Synopsis</h2>
<pre><code>int snd_pcm_lib_alloc_vmalloc_buffer(struct snd_pcm_substream *substream, size_t size);</code></pre>
<h2>Arguments</h2>
<p><i>substream</i></p>
<dl>
<dd>
<dd>the substream to allocate the buffer to</dl>
<p> <i>size</i></p>
<dl>
<dd>the requested buffer size, in bytes</dl>
<h2>Description</h2>
<p>Allocates the PCM substream buffer using <code>vmalloc</code>, i.e., the memory is contiguous in kernel virtual space, but not in physical memory. Use this if the buffer is accessed by kernel code but not by device DMA.</p>
<h2>Return</h2>
<p>1 if the buffer was changed, 0 if not changed, or a negative error code.</p>
<h2>Copyright</h2>
