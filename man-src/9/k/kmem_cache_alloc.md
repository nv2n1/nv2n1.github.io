---
title: "kmem_cache_alloc(9)"
name: "kmem_cache_alloc"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kmem_cache_alloc/"
description: "kmem_cache_alloc – Allocate an object"
---

<p>kmem_cache_alloc &#8211; Allocate an object</p>
<h2>Synopsis</h2>
<pre><code>void *kmem_cache_alloc(struct kmem_cache *cachep, gfp_t flags);</code></pre>
<h2>Arguments</h2>
<p><i>cachep</i></p>
<dl>
<dd>
<dd>The cache to allocate from.</dl>
<p> <i>flags</i></p>
<dl>
<dd>See <code>kmalloc</code>.</dl>
<h2>Description</h2>
<p>Allocate an object from this cache. The flags are only relevant if the cache has no available objects.</p>
<h2>Copyright</h2>
