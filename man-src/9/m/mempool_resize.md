---
title: "mempool_resize(9)"
name: "mempool_resize"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mempool_resize/"
description: "mempool_resize – resize an existing memory pool"
---

<p>mempool_resize &#8211; resize an existing memory pool</p>
<h2>Synopsis</h2>
<pre><code>int mempool_resize(mempool_t *pool, int new_min_nr);</code></pre>
<h2>Arguments</h2>
<p><i>pool</i></p>
<dl>
<dd>
<dd>pointer to the memory pool which was allocated via <code>mempool_create</code>.</dl>
<p> <i>new_min_nr</i></p>
<dl>
<dd>the new minimum number of elements guaranteed to be allocated for this pool.</dl>
<h2>Description</h2>
<p>This function shrinks/grows the pool. In the case of growing, it cannot be guaranteed that the pool will be grown to the new size immediately, but new <code>mempool_free</code> calls will refill it. This function may sleep. </p>
<p> Note, the caller must guarantee that no mempool_destroy is called while this function is running. <code>mempool_alloc</code> &amp; <code>mempool_free</code> might be called (eg. from IRQ contexts) while this function executes.</p>
<h2>Copyright</h2>
