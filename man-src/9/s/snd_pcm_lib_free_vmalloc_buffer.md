---
title: "snd_pcm_lib_free_vmalloc_buffer(9)"
name: "snd_pcm_lib_free_vmalloc_buffer"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_lib_free_vmalloc_buffer/"
description: "snd_pcm_lib_free_vmalloc_buffer – free vmalloc buffer"
---

<p>snd_pcm_lib_free_vmalloc_buffer &#8211; free vmalloc buffer</p>
<h2>Synopsis</h2>
<pre><code>int snd_pcm_lib_free_vmalloc_buffer(struct snd_pcm_substream *substream);</code></pre>
<h2>Arguments</h2>
<p><i>substream</i></p>
<dl>
<dd>
<dd>the substream with a buffer allocated by <code>snd_pcm_lib_alloc_vmalloc_buffer</code></dl>
<h2>Return</h2>
<p>Zero if successful, or a negative error code on failure.</p>
<h2>Copyright</h2>
