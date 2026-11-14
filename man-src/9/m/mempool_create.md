---
title: "mempool_create(9)"
name: "mempool_create"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mempool_create/"
description: "mempool_create – create a memory pool"
---

<p>mempool_create &#8211; create a memory pool</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>mempool_t * mempool_create(int&nbsp;<wbr></code><i>min_nr</i><code>, mempool_alloc_t&nbsp;<wbr>*&nbsp;<wbr></code><i>alloc_fn</i><code>, mempool_free_t&nbsp;<wbr>*&nbsp;<wbr></code><i>free_fn</i><code>, void&nbsp;<wbr>*&nbsp;<wbr></code><i>pool_data</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>min_nr</i></p>
<dl>
<dd>
<dd>the minimum number of elements guaranteed to be allocated for this pool.</dl>
<p> <i>alloc_fn</i></p>
<dl>
<dd>user-defined element-allocation function.</dl>
<p> <i>free_fn</i></p>
<dl>
<dd>user-defined element-freeing function.</dl>
<p> <i>pool_data</i></p>
<dl>
<dd>optional private data available to the user-defined functions.</dl>
<h2>Description</h2>
<p>this function creates and allocates a guaranteed size, preallocated memory pool. The pool can be used from the <code>mempool_alloc</code> and <code>mempool_free</code> functions. This function might sleep. Both the <code>alloc_fn</code> and the <code>free_fn</code> functions might sleep &#8211; as long as the <code>mempool_alloc</code> function is not called from IRQ contexts.</p>
<h2>Copyright</h2>
