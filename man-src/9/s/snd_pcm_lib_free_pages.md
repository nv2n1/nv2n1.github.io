---
title: "snd_pcm_lib_free_pages(9)"
name: "snd_pcm_lib_free_pages"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_lib_free_pages/"
description: "snd_pcm_lib_free_pages – release the allocated DMA buffer."
---

<p>snd_pcm_lib_free_pages &#8211; release the allocated DMA buffer.</p>
<h2>Synopsis</h2>
<pre><code>int snd_pcm_lib_free_pages(struct snd_pcm_substream *substream);</code></pre>
<h2>Arguments</h2>
<p><i>substream</i></p>
<dl>
<dd>
<dd>the substream to release the DMA buffer</dl>
<h2>Description</h2>
<p>Releases the DMA buffer allocated via <code>snd_pcm_lib_malloc_pages</code>.</p>
<h2>Return</h2>
<p>Zero if successful, or a negative error code on failure.</p>
<h2>Copyright</h2>
