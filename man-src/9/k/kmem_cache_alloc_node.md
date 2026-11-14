---
title: "kmem_cache_alloc_node(9)"
name: "kmem_cache_alloc_node"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kmem_cache_alloc_node/"
description: "kmem_cache_alloc_node – Allocate an object on the specified node"
---

<p>kmem_cache_alloc_node &#8211; Allocate an object on the specified node</p>
<h2>Synopsis</h2>
<pre><code>void *kmem_cache_alloc_node(struct kmem_cache *cachep, gfp_t flags, int nodeid);</code></pre>
<h2>Arguments</h2>
<p><i>cachep</i></p>
<dl>
<dd>
<dd>The cache to allocate from.</dl>
<p> <i>flags</i></p>
<dl>
<dd>See <code>kmalloc</code>.</dl>
<p> <i>nodeid</i></p>
<dl>
<dd>node number of the target node.</dl>
<h2>Description</h2>
<p>Identical to kmem_cache_alloc but it will allocate memory on the given node, which can improve the performance for cpu bound structures. </p>
<p> Fallback to other node is possible if __GFP_THISNODE is not set.</p>
<h2>Copyright</h2>
