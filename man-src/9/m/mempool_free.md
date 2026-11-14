---
title: "mempool_free(9)"
name: "mempool_free"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mempool_free/"
description: "mempool_free – return an element to the pool."
---

<p>mempool_free &#8211; return an element to the pool.</p>
<h2>Synopsis</h2>
<pre><code>void mempool_free(void *element, mempool_t *pool);</code></pre>
<h2>Arguments</h2>
<p><i>element</i></p>
<dl>
<dd>
<dd>pool element pointer.</dl>
<p> <i>pool</i></p>
<dl>
<dd>pointer to the memory pool which was allocated via <code>mempool_create</code>.</dl>
<h2>Description</h2>
<p>this function only sleeps if the <code>free_fn</code> function sleeps.</p>
<h2>Copyright</h2>
