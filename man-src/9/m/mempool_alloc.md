---
title: "mempool_alloc(9)"
name: "mempool_alloc"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mempool_alloc/"
description: "mempool_alloc – allocate an element from a specific memory pool"
---

<p>mempool_alloc &#8211; allocate an element from a specific memory pool</p>
<h2>Synopsis</h2>
<pre><code>void *mempool_alloc(mempool_t *pool, gfp_t gfp_mask);</code></pre>
<h2>Arguments</h2>
<p><i>pool</i></p>
<dl>
<dd>
<dd>pointer to the memory pool which was allocated via <code>mempool_create</code>.</dl>
<p> <i>gfp_mask</i></p>
<dl>
<dd>the usual allocation bitmask.</dl>
<h2>Description</h2>
<p>this function only sleeps if the <code>alloc_fn</code> function sleeps or returns NULL. Note that due to preallocation, this function *never* fails when called from process contexts. (it might fail if called from an IRQ context.)</p>
<h2>Note</h2>
<p>using __GFP_ZERO is not supported.</p>
<h2>Copyright</h2>
