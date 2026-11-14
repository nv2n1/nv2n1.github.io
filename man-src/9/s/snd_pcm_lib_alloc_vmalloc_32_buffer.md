---
title: "snd_pcm_lib_alloc_vmalloc_32_buffer(9)"
name: "snd_pcm_lib_alloc_vmalloc_32_buffer"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_lib_alloc_vmalloc_32_buffer/"
description: "snd_pcm_lib_alloc_vmalloc_32_buffer – allocate 32-bit-addressable buffer"
---

<p>snd_pcm_lib_alloc_vmalloc_32_buffer &#8211; allocate 32-bit-addressable buffer</p>
<h2>Synopsis</h2>
<pre><code>int snd_pcm_lib_alloc_vmalloc_32_buffer(struct snd_pcm_substream *substream, size_t size);</code></pre>
<h2>Arguments</h2>
<p><i>substream</i></p>
<dl>
<dd>
<dd>the substream to allocate the buffer to</dl>
<p> <i>size</i></p>
<dl>
<dd>the requested buffer size, in bytes</dl>
<h2>Description</h2>
<p>This function works like <code>snd_pcm_lib_alloc_vmalloc_buffer</code>, but uses <code>vmalloc_32</code>, i.e., the pages are allocated from 32-bit-addressable memory.</p>
<h2>Return</h2>
<p>1 if the buffer was changed, 0 if not changed, or a negative error code.</p>
<h2>Copyright</h2>
