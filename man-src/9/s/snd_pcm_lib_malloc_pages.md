---
title: "snd_pcm_lib_malloc_pages(9)"
name: "snd_pcm_lib_malloc_pages"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_lib_malloc_pages/"
description: "snd_pcm_lib_malloc_pages – allocate the DMA buffer"
---

<p>snd_pcm_lib_malloc_pages &#8211; allocate the DMA buffer</p>
<h2>Synopsis</h2>
<pre><code>int snd_pcm_lib_malloc_pages(struct snd_pcm_substream *substream, size_t size);</code></pre>
<h2>Arguments</h2>
<p><i>substream</i></p>
<dl>
<dd>
<dd>the substream to allocate the DMA buffer to</dl>
<p> <i>size</i></p>
<dl>
<dd>the requested buffer size in bytes</dl>
<h2>Description</h2>
<p>Allocates the DMA buffer on the BUS type given earlier to <code>snd_pcm_lib_preallocate_xxx_pages</code>.</p>
<h2>Return</h2>
<p>1 if the buffer is changed, 0 if not changed, or a negative code on failure.</p>
<h2>Copyright</h2>
