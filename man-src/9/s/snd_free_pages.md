---
title: "snd_free_pages(9)"
name: "snd_free_pages"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_free_pages/"
description: "snd_free_pages – release the pages"
---

<p>snd_free_pages &#8211; release the pages</p>
<h2>Synopsis</h2>
<pre><code>void snd_free_pages(void *ptr, size_t size);</code></pre>
<h2>Arguments</h2>
<p><i>ptr</i></p>
<dl>
<dd>
<dd>the buffer pointer to release</dl>
<p> <i>size</i></p>
<dl>
<dd>the allocated buffer size</dl>
<h2>Description</h2>
<p>Releases the buffer allocated via <code>snd_malloc_pages</code>.</p>
<h2>Copyright</h2>
