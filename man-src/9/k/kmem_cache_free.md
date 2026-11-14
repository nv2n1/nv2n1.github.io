---
title: "kmem_cache_free(9)"
name: "kmem_cache_free"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kmem_cache_free/"
---

kmem_cache_free - Deallocate an object

<h2>Synopsis</h2>

<pre><code>void kmem_cache_free(struct kmem_cache *cachep, void *objp);</code></pre>

<h2>Arguments</h2>

<i>cachep</i>
<dl><dd><dd>The cache the allocation was from.</dl>
 

 <i>objp</i>
<dl><dd>The previously allocated object.</dl>

<h2>Description</h2>

Free an object which was previously allocated from this cache.

<h2>Copyright</h2>


