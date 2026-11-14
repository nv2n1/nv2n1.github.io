---
title: "snd_malloc_pages(9)"
name: "snd_malloc_pages"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_malloc_pages/"
description: "snd_malloc_pages – allocate pages with the given size"
---

<p>snd_malloc_pages &#8211; allocate pages with the given size</p>
<h2>Synopsis</h2>
<pre><code>void *snd_malloc_pages(size_t size, gfp_t gfp_flags);</code></pre>
<h2>Arguments</h2>
<p><i>size</i></p>
<dl>
<dd>
<dd>the size to allocate in bytes</dl>
<p> <i>gfp_flags</i></p>
<dl>
<dd>the allocation conditions, GFP_XXX</dl>
<h2>Description</h2>
<p>Allocates the physically contiguous pages with the given size.</p>
<h2>Return</h2>
<p>The pointer of the buffer, or <code>NULL</code> if no enough memory.</p>
<h2>Copyright</h2>
