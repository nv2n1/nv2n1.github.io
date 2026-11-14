---
title: "mempool_destroy(9)"
name: "mempool_destroy"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mempool_destroy/"
description: "mempool_destroy – deallocate a memory pool"
---

<p>mempool_destroy &#8211; deallocate a memory pool</p>
<h2>Synopsis</h2>
<pre><code>void mempool_destroy(mempool_t *pool);</code></pre>
<h2>Arguments</h2>
<p><i>pool</i></p>
<dl>
<dd>
<dd>pointer to the memory pool which was allocated via <code>mempool_create</code>.</dl>
<h2>Description</h2>
<p>Free all reserved elements in <i>pool</i> and <i>pool</i> itself. This function only sleeps if the <code>free_fn</code> function sleeps.</p>
<h2>Copyright</h2>
