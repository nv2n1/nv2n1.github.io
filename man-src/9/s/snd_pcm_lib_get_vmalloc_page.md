---
title: "snd_pcm_lib_get_vmalloc_page(9)"
name: "snd_pcm_lib_get_vmalloc_page"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_lib_get_vmalloc_page/"
description: "snd_pcm_lib_get_vmalloc_page – map vmalloc buffer offset to page struct"
---

<p>snd_pcm_lib_get_vmalloc_page &#8211; map vmalloc buffer offset to page struct</p>
<h2>Synopsis</h2>
<pre><code>struct page *snd_pcm_lib_get_vmalloc_page(struct snd_pcm_substream *substream, unsigned long offset);</code></pre>
<h2>Arguments</h2>
<p><i>substream</i></p>
<dl>
<dd>
<dd>the substream with a buffer allocated by <code>snd_pcm_lib_alloc_vmalloc_buffer</code></dl>
<p> <i>offset</i></p>
<dl>
<dd>offset in the buffer</dl>
<h2>Description</h2>
<p>This function is to be used as the page callback in the PCM ops.</p>
<h2>Return</h2>
<p>The page struct, or <code>NULL</code> on failure.</p>
<h2>Copyright</h2>
