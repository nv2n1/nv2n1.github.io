---
title: "mdiobus_alloc_size(9)"
name: "mdiobus_alloc_size"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mdiobus_alloc_size/"
---

mdiobus_alloc_size - allocate a mii_bus structure

<h2>Synopsis</h2>

<pre><code>struct mii_bus *mdiobus_alloc_size(size_t size);</code></pre>

<h2>Arguments</h2>

<i>size</i>
<dl><dd><dd>extra amount of memory to allocate for private storage. If non-zero, then bus-&gt;priv is points to that memory.</dl>

<h2>Description</h2>

called by a bus driver to allocate an mii_bus structure to fill in.

<h2>Copyright</h2>


